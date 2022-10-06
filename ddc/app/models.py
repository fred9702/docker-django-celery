from django.db import models


class BreedType(models.Model):

    def __str__(self):
        return self.breed_type

    breed_type = models.CharField(max_length=100, blank=True)


class Breed(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True, default='')
    breed_type = models.ForeignKey(BreedType, null=True, blank=True, on_delete=models.CASCADE)


class Dog(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, blank=True, default='')
    age = models.IntegerField(null=True)
    breed = models.ForeignKey(Breed, null=True, blank=True, on_delete=models.CASCADE)
