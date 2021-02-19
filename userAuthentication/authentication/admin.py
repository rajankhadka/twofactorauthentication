from django.contrib import admin

from authentication.models import PhoneNumber, OTPCode

admin.site.register(PhoneNumber)
admin.site.register(OTPCode)
