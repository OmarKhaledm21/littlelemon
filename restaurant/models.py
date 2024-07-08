from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )

    def __str__(self):
        return self.title


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators=[MaxValueValidator(999999)]
    )
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
