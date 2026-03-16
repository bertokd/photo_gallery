from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.photo_list, name="list"),
    path('<slug:slug>', views.photo_page, name="page"),
    path('new-photo/', views.new_photo, name='new'),
    path('<slug:slug>/delete/', views.photo_delete, name='delete'),
]