from django.contrib import admin
from .models import Project, Donation

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'target_amount', 'end_date', 'created_at')
    search_fields = ('title', 'owner__email')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('project', 'amount', 'donated_at')
    search_fields = ('project__title',)
