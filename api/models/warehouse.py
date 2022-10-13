from django.core.validators import MinValueValidator
from django.db import models

from .common import Status, TimestampModel
from .items import Item
from .users import Employee


class Warehouse(TimestampModel):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=128)

    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)

    status = models.ForeignKey(Status, on_delete=models.RESTRICT)

    def __str__(self):
        return f"Warehouse '{self.name}'"

    class Meta:
        db_table = "warehouse"
        indexes = [
            models.Index(fields=["name"]),
        ]


class Inventory(TimestampModel):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)

    warehouse = models.ForeignKey(Warehouse, on_delete=models.RESTRICT)
    item = models.ForeignKey(Item, on_delete=models.RESTRICT)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    delete_at = None

    updated_by = models.ForeignKey(Employee, on_delete=models.RESTRICT)

    def __str__(self):
        return f"Inventory of '{self.warehouse.name}'"

    class Meta:
        db_table = "inventory"

    def nombreItem(self):
        return self.item.name

    def created_at_Item(self):
        return self.item.created_at

    def brandItem(self):
        return self.item.brand

    def imgItem(self):
        return self.item.img.name
        # imgItem

    def ivaItem(self):
        return self.item.iva

    def modelItem(self):
        return self.item.model

    def priceItem(self):
        return self.item.price

    def category_id_Item(self):
        return self.item.category_id

    def category_name_Item(self):
        return self.item.category.name

    def created_by_Item(self):
        return {
            "created_by": self.item.created_by.id,
            "name": self.item.created_by.name,
            "lastname": self.item.created_by.lastname,
        }

    def status_id_Item(self):
        return self.item.status_id

    def codename_Item(self):
        return self.item.codename


class WarehouseTransaction(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    notes = models.CharField(max_length=300, blank=True)
    warehouse_origin = models.ForeignKey(
        Warehouse, on_delete=models.RESTRICT, related_name="origin"
    )
    warehouse_destiny = models.ForeignKey(
        Warehouse, on_delete=models.RESTRICT, related_name="destiny"
    )
    created_by = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.RESTRICT)

    class Meta:
        db_table = "warehouse_transaction"


class WhTransactionDetails(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    header = models.ForeignKey(WarehouseTransaction, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.RESTRICT)
    quantity = models.IntegerField()

    class Meta:
        db_table = "wh_transaction_details"
