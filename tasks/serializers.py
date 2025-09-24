# tasks/serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    assigned_to_username = serializers.CharField(source='assigned_to.username', read_only=True)
    is_overdue = serializers.ReadOnlyField()
    tags_list = serializers.ReadOnlyField(source='get_tags_list')
    
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'priority', 'status',
            'created_at', 'updated_at', 'due_date', 'completed_at',
            'created_by', 'created_by_username', 'assigned_to', 
            'assigned_to_username', 'tags', 'tags_list', 'is_overdue'
        ]
        read_only_fields = ['created_by', 'completed_at']
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)