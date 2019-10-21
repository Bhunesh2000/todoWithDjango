from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo                     

class TodoView(viewsets.ModelViewSet):       
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

def index(request):
    return render(request, 'index.html')

def viewshower(request):
	return render(request, 'index.html')    