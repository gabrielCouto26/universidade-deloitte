from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend.views.home import HomeView
from backend.views.student import StudentList, StudentDetail, StudentGradeList
from backend.views.teacher import TeacherList, TeacherDetail, TeacherGradeList
from backend.views.discipline import DisciplineList, DisciplineDetail
from backend.views.grade import GradeList, GradeDetail


urlpatterns = [
    path('home', HomeView.as_view(), name='home'),

    path('students/', StudentList.as_view(), name='students'),
    path('students/<int:pk>', StudentDetail.as_view(), name='student'),
    path('students/grades', StudentGradeList.as_view(), name='student-grades'),

    path('teachers/', TeacherList.as_view(), name='teachers'),
    path('teachers/<int:pk>', TeacherDetail.as_view(), name='teacher'),
    path('teachers/grades', TeacherGradeList.as_view(), name='teacher-grades'),

    path('disciplines/', DisciplineList.as_view(), name='disciplines'),
    path('disciplines/<int:pk>', DisciplineDetail.as_view(), name='discipline'),

    path('grades/', GradeList.as_view(), name='grades'),
    path('grades/<int:pk>', GradeDetail.as_view(), name='grade'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
