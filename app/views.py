from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from .permissions import IsAuthenticatedOrSafeMethods

from .models import Animal
from .serializers import *


class AnimalViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]


class DogViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.filter(species='dog')
    serializer_class = DogSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]

    def perform_create(self, serializer):
        serializer.save(species='dog')


class CatViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.filter(species='cat')
    serializer_class = CatSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]

    def perform_create(self, serializer):
        serializer.save(species='cat')


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]


class AnimalImageViewSet(viewsets.ModelViewSet):
    queryset = AnimalImage.objects.all()
    serializer_class = AnimalImageSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrSafeMethods, ]

