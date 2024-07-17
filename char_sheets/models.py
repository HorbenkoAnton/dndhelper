from django.db import models
from django.contrib.auth.models import User

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

class Spell(models.Model):
    LEVEL_CHOICES = [(i, str(i)) for i in range(10)]  
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.IntegerField(choices=LEVEL_CHOICES)

    def __str__(self):
        return self.name

class CharacterSheet(models.Model):
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
    ARMOR_CHOICES = [
        ('light', 'Light Armor'),
        ('medium', 'Medium Armor'),
        ('heavy', 'Heavy Armor'),
        ('shield', 'Shield'),
    ]
    WEAPON_CHOICES = [
        ('simple_melee', 'Simple Melee Weapons'),
        ('simple_ranged', 'Simple Ranged Weapons'),
        ('martial_melee', 'Martial Melee Weapons'),
        ('martial_ranged', 'Martial Ranged Weapons'),
    ]

    LANGUAGE_CHOICES = [
        ('common', 'Common'),
        ('dwarvish', 'Dwarvish'),
        ('elvish', 'Elvish'),
        ('giant', 'Giant'),
        ('gnomish', 'Gnomish'),
        ('goblin', 'Goblin'),
        ('halfling', 'Halfling'),
        ('orc', 'Orc'),
        ('abyssal', 'Abyssal'),
        ('celestial', 'Celestial'),
        ('draconic', 'Draconic'),
        ('deep_speech', 'Deep Speech'),
        ('infernal', 'Infernal'),
        ('primordial', 'Primordial'),
        ('sylvan', 'Sylvan'),
        ('undercommon', 'Undercommon'),
    ]
    TOOLS_CHOICES = [
        ('alchemist_supplies', 'Alchemist\'s Supplies'),
        ('brewer_supplies', 'Brewer\'s Supplies'),
        ('calligrapher_supplies', 'Calligrapher\'s Supplies'),
        ('carpenter_tools', 'Carpenter\'s Tools'),
        ('cartographer_tools', 'Cartographer\'s Tools'),
        ('cobbler_tools', 'Cobbler\'s Tools'),
        ('cook_utensils', 'Cook\'s Utensils'),
        ('glassblower_tools', 'Glassblower\'s Tools'),
        ('jeweler_tools', 'Jeweler\'s Tools'),
        ('leatherworker_tools', 'Leatherworker\'s Tools'),
        ('mason_tools', 'Mason\'s Tools'),
        ('painter_supplies', 'Painter\'s Supplies'),
        ('potter_tools', 'Potter\'s Tools'),
        ('smith_tools', 'Smith\'s Tools'),
        ('tinker_tools', 'Tinker\'s Tools'),
        ('weaver_tools', 'Weaver\'s Tools'),
        ('woodcarver_tools', 'Woodcarver\'s Tools'),
        ('disguise_kit', 'Disguise Kit'),
        ('forgery_kit', 'Forgery Kit'),
        ('herbalism_kit', 'Herbalism Kit'),
        ('navigator_tools', 'Navigator\'s Tools'),
        ('poisoner_kit', 'Poisoner\'s Kit'),
        ('thieves_tools', 'Thieves\' Tools'),
    ]

    #Basic info
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='character_sheets')
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=20, choices=RACE_CHOICES)
    class_type = models.CharField(max_length=20, choices=CLASS_CHOICES)
    level = models.PositiveIntegerField(default=1)

    #main stats
    strength = models.PositiveIntegerField()
    dexterity = models.PositiveIntegerField()
    constitution = models.PositiveIntegerField()
    intelligence = models.PositiveIntegerField()
    wisdom = models.PositiveIntegerField()
    charisma = models.PositiveIntegerField()

    #Stat bonuses
    strength_b = models.IntegerField()
    dexterity_b = models.IntegerField()
    constitution_b = models.IntegerField()
    intelligence_b = models.IntegerField()
    wisdom_b = models.IntegerField()
    charisma_b = models.IntegerField()

    #Living stats
    speed = models.PositiveIntegerField()
    max_hp = models.PositiveIntegerField()
    current_hp = models.PositiveIntegerField()
    temporary_hp = models.PositiveIntegerField(default=0)
    armor_class = models.PositiveIntegerField()

    #status
    condition = models.CharField(max_length=250, blank=True)
    defense_traits = models.CharField(max_length=250,blank=True)

    #bonuses
    proficiency_bonus = models.PositiveIntegerField()
    inspiration = models.BooleanField()
    initiative = models.PositiveIntegerField()

    #senses
    passive_reception = models.PositiveIntegerField()
    passive_investigation = models.PositiveIntegerField()
    passive_insight= models.PositiveIntegerField()

    #PROFICIENCIES & LANGUAGES
    armor = models.CharField(max_length=20, choices=ARMOR_CHOICES)
    weapon = models.CharField(max_length=20, choices=WEAPON_CHOICES)
    languages = models.JSONField(default=list)
    tools = models.CharField(max_length=50, choices=TOOLS_CHOICES)

    # Saving Throws with IntegerField and Boolean flag
    str_saving_throw = models.IntegerField(default=0)
    str_saving_throw_flag = models.BooleanField(default=False)
    
    dex_saving_throw = models.IntegerField(default=0)
    dex_saving_throw_flag = models.BooleanField(default=False)
    
    con_saving_throw = models.IntegerField(default=0)
    con_saving_throw_flag = models.BooleanField(default=False)
    
    int_saving_throw = models.IntegerField(default=0)
    int_saving_throw_flag = models.BooleanField(default=False)
    
    wis_saving_throw = models.IntegerField(default=0)
    wis_saving_throw_flag = models.BooleanField(default=False)
    
    cha_saving_throw = models.IntegerField(default=0)
    cha_saving_throw_flag = models.BooleanField(default=False)

 # Skills with IntegerField and Boolean flag
    acrobatics = models.IntegerField(default=0)
    acrobatics_flag = models.BooleanField(default=False)
    
    animal_handling = models.IntegerField(default=0)
    animal_handling_flag = models.BooleanField(default=False)
    
    arcana = models.IntegerField(default=0)
    arcana_flag = models.BooleanField(default=False)
    
    athletics = models.IntegerField(default=0)
    athletics_flag = models.BooleanField(default=False)
    
    deception = models.IntegerField(default=0)
    deception_flag = models.BooleanField(default=False)
    
    history = models.IntegerField(default=0)
    history_flag = models.BooleanField(default=False)
    
    insight = models.IntegerField(default=0)
    insight_flag = models.BooleanField(default=False)
    
    intimidation = models.IntegerField(default=0)
    intimidation_flag = models.BooleanField(default=False)
    
    investigation = models.IntegerField(default=0)
    investigation_flag = models.BooleanField(default=False)
    
    medicine = models.IntegerField(default=0)
    medicine_flag = models.BooleanField(default=False)
    
    nature = models.IntegerField(default=0)
    nature_flag = models.BooleanField(default=False)
    
    perception = models.IntegerField(default=0)
    perception_flag = models.BooleanField(default=False)
    
    performance = models.IntegerField(default=0)
    performance_flag = models.BooleanField(default=False)
    
    persuasion = models.IntegerField(default=0)
    persuasion_flag = models.BooleanField(default=False)
    
    religion = models.IntegerField(default=0)
    religion_flag = models.BooleanField(default=False)
    
    sleight_of_hand = models.IntegerField(default=0)
    sleight_of_hand_flag = models.BooleanField(default=False)
    
    stealth = models.IntegerField(default=0)
    stealth_flag = models.BooleanField(default=False)
    
    survival = models.IntegerField(default=0)
    survival_flag = models.BooleanField(default=False)

    #Inventory an spells
    items = models.ManyToManyField(Item, blank=True)
    spells = models.ManyToManyField(Spell, blank=True)

    #Charecter Info
    background = models.CharField(max_length=700,blank=True)
    appearance = models.CharField(max_length=250,blank=True)
    philosophy = models.CharField(max_length=100,blank=True)
    life_goals = models.CharField(max_length=50,blank=True)
    strengths = models.CharField(max_length=50,blank=True)
    flaws = models.CharField(max_length=50,blank=True)
    bonds = models.CharField(max_length=50,blank=True)
    distinguishing_features = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
    


