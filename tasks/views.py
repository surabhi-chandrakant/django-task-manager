# tasks/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count, Q
from django.utils import timezone
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
import json
from datetime import datetime, timedelta

# API ViewSets
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'assigned_to']
    search_fields = ['title', 'description', 'tags']
    ordering_fields = ['created_at', 'due_date', 'priority']
    ordering = ['-created_at']
    
    def get_queryset(self):
        return Task.objects.filter(
            Q(created_by=self.request.user) | Q(assigned_to=self.request.user)
        ).distinct()
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        tasks = self.get_queryset()
        
        status_stats = tasks.values('status').annotate(count=Count('id'))
        priority_stats = tasks.values('priority').annotate(count=Count('id'))
        
        # Monthly completion stats
        current_date = timezone.now().date()
        monthly_stats = []
        for i in range(6):
            month_start = current_date.replace(day=1) - timedelta(days=i*30)
            month_end = (month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            completed_count = tasks.filter(
                completed_at__date__range=[month_start, month_end]
            ).count()
            monthly_stats.append({
                'month': month_start.strftime('%b %Y'),
                'completed': completed_count
            })
        
        return Response({
            'status_distribution': list(status_stats),
            'priority_distribution': list(priority_stats),
            'monthly_completion': list(reversed(monthly_stats)),
            'total_tasks': tasks.count(),
            'completed_tasks': tasks.filter(status='completed').count(),
            'overdue_tasks': sum(1 for task in tasks if task.is_overdue)
        })

# Web Views
@login_required
def dashboard(request):
    tasks = Task.objects.filter(
        Q(created_by=request.user) | Q(assigned_to=request.user)
    ).distinct()
    
    context = {
        'total_tasks': tasks.count(),
        'pending_tasks': tasks.filter(status='pending').count(),
        'completed_tasks': tasks.filter(status='completed').count(),
        'overdue_tasks': sum(1 for task in tasks if task.is_overdue),
        'recent_tasks': tasks[:5]
    }
    return render(request, 'dashboard.html', context)

@login_required
def task_list(request):
    tasks = Task.objects.filter(
        Q(created_by=request.user) | Q(assigned_to=request.user)
    ).distinct()
    
    # Filters
    status = request.GET.get('status')
    priority = request.GET.get('priority')
    search = request.GET.get('search')
    
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
    
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'medium'),
            due_date=data.get('due_date'),
            created_by=request.user,
            tags=data.get('tags', '')
        )
        return JsonResponse({'success': True, 'task_id': task.id})
    
    return render(request, 'tasks/task_form.html')