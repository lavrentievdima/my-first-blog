from django.contrib import admin

from .models import Good, Purchases, UsersInSite, Contacts, Type


admin.site.register(Good)
admin.site.register(Purchases)
admin.site.register(UsersInSite)
admin.site.register(Contacts)
admin.site.register(Type)

