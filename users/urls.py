<<<<<<< HEAD
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/Userlogin.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/Userlogout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
=======
from django.urls import path, include
from .views import SignUpView, UserUpdateView, UserPasswordChangeView, UserPasswordResetView
from django.contrib.auth import views # new

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('change_password/', UserPasswordChangeView.as_view(), name='change_password'),
    path('reset_password/', UserPasswordResetView.as_view(), name='reset_password'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update_user'),
>>>>>>> dd8e683bf902422332c15d70d55d3d53b3553e2d
]
