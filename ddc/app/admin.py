from django.contrib import admin

# Register your models here.
from django.contrib import admin

from app.models import Dog, Breed, BreedType


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    fields = ('name', 'age', 'breed')
    list_display = ('name', 'age', 'breed')
    search_fields = ('name', 'age', 'breed')


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    fields = ('name', 'breed_type')
    list_display = ('name', 'breed_type')
    search_fields = ('name', 'breed_type')


@admin.register(BreedType)
class BreedTypeAdmin(admin.ModelAdmin):
    fields = ('breed_type',)
    list_display = ('breed_type',)
    search_fields = ('breed_type',)