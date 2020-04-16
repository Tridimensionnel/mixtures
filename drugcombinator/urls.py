from django.urls import path, include, register_converter
from django.views.decorators.cache import cache_page
from drugcombinator.converters import SlugListConverter
from drugcombinator import views


cache = cache_page(60 * 10)

register_converter(SlugListConverter, 'slug_list')

urlpatterns = [
    path('', views.main, name='main'),
    path('combo/<slug_list:slugs>/', views.combine, name='combine'),
    path('substance/<str:name>/', views.drug, name='drug'),
    path('substances/', views.drug_search, name='drug_search'),
    path('table/', views.combine_chart, name='combine_chart'),
    path('docs/', views.docs, name='docs'),

    path('autocomplete.js', cache(views.autocomplete), name='autocomplete')
]
