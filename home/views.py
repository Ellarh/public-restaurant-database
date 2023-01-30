from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Restaurant


class IndexView(TemplateView):
    template_name = 'index.html'


class CreateRestaurantView(LoginRequiredMixin, CreateView):
    fields = ('name', 'address', 'city', 'state', 'website', 'phone_number')
    model = Restaurant
    template_name = 'home/add_restaurant.html'


class RestaurantList(ListView):
    context_object_name = 'restaurant_list'
    model = Restaurant
    template_name = 'home/restaurant_list.html'

    def get_queryset(self):
        return Restaurant.objects.filter(is_published=True).order_by('-id')


class RestaurantDetailView(DetailView):
    context_object_name = 'restaurant_detail'
    model = Restaurant
    template_name = 'home/restaurant_detail.html'


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    fields = ('name', 'address', 'city', 'state')
    template_name = 'home/restaurant_update.html'
    model = Restaurant


def search(request):
    # First query the database, and order and filter as you want
    queryset_list = Restaurant.objects.filter(is_published=True).order_by('-date_added')

    # Look for the model entry 'name' in the database, get it and filter it to be exactly as inputted in the form
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            # Django field lookups
            queryset_list = queryset_list.filter(name__iexact=name)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    context = {
        'restaurant': queryset_list,
    }
    return render(request, 'home/search.html', context=context)
