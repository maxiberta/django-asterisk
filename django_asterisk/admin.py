# coding=utf-8

from django.contrib import admin
from models import Call

class CallAdmin(admin.ModelAdmin):
    model = Call
    list_display = ['id', 'channel', 'context', 'caller_id', 'created', 'start', 'duration', 'response', 'cause', 'disposition', 'related_object']
    list_display_links = ['id', 'channel']
    list_filter = ('response', 'cause', 'disposition', 'context',)
    search_fields = ('channel',)
    date_hierarchy = 'start'
    actions = ['make_call']
    def lookup_allowed(self, lookup, value=None):
        return True
    def related_object(self, obj):
        from django.utils.safestring import mark_safe
        return mark_safe('%s <sup><a href="%s">Link</a></sup>' % (obj.related_object, obj.related_object.get_absolute_url()))
    related_object.allow_tags = True
    def make_call(self, request, queryset):
        from engine import call_all
        answered, not_answered, errors = call_all(queryset.all())
        self.message_user(request, "%s answered; %s not answered; %s error" % (answered, not_answered, errors))
    make_call.short_description = u'Make call'

admin.site.register(Call, CallAdmin)
