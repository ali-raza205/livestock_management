from django.urls import path
from livestock_management import settings
from lms import views, insert_view
from django.conf.urls.static import static


urlpatterns = [
    path('animal_profiles/', views.AnimalProfileList.as_view(), name='animal_profile_list'),
    path('genders/', views.GenderList.as_view(), name='Genders'),
    path('types/', views.AnimalType.as_view(), name='Types'),
    path('breeds/', views.AnimalBreed.as_view(), name='Breeds'),
    path('feeds/', views.Feeds.as_view(), name='Feeds'),
    path('lifecycle/', views.lifecycle.as_view(), name='Lifecycle'),
    path('lifestage/', views.lifeStage.as_view(), name='Lifestage'),
    path('healthstatus/', views.HealthStatus.as_view(), name='HealthStatus'),
    path('breedingmethod/', views.BreedingMethod.as_view(), name='breedingmethod'),
    path('healthstatus/', views.HealthStatus.as_view(), name='HealthStatus'),
    path('OperationalStatus/', views.OperationalStatus.as_view(), name='OperationalStatus'),
    path('PaymentMethod/', views.PaymentMethod.as_view(), name='PaymentMethod'),
    path('PaymentType/', views.PaymentType.as_view(), name='PaymentType'),
    path('Results/', views.Results.as_view(), name='Results'),
    path('Shifts/', views.Shifts.as_view(), name='Shifts'),
     path('purchasetype/', views.PurchaseType.as_view(), name='Shifts'),
    path('insertprofile/',insert_view.InsertAnimal.as_view()),
    path('animalsale/',insert_view.AnimalSale.as_view()),
    path('breedingrecord/',insert_view.AnimalSale.as_view()),
    path('deadanimals/',insert_view.DeadAnimals.as_view()),
    path('equipments/',insert_view.Equipments.as_view()),
    path('FarmImplements/',insert_view.FarmImplements.as_view()),
    path('FeedingRecord/',insert_view.FeedingRecord.as_view()),
    path('HealthRecord/',insert_view.HealthRecord.as_view()),
    path('MilkBuyer/',insert_view.MilkBuyer.as_view()),
    path('MilkSales/',insert_view.MilkSales.as_view()),
    path('MilkingRecord/',insert_view.MilkingRecord.as_view()),
    path('insertCrops/',insert_view.CropsInsert.as_view()),
    path('addpurchase/',insert_view.InsertFarmPurchase.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)