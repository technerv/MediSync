from rest_framework import serializers
from .models import InsuranceCompany, InsurancePolicy, Claim

class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCompany
        # fields = '__all__'
        fields = ['name', 'contact_number', 'email', 'address']

class InsurancePolicySerializer(serializers.ModelSerializer):

    insurance_company = serializers.StringRelatedField()
    patient = serializers.StringRelatedField()

    class Meta:
        model = InsurancePolicy
        # fields = '__all__'
        fields = ['id', 'patient', 'policy_number', 'start_date', 'end_date', 'coverage_details', 'insurance_company']

class ClaimSerializer(serializers.ModelSerializer):
    insurance_policy = serializers.StringRelatedField()

    class Meta:
        model = Claim
        # fields = '__all__'
        fields = ['id', 'claim_number', 'date_of_claim', 'amount_claimed', 'status', 'notes', 'insurance_policy']