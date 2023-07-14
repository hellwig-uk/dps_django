"""
Base models to be used by multiple apps.
"""

from django.db import models
from django.db.models import BigAutoField, DateTimeField, Q
from django.utils.timezone import now


class Manager(models.Manager):
    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .filter(
                Q(dts_archived__gt=now()) | Q(dts_archived__isnull=True),
            )
        )
        return queryset


class Model(models.Model):
    rid = BigAutoField(primary_key=True)
    dts_inserted = DateTimeField(
        verbose_name="DTS Inserted",
        auto_now_add=True,
    )
    dts_modified = DateTimeField(
        verbose_name="DTS Modified",
        auto_now=True,
    )
    dts_archived = DateTimeField(
        verbose_name="DTS Archived",
        null=True,
        editable=False,
    )

    objects = Manager()
    objects_with_archived = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False, no_archive=False):
        if no_archive:
            return super().delete(using, keep_parents)

        self.dts_archived = now()
        self.save()
        return True
