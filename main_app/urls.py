from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('stars/', views.stars_index, name='index'),
    path('stars/create/', views.StarCreate.as_view(), name='stars_create'),
    path('stars/<int:star_id>/', views.stars_detail, name='detail'),
    path('stars/<int:pk>/update/', views.StarUpdate.as_view(), name='stars_update'),
    path('stars/<int:pk>/delete/', views.StarDelete.as_view(), name='stars_delete'),

    path('planets/', views.planets_index, name='planets_index'),
    path('planets/create/', views.PlanetCreate.as_view(), name='planets_create'),
    path('planets/<int:planet_id>/', views.planets_detail, name='planets_detail'),
    path('planets/<int:pk>/update/', views.PlanetUpdate.as_view(), name='planets_update'),
    path('planets/<int:pk>/delete/', views.PlanetDelete.as_view(), name='planets_delete'),
    
	
	path('satellites/', views.satellites_index, name='satellites_index'),
    path('satellites/create/', views.SatelliteCreate.as_view(), name='satellites_create'),
    path('satellites/<int:satellite_id>/', views.satellites_detail, name='satellites_detail'),
    path('satellites/<int:pk>/update/', views.SatelliteUpdate.as_view(), name='satellites_update'),
    path('satellites/<int:pk>/delete/', views.SatelliteDelete.as_view(), name='satellites_delete'),
]