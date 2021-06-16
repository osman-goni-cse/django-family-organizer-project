from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder

# Create your views here.


def add_location(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    # print(lat)
    # print(lng)
    country = location.country
    if lat == None or lng == None:
        if address:
          address.delete()
        return HttpResponse('You address input is invalid')

    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)

    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'add_location/map_location.html', context)
