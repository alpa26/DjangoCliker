from django.db import models
from django.contrib.auth.models import User
from copy import copy

# Create your models here.
class Core(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    level = models.IntegerField(default=1)

    def click(self):
        self.coins += self.click_power

        if self.coins >= self.check_level_price(): # Проверка на достаточное количество монет 
            self.level += 1                        # для создания буста
   
            return True # Труе если буст создался
        return False # Фалсе если буст не создался
   
    def check_level_price(self): # Функция вычисления количества монет для повышения уровня
        return (self.level**2)*10*(self.level)


class Boost(models.Model):
    core = models.ForeignKey(Core, null=False, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    price = models.IntegerField(default=10)
    power = models.IntegerField(default=1)
    def levelup(self):
        if self.price > self.core.coins: # Если монет недостаточно, ничего не делаем 
            return False

        old_boost_stats = copy(self) # Сохраняем старые значения буста, чтобы потом вернуть их на фронт

        # Меняем параметры ядра
        self.core.coins -= self.price
        self.core.click_power += self.power
        self.core.save()

        # Меняем параметры буста
        self.level += 1
        self.power *= 2
        self.price *= 10
        self.save()

        return old_boost_stats, self