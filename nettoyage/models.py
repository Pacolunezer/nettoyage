from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Modèle pour les services de nettoyage
class CleaningService(models.Model):
    SERVICE_CHOICES = [
        ('hotel', 'Hotel'),
        ('creche', 'Crèche'),
        ('office', 'Bureau'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.name

# Modèle pour les réservations de services
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(CleaningService, on_delete=models.CASCADE)
    prenom= models.CharField(max_length=200)
    nom = models.CharField(max_length=100)
    telephone= models.CharField(max_length=13)
    email= models.EmailField()
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Booking by {self.user.username} for {self.service.name}"

# Modèle pour le feedback client
class Feedback(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"Feedback for {self.booking.service.name} by {self.booking.user.username}"
