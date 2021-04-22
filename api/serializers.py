# api/serializers.py
from rest_framework import serializers
from polls.models import Polls

class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = ['question', 'option_one', 'option_two', 'option_three']