from django.db.models.query import QuerySet
from django.shortcuts import render
from . models import Employee
from . serializers import EmployeeSerializer
from rest_framework import viewsets

# Create your views here.
# Create your views here.

class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
