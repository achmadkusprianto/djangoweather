# This is my file
from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=01595E58-7A67-4E14-93CC-ADC5D844CB36")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    if api[0]['Category']['Name'] == "Good":
        category_description = 'Cuacanya bagus'
        category_color = 'good'      
    elif api[0]['Category']['Name'] == "Moderate":
        category_description = 'Cuacanya sedang'
        category_color = 'moderate'      
    elif api[0]['Category']['Name'] == "Unhealthy for Sensitive":
        category_description = 'Cuacanya kurang bagus'
        category_color = 'usg'      
    elif api[0]['Category']['Name'] == "Unhealthy":
        category_description = 'Cuacanya tidak sehat'
        category_color = 'unhealthy'      
    elif api[0]['Category']['Name'] == "Very Unhealthy":
        category_description = 'Cuacanya sangat tidak sehat'
        category_color = 'very_unhealthy'      
    elif api[0]['Category']['Name'] == "Hazardous":
        category_description = 'Cuacanya berbahaya'
        category_color = 'hazardous'      


    return render(request, 'home.html', {
        'api': api, 
        'category_description': category_description, 
        'category_color': category_color
        })


def about(request):
    return render(request, 'about.html', {})