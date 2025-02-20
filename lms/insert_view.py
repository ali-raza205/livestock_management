from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from livestock_management import models
from lms import serializers ,utilityfunctions

class InsertAnimal(APIView):
    def post(self, request, format=None):
        try:
            # Create animal profile
            profile_serializer = serializers.AnimalProfileSerializer(data=request.data)
            print(profile_serializer)
            if not profile_serializer.is_valid():
                return Response({
                    "message": "Validation error",
                    "errors": print(profile_serializer.errors)
                }, status=status.HTTP_400_BAD_REQUEST)
            
            animal_profile = profile_serializer.save()
            
            # Handle automatic code assignment
            if 'animal_tag_code' not in request.data:
                assign_code_to_animal(animal_profile)
            
            # Handle AnimalLifeStage if provided
            life_stage_serializer = None
            if 'life_stage' in request.data:
                life_stage_data = {
                    'animal': animal_profile.animal_id,
                    'life_stage': request.data['life_stage'],
                    'start_date': request.data['start_date']
                }
                life_stage_serializer = serializers.AnimalLifeStageSerializer(data=life_stage_data)
                if not life_stage_serializer.is_valid():
                    return Response({
                        "message": "Life stage validation error",
                        "errors": print(life_stage_serializer.errors)
                    }, status=status.HTTP_400_BAD_REQUEST)
                life_stage_serializer.save()
            
            # Handle CurrentLifeStage if provided
            current_life_stage_serializer = None
            if 'current_life_stage' in request.data:
                current_life_stage_data = {
                    'animal_id': animal_profile.animal_id,
                    'life_stage_id': request.data['current_life_stage']
                }
                current_life_stage_serializer = serializers.CurrentLifeStageSerializer(data=current_life_stage_data)
                if not current_life_stage_serializer.is_valid():
                    return Response({
                        "message": "Current life stage validation error",
                        "errors": print(current_life_stage_serializer.errors)
                    }, status=status.HTTP_400_BAD_REQUEST)
                current_life_stage_serializer.save()

            # Handle AnimalLifeCycle if provided
            life_cycle_serializer = None
            if 'life_cycle' in request.data:
                life_cycle_data = {
                    'animal': animal_profile.animal_id,
                    'life_cycle': request.data['life_cycle'],
                    'date': request.data['life_cycle_date']
                }
                life_cycle_serializer = serializers.AnimalLifeCycleSerializer(data=life_cycle_data)
                if not life_cycle_serializer.is_valid():
                    return Response({
                        "message": "Life cycle validation error",
                        "errors": print(life_cycle_serializer.errors)
                    }, status=status.HTTP_400_BAD_REQUEST)
                life_cycle_serializer.save()

            # Handle CurrentLifeCycle if provided
            current_life_cycle_serializer = None
            if 'current_life_cycle' in request.data:
                current_life_cycle_data = {
                    'animal_id': animal_profile.animal_id,
                    'life_cycle_id': request.data['current_life_cycle']
                }
                current_life_cycle_serializer = serializers.CurrentLifeCycleSerializer(data=current_life_cycle_data)
                if not current_life_cycle_serializer.is_valid():
                    return Response({
                        "message": "Current life cycle validation error",
                        "errors": print(current_life_cycle_serializer.errors)
                    }, status=status.HTTP_400_BAD_REQUEST)
                current_life_cycle_serializer.save()

            # Handle ParentDetails if provided
            parent_details_serializer = None
            if 'parent_details' in request.data:
                parent_details_data = {
                    'parent': request.data['parent_details'],
                    'animal': animal_profile.animal_id
                }
                parent_details_serializer = serializers.ParentDetailsSerializer(data=parent_details_data)
                if not parent_details_serializer.is_valid():
                    return Response({
                        "message": "Parent details validation error",
                        "errors": print(parent_details_serializer.errors)
                    }, status=status.HTTP_400_BAD_REQUEST)
                parent_details_serializer.save()

            # Handle AnimalImages if provided
            image_serializers = []
            if 'images' in request.data and isinstance(request.data['images'], list):
                for image_data in request.data['images']:
                    image_data['profile'] = animal_profile.animal_id
                    image_serializer = serializers.AnimalImageSerializer(data=image_data)
                    if not image_serializer.is_valid():
                        return Response({
                            "message": "Image validation error",
                            "errors": print(image_serializer.errors)
                        }, status=status.HTTP_400_BAD_REQUEST)
                    image_serializer.save()
                    image_serializers.append(image_serializer.data)
            
            return Response({
                "message": "Animal profile and related data created successfully",
                "data": {
                    "profile": profile_serializer.data,
                    "life_stage": life_stage_serializer.data if life_stage_serializer else None,
                    "current_life_stage": current_life_stage_serializer.data if current_life_stage_serializer else None,
                    "life_cycle": life_cycle_serializer.data if life_cycle_serializer else None,
                    "current_life_cycle": current_life_cycle_serializer.data if current_life_cycle_serializer else None,
                    "parent_details": parent_details_serializer.data if parent_details_serializer else None,
                    "images": image_serializers
                }
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            import traceback
            print(f"Error creating animal profile: {str(e)}")
            print(traceback.format_exc())
            return Response({
                "message": "Error creating animal profile",
                "error": str(e),
                "traceback": traceback.format_exc()
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
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
    
def get_available_code():
    """Find an available code or generate a new one."""
    available_code = models.AnimalCode.objects.filter(code_status=False).first()
    
    if available_code:
        available_code.code_status = True  # Mark as assigned
        available_code.save()
        return available_code.code_text
    else:
        # Generate a new code if no unused codes exist
        last_code = models.AnimalCode.objects.order_by('-code_id').first()
        new_code = str(int(last_code.code_text) + 1) if last_code else "1000"  # Start from 1000
        return models.AnimalCode.objects.create(code_text=new_code, code_status=True).code_text
def assign_code_to_animal(animal):
    """Assigns an available code to a new animal."""
    animal_code = get_available_code()
    models.AssignCode.objects.create(animal=animal, code=models.AnimalCode.objects.get(code_text=animal_code))
    
def release_animal_code(animal):
    """Marks an animal's code as available when it dies or is sold."""
    assigned_code = models.AssignCode.objects.filter(animal=animal).first()
    
    if assigned_code:
        # Mark code as available again
        models.AnimalCode.objects.filter(code_id=assigned_code.code.code_id).update(code_status=False)
        assigned_code.delete()