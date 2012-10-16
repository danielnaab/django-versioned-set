from django.db import models

from versioned_set.models import VersionedSetData


class VersionedSetTestData(VersionedSetData):
    data = models.IntegerField()
