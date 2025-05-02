from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('decks/<int:deck_id>/', views.deck_detail, name='deck_detail'),
    path('decks/<int:deck_id>/study/', views.study_mode, name='study_mode'),
    path('about/', views.about, name='about'),
    # API Endpoints
    path('api/decks/create/', views.api_create_deck, name='api_create_deck'),
    path('api/decks/<int:deck_id>/delete/', views.api_delete_deck, name='api_delete_deck'),
    path('api/decks/<int:deck_id>/flashcards/create/', views.api_create_flashcard, name='api_create_flashcard'),
    path('api/decks/<int:deck_id>/flashcards/<int:card_id>/update/', views.api_update_flashcard, name='api_update_flashcard'),
    path('api/decks/<int:deck_id>/flashcards/<int:card_id>/delete/', views.api_delete_flashcard, name='api_delete_flashcard'),
]