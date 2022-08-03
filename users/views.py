from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Import User UpdateForm, ProfileUpdatForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserUpdateForm
    form_second_class = ProfileUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy('users:profile')




