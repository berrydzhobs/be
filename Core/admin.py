from django.contrib import admin
from .models import Offer_request, Message, Payment_method, Email_list

admin.site.register(Offer_request)
admin.site.register(Message)
admin.site.register(Payment_method)
admin.site.register(Email_list)