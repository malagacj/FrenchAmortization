from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Simulation


class SimulationListView(ListView):
    model = Simulation


class SimulationDetailView(DetailView):
    model = Simulation
