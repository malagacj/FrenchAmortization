from django.contrib import admin
from django.urls import path
from .views import SimulationListView


urlpatterns = [
    path('admin/', admin.site.urls),
]
