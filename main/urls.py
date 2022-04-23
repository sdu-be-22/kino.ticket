
from django.urls import path
from.import views
urlpatterns = [
    path('',views.glav, name='home'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('movie/<int:movie_id>', views.movie_view, name='movie_detail'),
]