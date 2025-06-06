from django.shortcuts import render
from rest_framework.views import APIView # type: ignore
from .serializers import *
from rest_framework import status, permissions, authentication # type: ignore
from rest_framework.response import Response # type: ignore

#Register organization API
class RegisterOrganizationAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = RegisterOrganizationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Register package API
class UserRegisterPackageAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Booking package API
class BookingPackageAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = BookingPackageSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


#Display all packages to user
class ReturnAllPackagesAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        packages = PackageRegistration.objects.all()
        serializer = UserRegisterSerializer(packages, many=True)
        return Response(serializer.data)
    

#Display all registred organizations to user
class ReturnAllRegistredOrganizationAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        registred_organizations = Organizations.objects.all()
        serializer = RegisterOrganizationSerializer(registred_organizations, many=True)
        return Response(serializer.data)
    

#Display package the user has booked
class UserBookingPackagesAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        bookings = BookingPackage.objects.filter(user=user)
        serializer = BookingPackageSerializer(bookings, many=True)
        return Response(serializer.data)


#Vuta packages the organization husika
class OrganizationPackageAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        organizationPackage = PackageRegistration.objects.filter(user=user)
        serializer = UserRegisterSerializer(organizationPackage, many=True)
        return Response(serializer.data)
    
