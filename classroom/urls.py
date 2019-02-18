from django.urls import path
from .views import students_with_js, students_without_js

urlpatterns = [
    path('students-with-js/', students_with_js, name="students_with_js"),
    path('students-without-js/', students_without_js, name="students_without_js")
]