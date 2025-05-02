from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Deck, Flashcard
from django.views.decorators.http import require_POST

# Template Views
def home(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/home.html', {'decks': decks})

def deck_detail(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    return render(request, 'flashcards/deck_detail.html', {'deck': deck})

def study_mode(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    flashcards = deck.flashcards.all()
    return render(request, 'flashcards/study_mode.html', {'deck': deck, 'flashcards': flashcards})

def about(request):
    return render(request, 'flashcards/about.html')

# API Views
@require_POST
def api_create_deck(request):
    name = request.POST.get('name')
    if not name:
        return JsonResponse({'error': 'Deck name is required'}, status=400)
    deck = Deck.objects.create(name=name)
    return JsonResponse({'id': deck.id, 'name': deck.name, 'flashcard_count': 0})

@require_POST
def api_delete_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    deck.delete()
    return JsonResponse({'message': 'Deck deleted successfully'})

@require_POST
def api_create_flashcard(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    front = request.POST.get('front')
    back = request.POST.get('back')
    if not (front and back):
        return JsonResponse({'error': 'Both front and back are required'}, status=400)
    flashcard = Flashcard.objects.create(deck=deck, front=front, back=back)
    return JsonResponse({'id': flashcard.id, 'front': flashcard.front, 'back': flashcard.back})

@require_POST
def api_update_flashcard(request, deck_id, card_id):
    flashcard = get_object_or_404(Flashcard, id=card_id, deck_id=deck_id)
    front = request.POST.get('front')
    back = request.POST.get('back')
    if not (front and back):
        return JsonResponse({'error': 'Both front and back are required'}, status=400)
    flashcard.front = front
    flashcard.back = back
    flashcard.save()
    return JsonResponse({'id': flashcard.id, 'front': flashcard.front, 'back': flashcard.back})

@require_POST
def api_delete_flashcard(request, deck_id, card_id):
    flashcard = get_object_or_404(Flashcard, id=card_id, deck_id=deck_id)
    flashcard.delete()
    return JsonResponse({'message': 'Flashcard deleted successfully'})