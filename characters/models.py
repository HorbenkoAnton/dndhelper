from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
stat_validator = [MinValueValidator(6),MaxValueValidator(20)]

class BasicInfo(models.Model):
    CLASS_CHOICES = [
        ('barbarian', 'Barbarian'),
        ('bard', 'Bard'),
        ('cleric', 'Cleric'),
        ('druid', 'Druid'),
        ('fighter', 'Fighter'),
        ('monk', 'Monk'),
        ('paladin', 'Paladin'),
        ('ranger', 'Ranger'),
        ('rogue', 'Rogue'),
        ('sorcerer', 'Sorcerer'),
        ('warlock', 'Warlock'),
        ('wizard', 'Wizard'),
    ]
    RACE_CHOICES = [
        ('human', 'Human'),
        ('elf', 'Elf'),
        ('dwarf', 'Dwarf'),
        ('halfling', 'Halfling'),
        ('gnome', 'Gnome'),
        ('half_orc', 'Half-Orc'),
        ('half_elf', 'Half-Elf'),
        ('dragonborn', 'Dragonborn'),
        ('tiefling', 'Tiefling'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='character_sheets')
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=20, choices=RACE_CHOICES)
    class_type = models.CharField(max_length=20, choices=CLASS_CHOICES)
    level = models.PositiveIntegerField(default=1)

class Stats(models.Model):
    strength = models.PositiveIntegerField(validators=stat_validator, default=6)
    dexterity = models.PositiveIntegerField(validators=stat_validator, default=6)
    constitution = models.PositiveIntegerField(validators=stat_validator, default=6)
    intelligence = models.PositiveIntegerField(validators=stat_validator, default=6)
    wisdom = models.PositiveIntegerField(validators=stat_validator, default=6)
    charisma = models.PositiveIntegerField(validators=stat_validator, default=6)


class CharacterSheet(models.Model):
    basic_info = models.OneToOneField(BasicInfo, on_delete=models.CASCADE)
    stats = models.OneToOneField(Stats,on_delete=models.CASCADE)
