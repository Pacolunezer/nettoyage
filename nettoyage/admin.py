from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CleaningService, Booking, Feedback

# Configuration de l'administration pour le modèle CleaningService
@admin.register(CleaningService)
class CleaningServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'image')  # Affiche ces champs dans la liste
    search_fields = ('name', 'service_type')  # Permet de rechercher par nom et type de service
    list_filter = ('service_type',)  # Ajoute un filtre par type de service

# Configuration de l'administration pour le modèle Booking
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service',  'prenom', 'nom', 'email', 'telephone')  # Affiche ces champs dans la liste
    search_fields = ('user__username', 'service__name')  # Permet de rechercher par utilisateur ou service
      # Filtre par statut et date de réservation
    # Ajoute une hiérarchie de dates pour naviguer par date

# Configuration de l'administration pour le modèle Feedback
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating', 'comment')  # Affiche la réservation, la note et le commentaire
    search_fields = ('booking__user__username', 'booking__service__name')  # Recherche par utilisateur ou service
    list_filter = ('rating',)  # Filtre par note
