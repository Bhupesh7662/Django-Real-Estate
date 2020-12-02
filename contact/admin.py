from django.contrib import admin
from .models import Contact, Inquiry


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'inquiry_name', 'property_detail', 'inquiry_email', 'inquiry_date')
    list_display_links = ('id', 'inquiry_name')
    search_fields = ('inquiry_name', 'inquiry_email', 'property_detail')
    list_per_page = 25

admin.site.register(Contact)
admin.site.register(Inquiry, InquiryAdmin)
