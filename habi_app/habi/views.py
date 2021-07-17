from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from habi.models import *

# Create your views here.


class Search_Property (APIView):
    def get(self, request):

        try:
            # Lista de estados disponibles para el usuario
            public_status_ids = [3, 4, 5]

            # Busquedda sin parametro de filtros
            availables_porperties = StatusHistory.objects.filter(
                status_id__in=public_status_ids).values_list('property_id', flat=True).distinct()
            properties = Property.objects.filter(pk__in=availables_porperties)

            # Obtiene Query Params
            year = self.request.query_params.get('year')
            city = self.request.query_params.get('city')
            state_id = self.request.query_params.get('state')

            # aplica filtros de año y ciudad
            if year != None:
                properties = properties.filter(year=year)

            if city != None:
                properties = properties.filter(city=city)

            content = []
            for i in properties:
                raw = {}
                raw["id"] = i.id
                raw["address"] = i.address
                raw["city"] = i.city
                # obtiene el estado mas actulizado
                property_state = StatusHistory.objects.filter(
                    property_id=i.id).order_by("update_date").reverse()[0]
                state_label = Status.objects.get(pk=property_state.status_id)
                # aplica el filtro de estado
                if state_id != None:
                    if int(state_id) != property_state.status_id:
                        continue
                raw["state"] = {"id": property_state.status_id,
                                "description": state_label.name}
                raw["price"] = i.city
                raw["description"] = i.description
                content.append(raw)
            return Response(content, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error realizando la consutla': str(e)}, status=status.HTTP_409_CONFLICT)
