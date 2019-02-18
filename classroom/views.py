from django.shortcuts import render
import requests

def students_with_js(request):
    context = { 'nbar': 'with_js' }
    return render(request, "students_with_js.html", context) 

def students_without_js(request):
    response = requests.get('http://localhost:5000/api/v1/students/')
    students = response.json()
    context = { 'students': students, 'nbar': 'without_js' }
    return render(request, 'students_without_js.html', context)
