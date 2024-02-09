from django.db import models
from django import forms
# Create your models here.




class User(models.Model):

    name = models.CharField('Nom et Prenom', max_length=75)
    email = models.EmailField('Votre email', max_length=254, null=True, blank=True)
    phone = models.CharField('Telephone', max_length=50, unique=True)
    date = models.DateTimeField('Date', auto_now_add=True)
    secteur =  models.CharField('Secteur', max_length=600)
    code = models.CharField('Code', max_length=50)
    indicatif = models.CharField(max_length=50)
    message = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.name





class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'secteur', 'code', 'indicatif', 'message']
        help_texts = {
            'name': 'Entrez votre nom et prénom.',
            'email': 'Entrez votre adresse email.',
            'phone': 'Ce numero est deja enregistrer',
            'secteur': 'Sélectionnez votre secteur d\'activité.',
            'code': 'Entrez votre code.',
            'indicatif': 'Entrez votre indicatif.',
            'message': 'Laissez un message optionnel.'
        }
        error_messages = {
            'name': {
                'required': "Ce champ est requis.",
            },
            'email': {
                'required': "Ce champ est requis.",
                'invalid': "Veuillez entrer une adresse email valide."
            },
            'phone': {
                'required': "Ce champ est requis.",
                'unique': "Ce numéro de téléphone est déjà utilisé."
            },
            }