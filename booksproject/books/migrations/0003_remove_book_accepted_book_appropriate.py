# Generated by Django 4.0.4 on 2022-04-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='accepted',
        ),
        migrations.AddField(
            model_name='book',
            name='appropriate',
            field=models.CharField(choices=[('un', 'Under 18'), ('bt', 'Between 8-15'), ('ad', 'Adults')], default='bt', max_length=250),
        ),
    ]
