from django.urls import path

from authentication import views

urlpatterns = [
    path('all/', views.viewAllUser),
    path('register/', views.registerUser),
    path('login/', views.loginUser),
    path('otpcode/', views.verifyOTPCode)
]
