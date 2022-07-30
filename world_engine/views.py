from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = "world_engine/index.html"