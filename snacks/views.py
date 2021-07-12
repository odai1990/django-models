from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from .models import Snack
# Create your views here.
class SnacksList(ListView):
    template_name='snack_list.html'
    model =Snack

class SnacksDetials(DetailView):
    template_name='snack_detail.html'
    model =Snack