from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API View Set uses the DefaultRouter
router = DefaultRouter()
# /api/hello-viewset/
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
# /api/profile/ (GET, POST)
# /api/profile/:id (GET, POST, PUT, PATCH, DELETE)
router.register('profile', views.UserProfileViewSet) # basename not required when providing a queryset

# APIView uses urlpatterns to route HTTP methods
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-view'),
    path('', include(router.urls)), # for API View Set
]
