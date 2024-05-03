# vendor_management_system_django
A Vendor Management System (VMS) built using Django and Django REST Framework. This system manages vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Features

1. Vendor Profile Management:

    - Create, retrieve, update, and delete vendor profiles.
    - Calculate and display vendor performance metrics.
    
2. Purchase Order Tracking:

    - Create, retrieve, update, and delete purchase orders.
    - Track delivery status, items, quantity, and other details.
      
3. Vendor Performance Evaluation:

    - Calculate performance metrics, including on-time delivery rate, quality rating average, average response time, and fulfillment rate.
    - Historical performance tracking for trend analysis.
  

## Technical Requirements

- Django (latest stable version)
- Django REST Framework (latest stable version)
- Comprehensive data validations
- Django ORM for database interactions
- Token-based authentication
- PEP 8 compliant code


## Installation

1. Create and activate a virtual environment:

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

2. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

3. Run migrations:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

4. Run :

```bash
python manage.py runserver
```


## API

```bash 
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/vendors/ 
http://127.0.0.1:8000/api/vendors/<int:vendor_id>/ 
http://127.0.0.1:8000/api/purchase_orders/
http://127.0.0.1:8000/api/purchase_orders/<int:po_id>/ 
http://127.0.0.1:8000/api/historical_performance/ 
http://127.0.0.1:8000/api/vendors/<int:vendor_id>/performance/ 
http://127.0.0.1:8000/api/purchase_orders/<int:po_id>/acknowledge/
```


## API Documentation

Detailed API documentation is available in the `API Documentation` file. Please refer to this documentation for detailed information about each API endpoint, including input parameters, authentication requirements, and response formats.

  ```bash
  Sample JSON for Creating a New Vendor
  {
  "name": "Sample Vendor",
  "contact_details": "123-456-7890",
  "address": "456 Main St, City",
  "vendor_code": "SAMPLE123",
  "on_time_delivery_rate": 95.0,
  "quality_rating_avg": 4.5,
  "average_response_time": 2.5,
  "fulfillment_rate": 98.0
  }
  
  Sample JSON for Acknowledging a Purchase Order Create a file named acknowledge_purchase_order.json with the following content:
  
  json  
  
  {
  "acknowledgment_date": "2024-05-03T18:15:32.414971Z"
  }
  ```


## Endpoints

1. Vendor Endpoints

- Create a new vendor:

    ```bash
    URL: POST /api/vendors/ Payload Example:
   
    json
    {
        "name": "Vendor Name",
        "contact_details": "Contact Information",
        "address": "Vendor Address",
        "vendor_code": "ABC123"
    }
    ```
    *Authentication: Token-based authentication required.

- List all vendors:

    ```bash
    URL: GET /api/vendors/
    ```
    *Authentication: Token-based authentication required.
    
- Retrieve specific details of a vendor:

    ```bash
    URL: GET /api/vendors/{vendor_id}/
    ```
    *Authentication: Token-based authentication required.
    
- Update a vendor's details:

    ```bash
    URL: PUT /api/vendors/{vendor_id}/
    Payload Example:
    
    json
    {
    "name": "Updated Vendor Name",
    "contact_details": "Updated Contact Information",
    "address": "Updated Vendor Address",
    "vendor_code": "ABC123"
    }
    ```
    *Authentication: Token-based authentication required.
   
- Delete a vendor:
   
   ```bash 
    URL: DELETE /api/vendors/{vendor_id}/
   ```
    *Authentication: Token-based authentication required.

- Retrieve a vendor's performance metrics:
   
   ```bash 
    URL: GET /api/vendors/{vendor_id}/performance/
   ```
    *Authentication: Token-based authentication required.

3. Purchase Order Endpoints:

- Create a new purchase order:
   
   ```bash 
    URL: POST /api/purchase_orders/
    
    Payload Example:
   
    json
    {
    "po_number": "PO123",
    "vendor": 1,
    "order_date": "2024-04-20T00:00:00Z",
    "delivery_date": "2024-05-01T00:00:00Z",
    "items": [{"name": "Item1", "quantity": 10}],
    "quantity": 10,
    "status": "pending"
    }
   ```
    *Authentication: Token-based authentication required.

- List all purchase orders:
   
   ```bash 
    URL: GET /api/purchase_orders/
   ```
    *Authentication: Token-based authentication required.
   
- Retrieve details of a specific purchase order:
   
   ```bash 
    URL: GET /api/purchase_orders/{po_id}/
   ```
    *Authentication: Token-based authentication required.
   
- Update a purchase order:
   
   ```bash 
    URL: PUT /api/purchase_orders/{po_id}/
    Payload Example:
    
    json
    {
    "status": "completed",
    "acknowledgment_date": "2024-05-03T18:15:32.414971Z"
    }
   ```
    *Authentication: Token-based authentication required.

- Delete a purchase order:

    ```bash
    URL: DELETE /api/purchase_orders/{po_id}/
    ```
    *Authentication: Token-based authentication required.
    
    
4. Acknowledge Purchase Order Endpoint

- Acknowledge a purchase order:
   
   ```bash
    URL: PATCH /api/purchase_orders/{po_id}/acknowledge/
    Payload Example:
    
    json
    {
    "acknowledgment_date": "2024-05-03T18:15:32.414971Z"
    }
    ```
    *Authentication: Token-based authentication required. Please note that you should replace {vendor_id} and {po_id} in the URLs with the actual vendor and purchase order IDs you want to interact with.

    ```bash
    Ensure you have the appropriate authentication token and include it in the request headers for endpoints that require authentication. Also, adjust the payload examples based on the actual structure and requirements of your Django application.
    ```
