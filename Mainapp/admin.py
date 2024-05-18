from django.contrib import admin 
from .models import *
admin.site.register((Buyer,Worker,Category,Servicebook,Contact,Feedback))

# Register your models here.
