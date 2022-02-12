from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API View Set uses the DefaultRouter
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

# APIView uses urlpatterns to route HTTP methods
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path('', include(router.urls)), # for API View Set
]
