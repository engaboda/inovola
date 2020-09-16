from django.db import models


# Create your models here.
class CoffeeMachine(models.Model):
    """
        · Product type – product_type
        o COFFEE_MACHINE_LARGE
        o COFFEE_MACHINE_SMALL
        o ESPRESSO_MACHINE
        · Water line – water_line_compatible
        o true
        o false
    """
    PRODUCT_TYPE = (
        ('l', 'COFFEE_MACHINE_LARGE'),
        ('s', 'COFFEE_MACHINE_SMALL'),
        ('e', 'ESPRESSO_MACHINE')
    )

    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=1)
    water_line_compatible = models.BooleanField(default=True)

    def __str__(self):
        return "product_type: {} water_line_compatible: {}".format(self.get_product_type_display(), self.get_water_line_compatible_display())


class CoffeePods(models.Model):
    """
        · Product type – product_type
        o COFFEE_POD_LARGE
        o COFFEE_POD_SMALL
        o ESPRESSO_POD
        ·Coffee flavor – coffee_flavor
        o COFFEE_FLAVOR_VANILLA
        o COFFEE_FLAVOR_CARAMEL
        o COFFEE_FLAVOR_PSL
        o COFFEE_FLAVOR_MOCHA
        o COFFEE_FLAVOR_HAZELNUT
        · Pack size – pack_size
        o 1 dozen (12)
        o 3 dozen (36)
        o 5 dozen (60)
        o 7 dozen (84)
    """
    PRODUCT_TYPE = (
        ('l', 'COFFEE_POD_LARGE'),
        ('s', 'COFFEE_POD_SMALL'),
        ('e', 'ESPRESSO_POD')
    )

    PACK_SIZE = (
        ('1', '1 dozen (12)'),
        ('3', '3 dozen (36)'),
        ('5', '5 dozen (60)'),
        ('7', '7 dozen (84)')
    )

    COFFEE_FLAVER = (
        ('v', 'COFFEE_FLAVOR_VANILLA'),
        ('c', 'COFFEE_FLAVOR_CARAMEL'),
        ('p', 'COFFEE_FLAVOR_PSL'),
        ('m', 'COFFEE_FLAVOR_MOCHA'),
        ('h', 'COFFEE_FLAVOR_HAZELNUT'),
    )

    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=1)
    coffee_flavor = models.CharField(choices=COFFEE_FLAVER, max_length=1)
    pack_size = models.CharField(choices=PACK_SIZE, max_length=1)

    def __str__(self):
        return "{} {}".format(self.get_PRODUCT_TYPE_display(), self.get_PACKET_SIZE_display(), self.get_COFFEE_FLAVER_display())
