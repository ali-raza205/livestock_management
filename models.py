# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnimalProfile(models.Model):
    profile_id = models.BigAutoField(primary_key=True)
    animal_code = models.DecimalField(max_digits=65535, decimal_places=65535)
    breed = models.ForeignKey('Breeds', models.DO_NOTHING, blank=True, null=True)
    gender = models.ForeignKey('Gender', models.DO_NOTHING, blank=True, null=True)
    d_o_b = models.DateField(blank=True, null=True)
    parent_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animal_profile'


class AnimalSale(models.Model):
    animal_sale_id = models.BigAutoField(primary_key=True)
    animal = models.ForeignKey(AnimalProfile, models.DO_NOTHING)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING)
    date = models.DateField()
    sold_to = models.TextField()

    class Meta:
        managed = False
        db_table = 'animal_sale'


class AnimalType(models.Model):
    animal_type_id = models.BigAutoField(primary_key=True)
    animal_type_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'animal_type'


class BreedingMethods(models.Model):
    breeding_method_id = models.BigAutoField(primary_key=True)
    breeding_method_name = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'breeding_methods'


class BreedingRecord(models.Model):
    br_rec_id = models.BigAutoField(primary_key=True)
    animal = models.ForeignKey(AnimalProfile, models.DO_NOTHING)
    breeding_method = models.ForeignKey(BreedingMethods, models.DO_NOTHING, blank=True, null=True)
    br_date = models.DateField(blank=True, null=True)
    mate_breed = models.ForeignKey('Breeds', models.DO_NOTHING, db_column='mate_breed', blank=True, null=True)
    result = models.ForeignKey('Results', models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'breeding_record'


class Breeds(models.Model):
    breed_id = models.BigAutoField(primary_key=True)
    animal_type = models.ForeignKey(AnimalType, models.DO_NOTHING)
    breed_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'breeds'


class DeadAnimals(models.Model):
    profile_id = models.BigIntegerField(primary_key=True)
    animal_code = models.BigIntegerField()
    breed_id = models.BigIntegerField(blank=True, null=True)
    gender_id = models.BigIntegerField(blank=True, null=True)
    d_o_b = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    death_cause = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dead_animals'


class FeedingRecord(models.Model):
    f_rec_id = models.BigAutoField(primary_key=True)
    animal = models.ForeignKey(AnimalProfile, models.DO_NOTHING)
    feed = models.ForeignKey('Feeds', models.DO_NOTHING, blank=True, null=True)
    feed_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feeding_record'


class Feeds(models.Model):
    feed_id = models.BigAutoField(primary_key=True)
    feed_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'feeds'


class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True)
    gender = models.TextField()

    class Meta:
        managed = False
        db_table = 'gender'


class HealthRecord(models.Model):
    he_rec_id = models.BigAutoField(primary_key=True)
    animal = models.ForeignKey(AnimalProfile, models.DO_NOTHING)
    diagnoses = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    from_field = models.DateField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.DateField(blank=True, null=True)
    veternarian = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health_record'


class HealthStatus(models.Model):
    health_status_id = models.BigAutoField(primary_key=True)
    health_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'health_status'


class Lifecycle(models.Model):
    stage_id = models.BigAutoField(primary_key=True)
    stage_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'lifecycle'


class MilkBuyer(models.Model):
    buyer_id = models.BigAutoField(primary_key=True)
    buyer_name = models.TextField()
    milk_buyer_type = models.ForeignKey('MilkBuyerType', models.DO_NOTHING)
    whatspp_no = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milk_buyer'


class MilkBuyerType(models.Model):
    milk_buyer_type_id = models.BigAutoField(primary_key=True)
    buyer_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'milk_buyer_type'


class MilkSales(models.Model):
    sale_id = models.BigAutoField(primary_key=True)
    buyer = models.ForeignKey(MilkBuyer, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    date = models.DateField()
    price_id = models.BigIntegerField()
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    recieved_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    payment_type = models.ForeignKey('PaymentType', models.DO_NOTHING, db_column='payment_type')
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, db_column='payment_method')
    vehicle_no = models.TextField(blank=True, null=True)
    person_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milk_sales'


class MilkingRecord(models.Model):
    m_rec_id = models.BigAutoField(primary_key=True)
    animal = models.ForeignKey(AnimalProfile, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    shift = models.ForeignKey('Shifts', models.DO_NOTHING, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'milking_record'


class PaymentMethod(models.Model):
    payemnt_method_id = models.BigAutoField(primary_key=True)
    payment_method_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'payment_method'


class PaymentType(models.Model):
    payment_type_id = models.BigAutoField(primary_key=True)
    payment_type_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'payment_type'


class Pricing(models.Model):
    price_id = models.BigAutoField(primary_key=True)
    milk_buyer_type = models.ForeignKey(MilkBuyerType, models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'pricing'


class Results(models.Model):
    result_id = models.BigAutoField(primary_key=True)
    result_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'results'


class Shifts(models.Model):
    shift_id = models.BigAutoField(primary_key=True)
    shift_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'shifts'


class Staff(models.Model):
    staff_id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    designation = models.TextField()
    joining_date = models.DateField()
    cnin = models.DecimalField(max_digits=65535, decimal_places=65535)
    salary = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'staff'
