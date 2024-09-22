from django.contrib import admin
from django.urls import path, include
from public import views as public_views

urlpatterns = [
    path('',public_views.expense_list, name='expense_list'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Inclure les routes de l'application API
    path('public/', include('public.urls')),  # Inclure les routes de l'application publique
    path('accounts/', include('django.contrib.auth.urls')),

]
