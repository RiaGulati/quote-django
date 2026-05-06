from django.urls import path
from . import views

urlpatterns = [
    path('quote/', views.random_quote_api),
    path('quotes/', views.quotes_api),
    path('quotes/<int:id>/', views.quote_detail_api),
]