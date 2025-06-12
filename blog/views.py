from django.shortcuts import render
from rest_framework import viewsets
from blog.models import *
from blog.serializers import *

# Create your views here.
class BlogViewSets(viewsets.ModelViewSet):
    queryset=Blog.objects.all().order_by('-created_at')
    serializer_class=BlogSerializer
    
