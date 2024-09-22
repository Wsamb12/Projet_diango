from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_expense, name='add_expense'),  # Ajouter une dépense
    path('edit/<int:id>/', views.edit_expense, name='edit_expense'),  # Modifier une dépense
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),  # Supprimer une dépense
    path('statistics/', views.expense_statistics, name='expense_statistics'),  # Statistiques des dépenses
]
