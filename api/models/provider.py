from django.db import models

from api.models.common import Status, TimestampModel, TraceableModel


class Provider(TimestampModel, TraceableModel):

    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=128)
    document_path = models.CharField(max_length=128, unique=True)
    bussiness_name = models.CharField(max_length=128)
    phone_no = models.CharField(max_length=25)
    website = models.URLField(max_length=100, null=True)
    email = models.EmailField(max_length=64)
    latitude = models.DecimalField(max_digits=25, decimal_places=17, null=True)
    longitude = models.DecimalField(max_digits=25, decimal_places=17, null=True)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)

    class Meta:
        db_table = "provider"
        indexes = [models.Index(fields=["name"]), models.Index(fields=["email"])]
