from django.contrib import admin

from django.utils.html import format_html
from django.urls import reverse

from .models import PresenceRequest


@admin.register(PresenceRequest)
class PresenceRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_approved', 'created_at')
    fields = ['email', 'is_approved', 'created_at', ]
    readonly_fields = ('email', 'is_approved',
                       'created_at', 'approve', 'refuse',)
    actions = ['approve_bulk', 'refuse_bulk']

    def get_fields(self, request, obj):
        if obj.is_approved == None:
            return self.fields + ['approve', 'refuse']
        return self.fields

    def approve(self, request):
        return format_html("<a href='{url}'>approve</a>",
                           url=reverse('approve-request', kwargs={'request_pk': request.pk}))

    def refuse(self, request):
        return format_html("<a href='{url}'>refuse</a>",
                           url=reverse('refuse-request', kwargs={'request_pk': request.pk}))

    @admin.action(description='Approve selected requests')
    def approve_bulk(self, request, queryset):
        for obj in queryset:
            obj.approve()

    @admin.action(description='Refuse selected requests')
    def refuse_bulk(self, request, queryset):
        for obj in queryset:
            obj.refuse()
