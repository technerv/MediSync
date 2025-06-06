from django.contrib import admin
from .models import InsuranceCompany, InsurancePolicy, Claim

# admin.site.register(InsuranceCompany)
@admin.register(InsuranceCompany)
class InsuranceModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'email', 'address')

@admin.register(InsurancePolicy)
class InsurancePolicyModelAdmin(admin.ModelAdmin):
    list_display = ('patient', 'policy_number', 'insurance_company', 'start_date', 'end_date', 'coverage_details' )

@admin.register(Claim)
class ClaimModelAdmin(admin.ModelAdmin):
    list_display = ('insurance_policy', 'claim_number', 'date_of_claim', 'amount_claimed', 'status', 'notes')
# admin.site.register(InsurancePolicy)
# admin.site.register(Claim)