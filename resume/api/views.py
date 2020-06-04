from rest_framework import generics, permissions
from rest_framework.response import Response
from ..models import Experience
from .serializers import ExperienceSerializer
from .permissions import IsOwnerOrNoAccess


class ExperienceList(generics.ListCreateAPIView):
   queryset = Experience.objects.all()
   serializer_class = ExperienceSerializer


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Experience.objects.all()
   serializer_class = ExperienceSerializer