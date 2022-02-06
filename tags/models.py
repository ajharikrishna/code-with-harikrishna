from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# This ContentType model Specically made for allowing generic relationships


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Generic way to Identify an Object To do that we need two pieces of information
    # 1.Type of object(ex: product, article etc) (for table)
    # 2.ID of object (for record)
    # Using these two pieces of information we can identify any objects in our application
    # Or In Database Terms We Can Idnetify any record In any Tables
    # Because using the type we can find the table and using the ID we can find the record
    # so we should use abstract model like ContentType
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
