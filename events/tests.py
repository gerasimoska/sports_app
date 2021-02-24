from django.test import TestCase
from django.urls import reverse
from .models import Training, Meal


class TrainingTestCase(TestCase):
    def setUp(self):
        Training.objects.create(title="squats", description="core strength")
        Training.objects.create(title="deadlift", description="core stability")

    def test_get_treainings(self):
        squats = Training.objects.get(title="squats")
        deadlift = Training.objects.get(title="deadlift")
        self.assertEqual(squats.description, "core strength")
        self.assertEqual(deadlift.description, "core stability")


class MealTestCase(TestCase):
    def setUp(self):
        Meal.objects.create(title="breakfast", description="morning meal")
        Meal.objects.create(title="lunch", description="afternoon meal")

    def test_get_meals(self):
        breakfast = Meal.objects.get(title="breakfast")
        lunch = Meal.objects.get(title="lunch")
        self.assertEqual(breakfast.description, "morning meal")
        self.assertEqual(lunch.description, "afternoon meal")
