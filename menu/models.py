from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('main_course', 'Main Course'),
        ('salad', 'Salad'),
        ('soup', 'Soup'),
        ('dessert', 'Dessert'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')  # Will use Cloudinary
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='main_course')  # Add this field

    def __str__(self):
        return self.name
