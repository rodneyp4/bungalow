from django.urls import path
from bungalow.listings import views

urlpatterns = [
    path('listings/', views.listings_list),
    path('listings/<int:pk>/', views.listings_detail),
]