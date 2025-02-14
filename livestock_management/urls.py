from django.urls import path
from livestock_management import settings
from lms import views
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
    path('insertprofile/',views.AnimalProfileView.as_view())
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
