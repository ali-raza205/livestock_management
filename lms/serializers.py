from rest_framework import serializers
from livestock_management.models import AnimalProfile, AnimalSale, AnimalType, BreedingMethods, BreedingRecord, Breeds, DeadAnimals,\
    FeedingRecord, Feeds, Gender, HealthRecord, HealthStatus, Lifecycle, MilkBuyer, MilkBuyerType, MilkSales, \
    MilkingRecord, PaymentMethod, PaymentType, Pricing, Results, Shifts, Staff, AnimalAcquisition, LifeStage, \
    AnimalLifeCycle, AnimalLifeStage,CurrentLifeCycle,CurrentLifeStage, OperationalStatus,Crops, Equipments, PurchaseType, FarmPurchase,AnimalCode,AssignCode

# Serializer for AnimalProfile model
class AnimalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalProfile
        fields = '__all__'
class AnimalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalCode
        fields = '__all__'
class AssignCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignCode
        fields = '__all__'

# Serializer for AnimalSale model
class AnimalSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalSale
        fields = '__all__'
class AnimalLifeCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalLifeCycle
        fields = '__all__'
class AnimalLifeStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalLifeStage
        fields = '__all__'
class CurrentLifeCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentLifeCycle
        fields = '__all__'
class CurrentLifeStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentLifeStage
        fields = '__all__'

# Serializer for AnimalType model
class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = '__all__'

# Serializer for BreedingMethods model
class BreedingMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreedingMethods
        fields = '__all__'

# Serializer for BreedingRecord model
class BreedingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreedingRecord
        fields = '__all__'

# Serializer for Breeds model
class BreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeds
        fields = '__all__'

class AnimalAcquisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalAcquisition
        fields = '__all__'

# Serializer for DeadAnimals model
class DeadAnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeadAnimals
        fields = '__all__'

# Serializer for FeedingRecord model
class FeedingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedingRecord
        fields = '__all__'

# Serializer for Feeds model
class FeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = '__all__'

# Serializer for Gender model
class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

# Serializer for HealthRecord model
class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = '__all__'

# Serializer for HealthStatus model
class HealthStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthStatus
        fields = '__all__'

# Serializer for Lifecycle model
class LifecycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lifecycle
        fields = '__all__'
# Serializer for LifeStage model
class LifeStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeStage
        fields = '__all__'

# Serializer for MilkBuyer model
class MilkBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkBuyer
        fields = '__all__'

# Serializer for MilkBuyerType model
class MilkBuyerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkBuyerType
        fields = '__all__'

# Serializer for MilkSales model
class MilkSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkSales
        fields = '__all__'

# Serializer for MilkingRecord model
class MilkingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkingRecord
        fields = '__all__'

# Serializer for PaymentMethod model
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
        
class OperationalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalStatus
        fields = '__all__'        

# Serializer for PaymentType model
class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'
class PurchaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseType
        fields = '__all__'

# Serializer for Pricing model
class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'

# Serializer for Results model
class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'

# Serializer for Shifts model
class ShiftsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifts
        fields = '__all__'

# Serializer for Staff model
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        
class CropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crops
        fields = '__all__'

class EquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipments
        fields = '__all__'

class FarmPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmPurchase
        fields = '__all__'


