from django.urls import path

from api import views
urlpatterns = [
    path('all/', views.students),
    path('<int:student_id>/', views.student),
    path('create/', views.studentCreate),
    path('update/', views.studentupdate),
    path('delete/', views.delete)
]
