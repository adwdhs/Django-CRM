from django.urls import path
from . import views
from .views import LoginView, RegisterView, AddNewView


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('detail/<str:pk>', views.detail, name='detail'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('new', AddNewView.as_view(), name='addnew'),

]


