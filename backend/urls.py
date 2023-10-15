from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>', views.StudentDetail.as_view()),

    path('teachers/', views.TeacherList.as_view()),
    path('teachers/<int:pk>', views.TeacherDetail.as_view()),

    path('disciplines/', views.DisciplineList.as_view()),
    path('disciplines/<int:pk>', views.DisciplineDetail.as_view()),

    path('grades/', views.GradeList.as_view()),
    path('grades/<int:pk>', views.GradeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
