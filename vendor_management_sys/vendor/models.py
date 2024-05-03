from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField(max_length=255)
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.po_number} - {self.vendor.name}"
    
    
    def calculate_on_time_delivery_rate(self):
        total_completed_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed').count()
        if total_completed_orders > 0:
            on_time_completed_orders = PurchaseOrder.objects.filter(
                vendor=self.vendor, status='completed', delivery_date__lte=models.F('acknowledgment_date')
            ).count()
            self.vendor.on_time_delivery_rate = (on_time_completed_orders / total_completed_orders) * 100
        else:
            self.vendor.on_time_delivery_rate = 0.0
        self.vendor.save()
    
    
    def calculate_quality_rating_avg(self):
        completed_orders = PurchaseOrder.objects.filter(
            vendor=self.vendor, status='completed', quality_rating__isnull=False
        )
        total_ratings = sum(order.quality_rating for order in completed_orders)
        total_orders = completed_orders.count()
        self.vendor.quality_rating_avg = total_ratings / total_orders if total_orders else 0.0
        self.vendor.save()


    def calculate_avg_response_time(self):
        completed_orders = PurchaseOrder.objects.filter(
            vendor=self.vendor, status='completed', acknowledgment_date__isnull=False
        )
        total_time = sum((order.acknowledgment_date - order.issue_date).total_seconds() for order in completed_orders)
        total_orders = completed_orders.count()
        self.vendor.average_response_time = total_time / total_orders if total_orders else 0.0
        self.vendor.save()
    
    def calculate_fulfillment_rate(self):
        total_orders = PurchaseOrder.objects.filter(vendor=self.vendor)
        completed_orders = total_orders.filter(status='completed')
        successful_orders = completed_orders.exclude(acknowledgment_date__isnull=True)
        self.vendor.fulfillment_rate = (successful_orders.count() / total_orders.count()) * 100 if total_orders else 0.0
        self.vendor.save()
    
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"