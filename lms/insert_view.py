from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from livestock_management import models
from lms import serializers 

class AnimalProfileView(APIView):
    def post(self, request, format=None):
        serializer = serializers.AnimalProfileSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Animal profile created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HeatlthStatusInsert(APIView):
    def post(self, request, format=None):
        serializer = serializers.HealthStatusSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Health Status Updated Successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalStageInsert(APIView):
    def post(self, request, format=None):
        serializer = serializers.AnimalLifeStageSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Health Status Updated Successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    