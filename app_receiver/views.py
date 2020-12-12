from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import GPSData
import json


def index(request):
    return HttpResponse("Hello, world. You're at the app_receiver index.")


def get_data(request):
    all_data = serializers.serialize('json', GPSData.objects.all())
    return HttpResponse(json.dumps({'data': json.loads(all_data)}), content_type="application/json")


def save_data(request):
    data = json.loads(request.body)
    print("Got json payload :: {}".format(json.dumps(data)))
    object = GPSData(latitude=data["latitude"], longitude=data["longitude"])
    object.save()
    return HttpResponse(json.dumps({'data': json.loads(serializers.serialize('json', [object]))}), content_type="application/json")
