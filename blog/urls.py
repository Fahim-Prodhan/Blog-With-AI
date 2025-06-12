from django.urls import path,include
from blog.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogs',BlogViewSets)

urlpatterns = [
    path('', include(router.urls))
]
