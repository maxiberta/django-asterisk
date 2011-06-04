# coding=utf-8

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core import urlresolvers
import datetime

class Call(models.Model):
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    related_object = generic.GenericForeignKey()

    created = models.DateTimeField(auto_now_add=True)
    extension = models.CharField(max_length=80) # Destination extension (string, 80 characters)
    context = models.CharField(max_length=80) # Destination context (string, 80 characters)
    caller_id = models.CharField(max_length=80) # Caller*ID with text (80 characters)
    channel = models.CharField(max_length=80) # Channel used (80 characters)
    response = models.CharField(max_length=80, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True) # Start of call (date/time)
    duration = models.PositiveIntegerField(null=True, blank=True) # Total time in system, in seconds (integer)
    cause = models.PositiveIntegerField(null=True, blank=True)
    disposition = models.CharField(max_length=80, null=True, blank=True) # What happened to the call: ANSWERED, NO ANSWER, BUSY, FAILED

    def get_absolute_url(self):
	return urlresolvers.reverse('admin:%s_%s_change' %(self._meta.app_label, self._meta.module_name), args=[self.id])

