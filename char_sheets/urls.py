# your_app/urls.py
from django.urls import path
from .views import CharacterSheetListView,SpellListView, ItemListView, SpellCreateView, ItemCreateView,CharacterSheetCreateView,CharacterSheetDetailView

urlpatterns = [
    path('spells/', SpellListView.as_view(), name='spell-list'),
    path('spells/create/', SpellCreateView.as_view(), name='spell-create'),


    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/create/', ItemCreateView.as_view(), name='item-create'),

    path('character_sheet/new/', CharacterSheetCreateView.as_view(), name='character_sheet_create'),
    path('character_sheet/<int:pk>/', CharacterSheetDetailView.as_view(), name='character_sheet_detail'),
    path('character_sheet/', CharacterSheetListView.as_view(), name='character_sheet_list'),


]
