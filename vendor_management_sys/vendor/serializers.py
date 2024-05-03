
from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = '__all__'
        
    def validate(self, data):
        special_char = '!@#$%^&*()-+?_=,<>/'
        if any(c in special_char for c in data['name']):
            raise serializers.ValidationError('name can not contain special characters')
        return data
        

        
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        # depth = 1
        
    def validate_po_number(self, data):
        if len(data) > 20:
            raise serializers.ValidationError("PO number length must be <= 20 characters")       
        return data

    def validate_quantity(self, data):
        if data <= 0:
            raise serializers.ValidationError("Quantity must be a positive integer")
        return data
    
    def validate(self, data):
        options = ['pending', 'completed', 'canceled']
        if data['status'] not in options:
            raise serializers.ValidationError('status should be pending or completed or canceled')
        return data
        
    
    
class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
        
    def validate_on_time_delivery_rate(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("On-time delivery rate must be between 0 and 100")
        return value