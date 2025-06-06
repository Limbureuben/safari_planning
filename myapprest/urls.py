from django.urls import path
from .views import *

urlpatterns = [
    path('register-organization/', RegisterOrganizationAPI.as_view()),
    path('register-package/', UserRegisterPackageAPI.as_view()),
    path('booking-package/', BookingPackageAPI.as_view()),
    path('all-packages/', ReturnAllPackagesAPI.as_view()),
    path('all-registered-organizations/', ReturnAllRegistredOrganizationAPI.as_view()),
    path('my-booking/', UserBookingPackagesAPI.as_view()),
    path('organization-packages/', OrganizationPackageAPI.as_view()),
]
