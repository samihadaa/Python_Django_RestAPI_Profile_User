from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewset,'hello-viewset')
router.register('profiles',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)
urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
