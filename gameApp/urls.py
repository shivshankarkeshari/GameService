


from django.urls import path

from .views import SpecificGameDetailsView, GamesDetailsView

urlpatterns = [
    path('game_details/', GamesDetailsView.as_view()),
    path('game_details/<int:id>/', SpecificGameDetailsView.as_view()),
]