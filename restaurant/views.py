from django.shortcuts import render
from . import serializers
from .models import Booking, Menu
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class BookingViewSet(ModelViewSet):
    serializer_class = serializers.BookingSerializer
    queryset = Booking.objects.all()


"""
class MenuView(APIView):
    def get(self,request):
        menus = Menu.objects.all()
        serializer = serializers.MenuSerializer(menus, many=True)
        return Response(serializer.data)

class BookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = serializers.BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
