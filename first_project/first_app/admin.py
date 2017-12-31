from django.contrib import admin
from first_app.models import AccessRecord,Topic,Webpage
from first_app.models import UserProfileInfo
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(UserProfileInfo)
