from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from geopy.geocoders import Nominatim  # pip install geopy
geolocator = Nominatim(user_agent="http")

@csrf_exempt
def set_location(request):
    if request.method == 'POST' and 'longitude' in request.POST:
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        # Fetch Address 
        location = geolocator.reverse(latitude+","+longitude)
        address = location.raw['address']           

        response = HttpResponse('success')
        response.set_cookie('address', address)
        return response
    
    return HttpResponse('This page is not accessale.')


def location(request):
    address = ''
    try:
        # Cookie get
        address_data = request.COOKIES['address']
        address = eval(address_data)
        print(address['suburb'])
        print(address['city'])
        print(address['postcode'])
        print(address['state'])
        print(address['country'])
        print(address['country_code'])

    except KeyError:
        # Cookie is not set
        pass
    
    return render(request, 'location.html', context={'address': address})
