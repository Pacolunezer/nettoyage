from django.urls import path
from .views import HomeView, BookingView, UserBookingsView, FeedbackView, BookingSuccessView, Encombrement
from .views import PrestationListView
urlpatterns = [
    # Page d'accueil qui affiche les services de nettoyage
    path('', HomeView.as_view(), name='home'),

    # Page pour réserver un service de nettoyage
    path('booking/<int:service_id>/', BookingView.as_view(), name='booking'),

    # Page pour voir les réservations de l'utilisateur
    path('my-bookings/', UserBookingsView.as_view(), name='user_bookings'),

    # Page pour laisser un feedback après un service complété
    path('feedback/<int:booking_id>/', FeedbackView.as_view(), name='feedback'),
    path('booking/success/<int:service_id>', BookingSuccessView.as_view(), name='booking_success'),
    path('encombrement', Encombrement, name='encombrement'),
    path('prestations/', PrestationListView.as_view(), name='prestations'),
]
