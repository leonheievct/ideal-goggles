from .models import BlockedDate,Bookings
from rest_framework import serializers

class BlockedDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedDate
        fields = '__all__'


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        field = '__all__'


    