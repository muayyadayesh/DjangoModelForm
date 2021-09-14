from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
   path('user_login/', views.user_login, name='user_login'),
   path('registration/', views.registration, name='registration'),
   path('logout/', views.user_logout, name='logout'),
   path('special/', views.special, name='special'),
]
