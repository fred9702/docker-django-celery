from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from app.views import DogViewSet


router = routers.DefaultRouter()
router.register(r'dog', DogViewSet, 'Dog')

app_name = 'ddc'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'app')))
]

