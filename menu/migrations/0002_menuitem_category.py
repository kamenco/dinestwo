# Generated by Django 5.1.2 on 2024-10-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('main_course', 'Main Course'), ('salad', 'Salad'), ('soup', 'Soup'), ('dessert', 'Dessert')], default='main_course', max_length=50),
        ),
    ]
