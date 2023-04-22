from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    telephone = models.IntegerField()
    description_commande = models.TextField()
    

    class Meta:
        verbose_name = ("Commande")
        verbose_name_plural = ("Commandes")

    def __str__(self):
        return self.name
