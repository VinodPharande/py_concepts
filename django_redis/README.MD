# Step 1: Install the Required Tools:

## 1. Install Python: Make sure Python (version 3.7 or above) is installed.

1.1 Check with: python --version

1.2 If not installed, download it from python.org.

## 2. Install Redis:

2.1 Follow the [Redis installation instructions] <https://redis.io/docs/getting-started/installation/> for your operating system.

2.2 Start the Redis server:

`bash> redis-server`

## 3. Set Up a Virtual Environment:

`python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
`

## 4. Install Django and Django-Redis:

`pip install django django-redis`

# Step 2: Create a Django Project:

2.1 Run these commands to set up a project and an app:  
`django-admin startproject myproject
cd myproject
python manage.py startapp myapp
`

# Step 3: Configure Redis in settings.py:

Open the myproject/settings.py file and configure Redis as the cache backend:  
`# settings.py
INSTALLED_APPS += ['myapp']

CACHES = {
"default": {
"BACKEND": "django_redis.cache.RedisCache",
"LOCATION": "redis://127.0.0.1:6379/1",
"OPTIONS": {
"CLIENT_CLASS": "django_redis.client.DefaultClient",
},
}
}

# Optional: Set a fallback if Redis is unavailable

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
`

# Step 4: Create a View with Redis Cache:

Edit myapp/views.py  
`from django.core.cache import cache
from django.http import JsonResponse
import time

def expensive_operation_view(request):
cache_key = "expensive_data" # Unique key for this cache
cached_data = cache.get(cache_key) # Check if data exists in Redis

    if cached_data:
        return JsonResponse({"data": cached_data, "source": "cache"})

    # Simulate an expensive operation (e.g., database query)
    time.sleep(5)  # Simulating delay
    expensive_data = {"message": "Result of an expensive computation"}

    # Store the data in Redis with a TTL (e.g., 30 seconds)
    cache.set(cache_key, expensive_data, timeout=30)

    return JsonResponse({"data": expensive_data, "source": "server"})

`

# Step 5: Add the URL:

Edit myproject/urls.py to add a URL for the view:  
`from django.contrib import admin
from django.urls import path
from myapp.views import expensive_operation_view

urlpatterns = [
path('admin/', admin.site.urls),
path('expensive/', expensive_operation_view),
]
`

# Step 6: Run the Development Server:

6.1 Apply migrations:  
`python manage.py migrate`

6.2 Run the server:
`python manage.py runserver`

6.3 Open your browser and visit: http://127.0.0.1:8000/expensive/

# Testing the Redis Cache:

1. On the first request, you'll experience a 5-second delay as it simulates the expensive operation.

2. Subsequent requests (within 30 seconds) will be served instantly from Redis (source: "cache").

3. After 30 seconds, the cache expires, and the data will be recomputed.

# Common Issues & Troubleshooting:

1. Redis not running: Make sure you've started the Redis server by running redis-server in your terminal.

2. Connection errors: Double-check the LOCATION in settings.py. It should match your Redis server details.

3. Library versions: Ensure all required dependencies are installed and compatible (check with pip list).
