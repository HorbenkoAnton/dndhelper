from django.urls import path
from .views import (
    CharacterSheetCreateView, CharacterSheetListView,
    CharacterSheetUpdateView, CharacterSheetDeleteView,CharacterSheetDetailView
)

app_name = 'characters'

urlpatterns = [
    # CharacterSheet URLs
    path('create/', CharacterSheetCreateView.as_view(), name='character_sheet_create'),
    path('', CharacterSheetListView.as_view(), name='character_sheet_list'),
    path('<int:pk>/', CharacterSheetDetailView.as_view(), name='character_sheet_detail'),
    path('<int:pk>/update/', CharacterSheetUpdateView.as_view(), name='character_sheet_update'),
    path('<int:pk>/delete/', CharacterSheetDeleteView.as_view(), name='character_sheet_delete'),
]