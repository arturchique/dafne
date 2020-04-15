from django.shortcuts import render
from .models import Bag, Material, Size
from django.views import generic


def home(request):
    return render(
        request,
        'home.html',
        context={

        }
    )


def corp(request):
    return render(
        request,
        'catalog/corp.html',
        context={

        }
    )


class BagListView(generic.ListView):
    model = Bag


class BagDetailView(generic.DetailView):
    model = Bag


