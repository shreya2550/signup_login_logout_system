from django.contrib import admin
from .models import beneficiary
# Register your models here.
class beneficiaryAdmin(admin.ModelAdmin):
    list_display=('full_name','phone_number','next_renewal_date','adhar_number','validity_status')
    search_fields=('full_name','adhar_number')
admin.site.register(beneficiary,beneficiaryAdmin)