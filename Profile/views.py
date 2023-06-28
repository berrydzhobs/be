from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from Content.models import Article, Item, Project, Client, Service, Tool
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from hitcount.views import HitCountDetailView
from .models import Profile

# Create your views here.
class AuthorView(DetailView):
    model = Profile
    template_name = 'Author/profile.html'
    context_object_name = 'profile'

    def get_slug_field(self):
        return 'user__username'

    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.object.user)
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(user=user).order_by('-date')[:3]
        context['tools'] = Tool.objects.filter(user=user).order_by('-date')[:5]
        context['items'] = Item.objects.filter(user=user).order_by('-date')[:3]
        context['projects'] = Project.objects.filter(user=user).order_by('-date')[:5]
        context['services'] = Service.objects.filter(user=user).order_by('-date')[:5]
        return context

class Authorarticles(DetailView):
    model = Profile
    template_name = 'Author/articles.html'
    context_object_name = 'profile'

    def get_slug_field(self):
        return 'user__username'

    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.object.user)
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(user=user).order_by('-date')
        return context

class Authortools(DetailView):
    model = Profile
    template_name = 'Author/tools.html'
    context_object_name = 'profile'

    def get_slug_field(self):
        return 'user__username'

    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.object.user)
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.filter(user=user).order_by('-date')
        return context

class Authoritems(DetailView):
    model = Profile
    template_name = 'Author/items.html'
    context_object_name = 'profile'

    def get_slug_field(self):
        return 'user__username'

    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.object.user)
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.filter(user=user).order_by('-date')
        return context

class Authorprojects(DetailView):
    model = Profile
    template_name = 'Author/projects.html'
    context_object_name = 'profile'

    def get_slug_field(self):
        return 'user__username'

    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.object.user)
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(user=user).order_by('-date')
        return context

class Authorservices(DetailView):
    model = Profile
    template_name = 'Author/services.html'
    context_object_name = 'profile'

    def get_slug_field(self):
        return 'user__username'

    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.object.user)
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(user=user).order_by('-date')[:5]
        return context