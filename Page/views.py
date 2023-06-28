from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from Page.models import Funnel
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from hitcount.views import HitCountDetailView

# Create your views here.
class Funnel_Detail(HitCountDetailView):
    model = Funnel
    template_name = 'Page/funnel_detail.html'
    context_object_name = 'funnel'

# Create your views here.
def contact(request,*args,**kwargs):
    return render(request,"Page/go.html")