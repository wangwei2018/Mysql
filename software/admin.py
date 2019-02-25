from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Software_old)
admin.site.register(Software_imp)
admin.site.register(Software_new)
admin.site.register(Image_old)
admin.site.register(Image_imp)
admin.site.register(Image_new)
admin.site.register(SoundCode)

admin.site.unregister(User)
admin.site.register(User)



