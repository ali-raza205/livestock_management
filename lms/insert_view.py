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
    
class CropsInsert(APIView):
    def post(self, request, format=None):
        serializer = serializers.CropsSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Crops Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalSale(APIView):
    def post(self, request, format=None):
        serializer = serializers.AnimalSaleSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "AnimalSale Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BreedingRecord(APIView):
    def post(self, request, format=None):
        serializer = serializers.BreedingRecordSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Breeding Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
class DeadAnimals(APIView):
    def post(self, request, format=None):
        serializer = serializers.DeadAnimalsSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Dead Animals Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class Equipments(APIView):
    def post(self, request, format=None):
        serializer = serializers.EquipmentsSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Equipments Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
class FarmImplements(APIView):
    def post(self, request, format=None):
        serializer = serializers.FarmImplementsSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Dead Animals Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class FeedingRecord(APIView):
    def post(self, request, format=None):
        serializer = serializers.FeedingRecordSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Feeding Record Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class HealthRecord(APIView):
    def post(self, request, format=None):
        serializer = serializers.HealthRecordSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Health Record Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class MilkBuyer(APIView):
    def post(self, request, format=None):
        serializer = serializers.MilkBuyerSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Milk Buyer Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
class MilkSales(APIView):
    def post(self, request, format=None):
        serializer = serializers.MilkSalesSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Milk Sales Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class MilkingRecord(APIView):
    def post(self, request, format=None):
        serializer = serializers.MilkingRecordSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "MilkingRecord Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
class Staff(APIView):
    def post(self, request, format=None):
        serializer = serializers.StaffSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Staff Created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class InsertFarmPurchase(APIView):
    def post(self, request, format=None):
        serializer = serializers.FarmPurchaseSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Purchase successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  