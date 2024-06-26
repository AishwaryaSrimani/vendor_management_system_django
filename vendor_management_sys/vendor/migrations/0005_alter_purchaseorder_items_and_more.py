# Generated by Django 5.0.4 on 2024-05-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendor", "0004_alter_purchaseorder_po_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseorder", name="items", field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name="purchaseorder", name="order_date", field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="contact_details",
            field=models.TextField(max_length=255),
        ),
    ]
