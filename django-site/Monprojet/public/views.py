from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.db.models import Sum  # Pour calculer la somme des montants
from .forms import ExpenseForm
from api.models import Expense

# Vue pour ajouter une dépense
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            # Supprimer la référence à l'utilisateur, car il n'y a plus d'authentification
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

# Vue pour afficher la liste des dépenses
def expense_list(request):
    # Récupérer les dépenses via l'API ou localement
    response = requests.get('http://127.0.0.1:8000/api/expenses/')
    if response.status_code == 200:
        expenses = response.json()
        # Calculer la somme totale depuis l'API (si l'API retourne une liste de dicts)
        total_amount = sum(float(expense['amount']) for expense in expenses)
    else:
        expenses = Expense.objects.all()  # Récupérer toutes les dépenses sans filtrer par utilisateur
        # Calculer la somme totale des montants depuis la base de données
        total_amount = expenses.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'expense_list.html', {'expenses': expenses, 'total_amount': total_amount})

# Vue pour modifier une dépense
def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)  # Récupérer la dépense sans vérifier l'utilisateur
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # Rediriger vers la liste des dépenses après la modification
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form})

# Vue pour supprimer une dépense
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)  # Récupérer la dépense sans vérifier l'utilisateur
    if request.method == 'POST':
        expense.delete()  # Supprimer la dépense
        return redirect('expense_list')  # Rediriger vers la liste des dépenses après suppression
    return render(request, 'confirm_delete.html', {'expense': expense})

# Vue pour afficher les statistiques des dépenses
def expense_statistics(request):
    # Implémentez ici la logique pour calculer et afficher les statistiques via l'API ou la base de données
    pass
