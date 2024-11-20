from django.contrib import admin
from .models import Member, Group
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display=('name','gender', 'languages','groups','birth_date','bio', )
    
class GroupAdmin(admin.ModelAdmin):
    list_display=('name', 'leader', 'image')
admin.site.register(Member, MemberAdmin)
admin.site.register(Group, GroupAdmin)
