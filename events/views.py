from django.shortcuts import render
from django.views.generic import View
from .models import Training, Meal
from .serializers import EventSerilizer, TrainingSerilizer, MealSerilizer
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
import datetime
from itertools import chain


class TrainingListCreateView(APIView):
    model = Training

    def get(self, request):
        trainings = Training.objects.all()
        serializer = TrainingSerilizer(trainings, many=True)
        print(type(serializer.data))
        print(serializer.data)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request):
        serializer = TrainingSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        trainings = Training.objects.all()
        serializer = TrainingSerilizer(trainings, many=True)
        return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)


class TrainingGetDeleteView(APIView):
    model = Training

    def get(self, request, training_id):
        print("point2")
        training = Training.objects.get(pk=training_id)
        serializer = TrainingSerilizer(training)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def delete(self, request, training_id):
        training = Training.objects.get(pk=training_id)
        training.delete()

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, training_id):
        training = Training.objects.get(pk=training_id)
        serializer = TrainingSerilizer(training, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        training = Training.objects.get(pk=training_id)
        serializer = TrainingSerilizer(training)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


class MealListCreateView(APIView):
    model = Meal

    def get(self, request):
        meals = Meal.objects.all()
        serializer = MealSerilizer(meals, many=True)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request):
        serializer = MealSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        meals = Meal.objects.all()
        serializer = MealSerilizer(meals, many=True)

        return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED, safe=False)


class MealGetDeleteView(APIView):
    model = Meal

    def get(self, request, meal_id):
        meal = Meal.objects.get(pk=meal_id)
        serializer = MealSerilizer(meal)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    def delete(self, request, meal_id):
        meal = Meal.objects.get(pk=meal_id)
        meal.delete()

        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, meal_id):
        meal = Meal.objects.get(pk=meal_id)
        serializer = MealSerilizer(meal, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        meal = Meal.objects.get(pk=meal_id)
        serializer = MealSerilizer(meal)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


class EventsFilterView(APIView):
    def get(self, request):
        start = self.request.GET.get("start", None)
        end = self.request.GET.get("end", None)

        trainings = Training.objects.filter(start=start, end=end)
        meals = Meal.objects.filter(start=start, end=end)
        events = list(chain(trainings, meals))

        return HttpResponse(events, status=status.HTTP_200_OK)
