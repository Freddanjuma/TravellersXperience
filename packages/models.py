from django.db import models

class Package(models.Model):
    destination = models.ForeignKey(
        'destinations.Destination',
        on_delete=models.CASCADE,
        related_name='destination_packages'
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")
    image = models.ImageField(upload_to='packages/')

    def __str__(self):
        return f"{self.name} - {self.destination.name}"
