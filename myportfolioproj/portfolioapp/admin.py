from django.contrib import admin

from .models import MyDetails, About, Services, Projects, Testimonials #AboutProfile


admin.site.register(MyDetails)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(Testimonials)
# admin.site.register(AboutProfile)
