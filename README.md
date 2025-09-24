# Django Task Management System

A comprehensive web application built with Django and PostgreSQL featuring CRUD operations, weather API integration, and data visualization.

## 🚀 Features

- **CRUD Operations**: Full task management with REST APIs
- **Weather Integration**: Real-time weather data from OpenWeatherMap API
- **Data Visualization**: Charts and reports using Chart.js
- **User Authentication**: Django's built-in authentication system
- **Responsive Design**: Bootstrap-powered UI
- **RESTful APIs**: Django REST Framework implementation

## 🛠️ Technology Stack

- **Backend**: Django 4.2, Django REST Framework
- **Database**: PostgreSQL (with Supabase option)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5, Chart.js
- **API Integration**: OpenWeatherMap API
- **Deployment**: Railway/Heroku ready

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL or Supabase account
- Git
- OpenWeatherMap API key (free tier available)

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-task-manager.git
cd django-task-manager
```

### 2. Create Virtual Environment

```bash
python -m venv task_env
source task_env/bin/activate  # On Windows: task_env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://username:password@localhost:5432/taskdb
WEATHER_API_KEY=your-openweathermap-api-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the Application

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📁 Project Structure

```
django-task-manager/
├── task_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── tests.py
├── weather/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   └── services.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── tasks/
│   │   ├── task_list.html
│   │   ├── task_detail.html
│   │   └── task_form.html
│   └── weather/
│       └── weather_dashboard.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🔌 API Endpoints

### Task Management APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create new task |
| GET | `/api/tasks/{id}/` | Get specific task |
| PUT | `/api/tasks/{id}/` | Update task |
| DELETE | `/api/tasks/{id}/` | Delete task |

### Weather API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/weather/{city}/` | Get weather for city |

### Example API Usage

```bash
# Create a new task
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete Django Project",
    "description": "Build a task management system",
    "priority": "high",
    "due_date": "2024-12-31"
  }'

# Get weather data
curl http://localhost:8000/api/weather/London/
```

## 📊 Data Visualization Features

1. **Task Status Distribution**: Pie chart showing task completion rates
2. **Priority Analysis**: Bar chart of tasks by priority level
3. **Monthly Progress**: Line chart tracking task completion over time
4. **Weather Integration**: Current weather display with location-based data

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Test specific app:

```bash
python manage.py test tasks
python manage.py test weather
```

## 🚀 Deployment

### Railway Deployment

1. Create a Railway account at [railway.app](https://railway.app)
2. Connect your GitHub repository
3. Add environment variables in Railway dashboard
4. Deploy automatically on push

### Environment Variables for Production

```env
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=your-postgresql-connection-string
WEATHER_API_KEY=your-api-key
ALLOWED_HOSTS=your-domain.railway.app
```

## 🔐 Security Features

- CSRF protection enabled
- SQL injection prevention via Django ORM
- XSS protection with template auto-escaping
- Secure headers configuration
- Environment-based configuration

## 📱 Frontend Features

- **Responsive Design**: Mobile-friendly interface
- **Interactive Charts**: Real-time data visualization
- **AJAX Requests**: Seamless user experience
- **Form Validation**: Client and server-side validation
- **Toast Notifications**: User feedback system

## 🌤️ Weather Integration Details

The application integrates with OpenWeatherMap API to provide:
- Current weather conditions
- Location-based weather data
- Weather-aware task scheduling suggestions
- Historical weather data visualization

## 📈 Performance Optimizations

- Database query optimization with select_related
- Static file compression
- Caching for weather data
- Pagination for large datasets
- Lazy loading for charts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify PostgreSQL is running
   - Check DATABASE_URL in .env file

2. **Weather API Not Working**
   - Confirm WEATHER_API_KEY is valid
   - Check API rate limits

3. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_URL configuration

## 📞 Support

For questions or issues, please:
- Open an issue on GitHub
- Check the troubleshooting section
- Review Django documentation

## 🎯 Future Enhancements

- [ ] Real-time notifications with WebSocket
- [ ] Email reminders for due tasks
- [ ] Team collaboration features
- [ ] Mobile app with React Native
- [ ] Advanced analytics dashboard
- [ ] Integration with calendar applications

---

