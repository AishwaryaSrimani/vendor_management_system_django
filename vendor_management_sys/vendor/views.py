from rest_framework.decorators import api_view
from rest_framework.response import Response
from vendor.models import Vendor, PurchaseOrder, HistoricalPerformance
from vendor.serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from rest_framework import status
from django.utils import timezone


# Create your views here.

@api_view(['GET', 'POST'])
def vendors(request):
    if request.method == 'GET':
        obj = Vendor.objects.all()
        serializer = VendorSerializer(obj, many=True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = VendorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET', 'PUT', 'DELETE'])
def vendors_update_delete(request, vendor_id):
    try:
        vendor = Vendor.objects.get(id=vendor_id)
    except Vendor.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = VendorSerializer(vendor, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        vendor.delete()
        return Response({'message': 'Vendor deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET', 'POST'])
def purchase_order(request):
    if request.method == 'GET':
        obj = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(obj, many=True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = PurchaseOrderSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

@api_view(['GET', 'PUT', 'DELETE'])
def po_update_delete(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = request.data
        serializer = PurchaseOrderSerializer(purchase_order, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        purchase_order.delete()
        return Response({'message': 'Vendor deleted'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])    
def historical_performance(request):
    if request.method == 'GET':
        historical_performances = HistoricalPerformance.objects.all()
        serializer = HistoricalPerformanceSerializer(historical_performances, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = HistoricalPerformanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def vendor_performance(request, vendor_id):
    if request.method == 'GET':
        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=404)
        
        # Calculate performance metrics
        on_time_delivery_rate = vendor.on_time_delivery_rate
        quality_rating_avg = vendor.quality_rating_avg
        average_response_time = vendor.average_response_time
        fulfillment_rate = vendor.fulfillment_rate
        
        performance_data = {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfillment_rate': fulfillment_rate,
        }
        
        return Response(performance_data)



@api_view(['PATCH'])
def acknowledge_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(id=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase order not found'}, status=404)
    
    if request.method == 'PATCH':
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        purchase_order.vendor.average_response_time
        purchase_order.vendor.save()
        return Response({'message': 'Purchase order acknowledged'})



