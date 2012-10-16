from django.db import models
from django.utils.timezone import now as datetime_now
from mptt.models import MPTTModel, TreeForeignKey


class VersionedSet(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    created = models.DateTimeField(editable=False, blank=True, default=datetime_now)

    def get_items(self):
        my_sets = self.get_ancestors(include_self=True).select_related('items')

        # Successively add or remove the items from each revision to a target set.
        data = set()
        for my_set in my_sets:
            for item in my_set.items.all():
                if item.clear:
                    data.remove(item.data)
                else:
                    data.add(item.data)

        return data


class VersionedSetData(models.Model):
    versioned_set = models.ForeignKey(VersionedSet, related_name='items')
    clear = models.BooleanField(default=False)

    class Meta:
        abstract = True
