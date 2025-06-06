from rest_framework import serializers
from .models import BillingRecord, Invoice, Payment

class BillingSerializer(serializers.ModelSerializer):

    patient = serializers.StringRelatedField()
    date_of_service = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = BillingRecord
        # fields = '__all__'
        fields = ['id','patient','service_description','amount','date_of_service']

class InvoiceSerializer(serializers.ModelSerializer):

    patient = serializers.StringRelatedField()
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Invoice
        # fields = '__all__'
        fields = ['id','patient','total_amount','status','date_created']

class PaymentSerializer(serializers.ModelSerializer):

    invoice = serializers.StringRelatedField()
    date_paid = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Payment
        # fields = '__all__'
        fields = ['id','invoice', 'date_paid', 'payment_method']