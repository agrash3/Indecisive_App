# api/views.py
from rest_framework import generics
from polls.models import Polls
from .serializers import PollsSerializer

class PollsList(generics.ListCreateAPIView):
    queryset = Polls.objects.all()
    serializer_class = PollsSerializer

class PollsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polls.objects.all()
    serializer_class = PollsSerializer
