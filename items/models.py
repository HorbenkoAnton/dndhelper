from django.db import models

class Item(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('very_rare', 'Very Rare'),
        ('legendary','Legendary'),

    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)

    def __str__(self):
        return self.name