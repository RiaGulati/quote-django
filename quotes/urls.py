from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.all_quotes, name='all_quotes'),
    path('api/', include('quotes.api_urls')),
]