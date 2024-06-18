"""Views for the frontend"""

from django.shortcuts import render


# Create your views here.
def index(request):
    """Render request"""
    return render(request, "frontend/index.html")
