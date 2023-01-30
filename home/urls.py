from home import views
from django.urls import path

app_name = 'all'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list', views.RestaurantList.as_view(), name='list'),
    path('create', views.CreateRestaurantView.as_view(), name='create'),
    path('search', views.search, name='search'),
    path('<slug:pk>', views.RestaurantDetailView.as_view(), name='detail'),
    path('update/<slug:pk>', views.RestaurantUpdateView.as_view(), name='update'),

]