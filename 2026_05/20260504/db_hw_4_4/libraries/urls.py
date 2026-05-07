from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
    path('<int:book_pk>/create/', views.create, name='create'),
    path('<int:book_pk>/delete/<int:review_pk>/', views.delete, name='delete'),
]

