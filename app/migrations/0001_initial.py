# Generated by Django 5.0.1 on 2024-02-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Nom et Prenom')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Votre email')),
                ('phone', models.CharField(max_length=50, unique=True, verbose_name='Telephone')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('secteur', models.CharField(max_length=600, verbose_name='Secteur')),
                ('code', models.CharField(max_length=50, verbose_name='Code')),
                ('indicatif', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
