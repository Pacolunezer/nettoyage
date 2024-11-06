from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from .models import CleaningService, Booking, Feedback
from .forms import BookingForm

# Vue pour la page d'accueil
class HomeView(View):
    def get(self, request):
        services = CleaningService.objects.all()
        return render(request, 'home.html', {'services': services})
    
def Encombrement(request):
    return render(request, 'encombrement.html')
from django.views.generic import ListView
class PrestationListView(ListView):
    model = CleaningService
    template_name = 'prestations.html'  # Le nom de votre template pour les prestations
    context_object_name = 'services'    # Le nom utilisé dans le template pour les données

    # Optionnel : pour personnaliser l'ordre d'affichage ou ajouter des filtres
    def get_queryset(self):
        return CleaningService.objects.all() 
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
@method_decorator(login_required, name='dispatch')
class BookingView(View):
    def get(self, request, service_id):
        service = get_object_or_404(CleaningService, id=service_id)
        form = BookingForm()
        return render(request, 'booking.html', {'service': service, 'form': form})

    def post(self, request, service_id):
        service = get_object_or_404(CleaningService, id=service_id)
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associe l'utilisateur connecté
            booking.service = service
            booking.save()
            return redirect('booking_success', service_id=service.id)

        return render(request, 'booking.html', {'service': service, 'form': form})
class BookingSuccessView(View):
    def get(self, request, service_id):
        service = get_object_or_404(CleaningService, id=service_id)
        form = BookingForm()
        return render(request, 'booking_success.html', {'form': form, 'service': service})

    def post(self, request, service_id):
        service = get_object_or_404(CleaningService, id=service_id)
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assurez-vous que l'utilisateur est connecté
            booking.service = service
            booking.save()
            return redirect('booking_success')  # Redirection vers la page de succès

        return render(request, 'booking_template.html', {'form': form, 'service': service})
# Vue pour afficher les réservations de l'utilisateur
class UserBookingsView(View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'user_bookings.html', {'bookings': bookings})

# Vue pour gérer le feedback des clients
class FeedbackView(View):
    def get(self, request, booking_id):
        booking = Booking.objects.get(id=booking_id)
        return render(request, 'feedback.html', {'booking': booking})

    def post(self, request, booking_id):
        booking = Booking.objects.get(id=booking_id)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Feedback.objects.create(booking=booking, rating=rating, comment=comment)
        return redirect('feedback_success')
