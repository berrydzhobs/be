from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from Content.models import Article, Item, Project, Client, Service, Tool
from Page.models import Funnel
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Feed(ListView):
    model = Article
    template_name = 'Feed/feed.html'
    context_object_name = 'i'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tools'] = Tool.objects.all().order_by('?')[:2]
        context['articles'] = Article.objects.all().order_by('?')[:3]
        context['services'] = Service.objects.all().order_by('?')[:2]
        context['items'] = Item.objects.all().order_by('?')[:4]
        context['pro'] = Project.objects.all().order_by('?')[:1]
        return context

class Item_List(ListView):
    model = Item
    template_name = 'Feed/feed_item.html'
    context_object_name = 'item'
    paginate_by = 12
    ordering = ('-date')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['featured_item'] = Item.objects.all().order_by('?')[:1]
        return context

class Item_List_Gadget(ListView):
    model = Item
    template_name = 'Feed/feed_item.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['item'] = Item.objects.filter(digital=False).order_by('?')
        return context

class Item_List_Software(ListView):
    model = Item
    template_name = 'Feed/feed_item.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['item'] = Item.objects.filter(digital=True).order_by('?')
        return context


class Tools_List(ListView):
    model = Tool
    template_name = 'Feed/feed_tool.html'
    context_object_name = 'item'
    paginate_by = 12
    ordering = ('-date')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['featured_item'] = Tool.objects.all().order_by('?')[:1]
        return context




class Article_List(ListView):
    model = Article
    template_name = 'Feed/feed_article.html'
    context_object_name = 'note'
    paginate_by = 12
    ordering = ('-date')

class Article_List_Health(ListView):
    model = Article
    template_name = 'Feed/feed_article.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['note'] = Article.objects.filter(health=True).order_by('?')
        return context

class Article_List_Finance(ListView):
    model = Article
    template_name = 'Feed/feed_article.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['note'] = Article.objects.filter(finance=True).order_by('?')
        return context

class Article_List_Technology(ListView):
    model = Article
    template_name = 'Feed/feed_article.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['note'] = Article.objects.filter(technology=True).order_by('?')
        return context

class Article_List_Travel(ListView):
    model = Article
    template_name = 'Feed/feed_article.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['note'] = Article.objects.filter(travel=True).order_by('?')
        return context

class Article_List_Worklife(ListView):
    model = Article
    template_name = 'Feed/feed_article.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['note'] = Article.objects.filter(worklife=True).order_by('?')
        return context

class Article_List_Culture(ListView):
    model = Article
    template_name = 'Feed/feed_article.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['note'] = Article.objects.filter(culture=True).order_by('?')
        return context

class Project_List(ListView):
    model = Project
    template_name = 'Feed/feed_project.html'
    context_object_name = 'm'
    paginate_by = 4
    ordering = ('-date')

class Client_List(ListView):
    model = Client
    template_name = 'Feed/feed_client.html'
    context_object_name = 'clients'
    paginate_by = 6
    ordering = ('-date')

class Service_List(ListView):
    model = Service
    template_name = 'Feed/feed_service.html'
    context_object_name = 'm'
    paginate_by = 4
    ordering = ('-date')

class Funnel_List(ListView):
    model = Funnel
    template_name = 'Feed/feed_funnel.html'
    context_object_name = 'funnel'
    paginate_by = 4
    ordering = ('-date')