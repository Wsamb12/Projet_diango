from django.shortcuts import render
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Monprojet.settings')

# Create your views here.
from rest_framework import viewsets
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


