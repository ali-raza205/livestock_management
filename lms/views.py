from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from livestock_management import models
from lms import serializers 

class AnimalProfileList(APIView):
    def get(self, request, format=None):
        animal_profiles = models.AnimalProfile.objects.all()
        serializer = serializers.AnimalProfileSerializer(animal_profiles, many=True)
        return Response(serializer.data)
    
class GenderList(APIView):
    def get(self, request, format=None):
        Genders = models.Gender.objects.all()
        serializer = serializers.GenderSerializer(Genders, many=True)
        return Response(serializer.data)
    
class AnimalType(APIView):
    def get(self, request, format=None):
        Types = models.AnimalType.objects.all()
        serializer = serializers.AnimalTypeSerializer(Types, many=True)
        return Response(serializer.data)
    
class AnimalBreed(APIView):
    def post(self, request, format=None):
        type= request.data.get('AnimalTypeId')
        print (type)
        Breeds = models.Breeds.objects.filter(animal_type_id=type)
        serializer = serializers.BreedsSerializer(Breeds, many=True)
        return Response(serializer.data)
class lifecycle(APIView):
    def post(self, request, format=None):
        Lifecycle = models.Lifecycle.objects.all()
        serializer = serializers.LifecycleSerializer(Lifecycle, many=True)
        return Response(serializer.data)
class lifeStage(APIView):
    def post(self, request, format=None):
        LifeStage = models.LifeStage.objects.all()
        serializer = serializers.LifeStageSerializer(LifeStage, many=True)
        return Response(serializer.data)
class Feeds(APIView):
    def get(self, request, format=None):
        Feeds = models.Feeds.objects.all()
        serializer = serializers.FeedsSerializer(Feeds, many=True)
        return Response(serializer.data)
class HealthStatus(APIView):
    def get(self, request, format=None):
        Feeds = models.HealthStatus.objects.all()
        serializer = serializers.HealthStatusSerializer(Feeds, many=True)
        return Response(serializer.data)

class BreedingMethod(APIView):
    def get(self, request, format=None):
        BM = models.BreedingMethods.objects.all()
        serializer = serializers.BreedingMethodsSerializer(BM, many=True)
        return Response(serializer.data)
class PaymentMethod(APIView):
    def post(self, request, format=None):
        PaymentMethod = models.PaymentMethod.objects.all()
        serializer = serializers.PaymentMethodSerializer(PaymentMethod, many=True)
        return Response(serializer.data)
class PaymentType(APIView):
    def post(self, request, format=None):
        PaymentType = models.PaymentType.objects.all()
        serializer = serializers.PaymentTypeSerializer(PaymentType, many=True)
        return Response(serializer.data)
class Results(APIView):
    def post(self, request, format=None):
        Results = models.Results.objects.all()
        serializer = serializers.ResultsSerializer(Results, many=True)
        return Response(serializer.data)
class Shifts(APIView):
    def post(self, request, format=None):
        Results = models.Shifts.objects.all()
        serializer = serializers.ShiftsSerializer(Results, many=True)
        return Response(serializer.data)

#Store Data  
class AnimalProfileView(APIView):
    def post(self, request, format=None):
        serializer = serializers.AnimalProfileSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Animal profile created successfully", "data": serializer.data}, status=200)
        print (serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

