from django.urls import path,include
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
#router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]