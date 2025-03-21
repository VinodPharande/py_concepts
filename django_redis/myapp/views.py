from django.shortcuts import render

""""added by me"""
# Create your views here.
print("Hello from views.py")
from django.core.cache import cache
print("Hello from views.py 1")
# from django.core.cache import caches
from django.http import JsonResponse
print("Hello from views.py 2")
import time

def expensive_operation_view(request):
    print("Hello from expensive_operation_view")
    cache_key = "expensive_data"  # Unique key for this cache
    cached_data = cache.get(cache_key)  # Check if data exists in Redis

    if cached_data:
        print("Cache hit!")
        return JsonResponse({"data": cached_data, "source": "cache"})

    # Simulate an expensive operation (e.g., database query)
    time.sleep(10 )  # Simulating delay
    expensive_data = {"message": "Result of an expensive computation"}

    # Store the data in Redis with a TTL (e.g., 30 seconds)
    cache.set(cache_key, expensive_data, timeout=30)

    return JsonResponse({"data": expensive_data, "source": "server"})


# def cache_backend_info(request):
#     cache_backend = caches['default'].__class__.__name__
#     return JsonResponse({"active_cache_backend": cache_backend})