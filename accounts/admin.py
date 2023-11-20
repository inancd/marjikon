from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PersonalInfo

admin.site.unregister(Group)
class PersonalInfoInline(admin.StackedInline):
    model = PersonalInfo
    can_delete = False
    verbose_name_plural = 'Kişisel Bilgiler'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (PersonalInfoInline, )
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_seller')
    search_fields = ('email',)
    ordering = ('email',)

    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_seller')}),
      
    )

    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(CustomUser, CustomUserAdmin)
