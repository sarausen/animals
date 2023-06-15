from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from . import views

router = routers.DefaultRouter()
router.register(r'animals', views.AnimalViewSet)
router.register(r'volunteer', views.VolunteerViewSet)
router.register(r'image', views.AnimalImageViewSet)


urlpatterns = [

    path('', include(router.urls)),
    path('auth_token/', auth_views.obtain_auth_token),
    path('auth/', include('rest_framework.urls')),

    path('dog/', views.DogViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('dog/<int:pk>', views.DogViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),

    path('cat/', views.CatViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('cat/<int:pk>', views.CatViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),

]

