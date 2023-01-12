from django.shortcuts import render
import urllib.request
import json
from http import HTTPStatus
from urllib.error import HTTPError

# Create your views here.

def index (request):
    try:
        
        if request.method == 'POST' :
            pokemon = request.POST['pokemon'].lower()
            pokemon = pokemon.replace(' ', '%20')
            
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
            
            url_pokeapi.add_header('User-Agent','charmander')
            
            source = urllib.request.urlopen(url_pokeapi).read()
            
            list_of_data = json.loads(source)
            
            height_obtained = (float(list_of_data['height'])* 0.1)
            height_rounded = round(height_obtained, 2)
            
            weight_obtained = (float(list_of_data['weight'])* 0.1)
            weight_rounded = round(weight_obtained, 2)
            
            data = {
                "number":str(list_of_data['id']),
                "name":str(list_of_data['name']).capitalize(),
                "height":str(height_rounded) + " M",
                "weight":str(weight_rounded) + " Kg",
                "sprite":str(list_of_data['sprites']['front_default']),
                
            }
            print(data)
        else:
            data = {}
        
        return render(request,'main/index.html',data)
    except HTTPError as e: 
        if e.code == 404:
            return render(request, 'main/404.html')