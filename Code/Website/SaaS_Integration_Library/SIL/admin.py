from django.contrib import admin
from SIL.models import User, ApiCredential, Api, Call

admin.site.register(User)
admin.site.register(Api)
admin.site.register(ApiCredential)
admin.site.register(Call)
