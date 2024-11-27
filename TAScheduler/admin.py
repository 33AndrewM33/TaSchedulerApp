from django.contrib import admin
from TAScheduler.models import User, Supervisor, TA, Instructor, Course, Section, Lab, Lecture

admin.site.register(User)
admin.site.register(Supervisor)
admin.site.register(TA)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lab)
admin.site.register(Lecture)
admin.site.register(Admin)