from django.contrib import admin

from .models import MemberInGroups, Expenses, DeletedGroups

admin.site.register(MemberInGroups)

admin.site.register(Expenses)

admin.site.register(DeletedGroups)

# Register your models here.
