from rest_framework import serializers
from .models import (CommonInfo, Training, Meal)


class EventSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CommonInfo
        fields = ("id", "start", "end", "title", "description")


class TrainingSerilizer(EventSerilizer):
    class Meta:
        model = Training
        fields = EventSerilizer.Meta.fields


class MealSerilizer(EventSerilizer):
    class Meta:
        model = Meal
        fields = EventSerilizer.Meta.fields
