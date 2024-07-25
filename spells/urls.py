from django.urls import path
from .views import SpellListView, SpellCreateView, SpellUpdateView, SpellDeleteView

app_name = 'spells'

urlpatterns = [
    path('list/', SpellListView.as_view(), name='spell_list'),
    path('create/', SpellCreateView.as_view(), name='spell_create'),
    path('<int:pk>/update/', SpellUpdateView.as_view(), name='spell_update'),
    path('<int:pk>/delete/', SpellDeleteView.as_view(), name='spell_delete'),
]
