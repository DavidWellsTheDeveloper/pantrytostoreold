from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.

class Recipe(models.Model):
  recipe_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=300)
  summary = models.CharField(max_length=2000, null=True, blank=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.title}"

class Ingredient(models.Model):
  ingredient_id = models.AutoField(primary_key=True)
  recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
  name = models.CharField(max_length=500)
  amount = models.FloatField(null=True, blank=True)
  unit = models.CharField(max_length=100, null=True, blank=True)
  def __str__(self):
    return f"{self.amount} {self.unit}   {self.name}"

class Instruction(models.Model):
  instruction_id = models.AutoField(primary_key=True)
  recipe = models.ForeignKey(Recipe, related_name='instructions', on_delete=models.CASCADE)
  step = models.IntegerField()
  instruction = models.CharField(max_length=2000)
  def __str__(self):
    return f"{self.instruction}"

class GroceryListItem(models.Model):
  ingredient_id = models.IntegerField(null=True)
  amount = models.FloatField(null=True)
  unit = models.CharField(max_length=50, null=True, blank=True)
  description = models.CharField(max_length=100, default="")
  completed = models.BooleanField(default=False)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return f"{ammount} {unit} of {self.ingredient_id}"