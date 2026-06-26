from django.db import models

class Shipment(models.Model):
    TRANSACTION_TYPES = [
        ('IMPORT', 'Import'),
        ('EXPORT', 'Export'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending Administration'),
        ('CUSTOMS_CLEARANCE', 'Customs Clearance'),
        ('RELEASED', 'Released/Completed'),
    ]

    bl_number = models.CharField(max_length=50, unique=True, verbose_name="Bill of Lading Number")
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    shipper = models.CharField(max_length=100)
    consignee = models.CharField(max_length=100)
    origin_port = models.CharField(max_length=100)
    destination_port = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.bl_number}"

    @property
    def total_administrative_cost(self):
        return sum(cost.amount for container in self.containers.all() for cost in container.costs.all())


class Container(models.Model):
    CONTAINER_SIZES = [
        ('20FT', '20 Feet Standard'),
        ('40FT', '40 Feet Standard'),
        ('40HC', '40 Feet High Cube'),
    ]

    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='containers')
    container_number = models.CharField(max_length=20, unique=True)
    size = models.CharField(max_length=5, choices=CONTAINER_SIZES)
    seal_number = models.CharField(max_length=50)

    def __str__(self):
        return self.container_number


class CostComponent(models.Model):
    COST_TYPES = [
        ('THC', 'Terminal Handling Charge'),
        ('DEMURRAGE', 'Demurrage Fee'),
        ('DETENTION', 'Detention Fee'),
        ('CUSTOMS_DUTY', 'Pajak / Bea Masuk'),
        ('EDI_FEE', 'Biaya EDI Dokumen'),
        ('DOCUMENTATION', 'Biaya Manifest/Dokumen'),
    ]

    container = models.ForeignKey(Container, on_delete=models.CASCADE, related_name='costs')
    cost_type = models.CharField(max_length=20, choices=COST_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)  # Diperbaiki ke max_digits
    currency = models.CharField(max_length=3, default='IDR')
    is_paid = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cost_type} - {self.amount} {self.currency}"