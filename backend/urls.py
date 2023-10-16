from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),

    path('students/', views.StudentList.as_view(), name='students'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='student'),
    path('students/grades', views.StudentGradeList.as_view(), name='student-grades'),

    path('teachers/', views.TeacherList.as_view(), name='teachers'),
    path('teachers/<int:pk>', views.TeacherDetail.as_view(), name='teacher'),
    path('teachers/grades', views.TeacherGradeList.as_view(), name='teacher-grades'),

    path('disciplines/', views.DisciplineList.as_view(), name='disciplines'),
    path('disciplines/<int:pk>', views.DisciplineDetail.as_view(), name='discipline'),

    path('grades/', views.GradeList.as_view(), name='grades'),
    path('grades/<int:pk>', views.GradeDetail.as_view(), name='grade'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
