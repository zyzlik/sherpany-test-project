import os

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .models import Location, FusionTable


API_KEY = settings.GOOGLE_API_KEY


class MapView(View):
    def get(self, request):
        fusion_table = FusionTable()
        context = {
            'API_KEY': API_KEY,
            'fusion_table': fusion_table
        }
        return render(
            request,
            os.path.join('map', 'index.html'),
            context,
        )


class SaveLocationView(View):
    def get(self, request):
        return HttpResponseRedirect('/')

    def post(self, request):
        if request.is_ajax():
            address = request.POST.get('address')
            lat = request.POST.get('lat')
            lng = request.POST.get('lng')
            fusion_table_id = request.POST.get('fusion_table')
            fusion_table = FusionTable(fusion_table_id)
            # Check for uniqness in Fusion Table
            if fusion_table.check_dublicate_fusion_table(address):
                response = ''
            else:
                fusion_table.insert_fusion_table(lat, lng, address)
                # Save to DB
                location = Location(
                    address=address,
                    lat=lat,
                    lng=lng
                )
                location.save()
                response = address
            return HttpResponse(response)


class ResetTablesView(View):
    def get(self, request):
        return HttpResponseRedirect('/')

    def post(self, request):
        if request.is_ajax():
            fusion_table_id = request.POST.get('fusion_table')
            fusion_table = FusionTable(fusion_table_id)
            fusion_table.reset_fusion_table()
            Location.objects.all().delete()
            return HttpResponse()
