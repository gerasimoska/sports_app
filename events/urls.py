from django.urls import path
from .views import (
    TrainingListCreateView,
    TrainingGetDeleteView,
    MealListCreateView,
    MealGetDeleteView,
    EventsFilterView,
)

urlpatterns = [
    path(
        "trainings/",
        TrainingListCreateView.as_view(),
        name="trainings-list",
    ),
    path(
        "trainings/<int:training_id>",
        TrainingGetDeleteView.as_view(),
        name="training-details",
    ),
    path(
        "meals/",
        MealListCreateView.as_view(),
        name="meals-list",
    ),
    path(
        "meals/<int:meal_id>",
        MealGetDeleteView.as_view(),
        name="meal-details",
    ),
    path(
        "",
        EventsFilterView.as_view(),
        name="events-filter",
    ),
]
