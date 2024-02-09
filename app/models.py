from django.db import models

# Create your models here.




class User(models.Model):

    name = models.CharField('Nom et Prenom', max_length=75)
    email = models.EmailField('Votre email', max_length=254)
    phone = models.CharField('Telephone', max_length=50)
    date = models.DateTimeField('Date', auto_now_add=True)
    secteur =  models.CharField('Secteur', max_length=50)
    code = models.CharField('Code', max_length=50)
    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.name


