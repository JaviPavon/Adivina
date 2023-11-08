from django.db import models

import random

class Adivina(models.Model):

    numero = random.randint(0, 100)


    def __str__(self):

        return self.numero