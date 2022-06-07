from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Core(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    level = models.IntegerField(default=0) # От уровня зависит количество бустов

    def click(self):
        self.coins += self.click_power

        if self.coins >= self.check_level_price(): # Проверка на достаточное количество монет 
            self.level += 1                        # для создания буста
   
            return True # Труе если буст создался
        return False # Фалсе если буст не создался
   
    def check_level_price(self): # Функция вычисления количества монет для повышения уровня
        return (self.level**2+1)*100*(self.level+1) 


class Boost(models.Model):
    core = models.ForeignKey(Core, null=False, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    price = models.IntegerField(default=10)
    power = models.IntegerField(default=1)