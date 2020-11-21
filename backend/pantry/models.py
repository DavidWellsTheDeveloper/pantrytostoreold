from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.

class SavedRecipes(models.Model):
  recipe_id = models.CharField(max_length=10)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  class Meta:
    constraints = [
      UniqueConstraint(fields=['recipe_id', 'user'], name='unique_saved')
    ]
  def __str__(self):
    return f"{self.recipe_id}"


class GroceryListItem(models.Model):
  ingredient_id = models.IntegerField()
  amount = models.FloatField()
  unit = models.CharField(max_length=50, null=True, blank=True)
  description = models.CharField(max_length=100, default="")
  completed = models.BooleanField(default=False)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return f"{ammount} {unit} of {self.ingredient_id}"