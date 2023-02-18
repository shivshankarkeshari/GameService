from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from drf_yasg.utils import swagger_auto_schema


from .models import GameDetails
from .serialzers import GameDetailsSerialzer
from swagger_utils.games_CRUD import (delete_obj_swagger_response, get_list_of_objs_swagger_response, get_obj_swagger_responses, post_obj_swagger_response)



class SpecificGameDetailsView(APIView):
    @swagger_auto_schema(responses=get_obj_swagger_responses)
    def get(self, req, id=None):
        try:
            return Response({"message": None, "data": GameDetailsSerialzer(instance=GameDetails.objects.get(id=id), many=False).data}, 200)
        except Exception as e:
            return Response({"message": str(e), "data": None}, 404)

    @swagger_auto_schema(request_body=GameDetailsSerialzer, responses={
        200: post_obj_swagger_response[201],
        422: post_obj_swagger_response[422],
    })
    def put(self, req, id=None):
        try:
            data = req.data
            obj = GameDetails.objects.get(id=id)
            ser = GameDetailsSerialzer(instance=obj, data=data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"message": "data has been updated", "data": ser.data}, 200)
            else:
                return Response({"message": "there is issue with provided data", "data": None, "errors": ser.errors}, 200)
        except Exception as e:
            return Response({"message": str(e), "data": None}, 422)

    @swagger_auto_schema(responses=delete_obj_swagger_response)
    def delete(self, req, id=None):
        try:
            obj = GameDetails.objects.get(id=id)
            obj.delete()
            return Response({"message": "deleted"}, 202)
        except Exception as e:
            return Response({"message": str(e)}, 204)
    

class GamesDetailsView(APIView, LimitOffsetPagination):
    serializer_class = GameDetailsSerialzer

    @swagger_auto_schema(responses=get_list_of_objs_swagger_response)
    def get(self, req):
        games_objs = GameDetails.objects.all()
        results = self.paginate_queryset(games_objs, req, view=self)
        serializer = GameDetailsSerialzer(results, many=True)
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(request_body=GameDetailsSerialzer, responses=post_obj_swagger_response)
    def post(self, req):
        data = req.data
        ser = GameDetailsSerialzer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({"message": 
            "given game related data has been saved", "data": ser.data, "errors": None}, 201)
        else:
            return Response({"message": "please check given data", "data": None, "errors": ser.errors}, 422)
    

