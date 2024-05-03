from django.urls import path
from .views import vendors, vendors_update_delete, purchase_order, po_update_delete, historical_performance, acknowledge_purchase_order, vendor_performance

urlpatterns = [
    path('api/vendors/', vendors),
    path('api/vendors/<int:vendor_id>/', vendors_update_delete),
    path('api/purchase_orders/', purchase_order),
    path('api/purchase_orders/<int:po_id>/', po_update_delete),
    path('api/historical_performance/', historical_performance),
    path('api/vendors/<int:vendor_id>/performance/', vendor_performance),
    path('api/purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order),
]
