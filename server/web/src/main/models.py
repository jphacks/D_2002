from django.db import models
from stdimage.models import StdImageField
from stdimage.validators import MinSizeValidator, MaxSizeValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=100,
        blank=False,
        null=False)

    amount = models.IntegerField(
        verbose_name='amount',
        blank=True,
        null=True)

    price = models.IntegerField(
        verbose_name='price',
        blank=False,
        null=False)
    
    image = StdImageField(
        verbose_name='image',
        upload_to="product",
        validators=[MinSizeValidator(300, 300), MaxSizeValidator(5760, 3840)],
        blank=True,
        variations={
            'medium': (500, 500, True),
            'small': (300, 300, True),
        },
    )

    abi = models.CharField(
        verbose_name='name',
        max_length=1000,
        blank=False,
        null=False)

    tx_hash = models.CharField(
        verbose_name='name',
        max_length=2000,
        blank=False,
        null=False)


    def __str__(self):
        return self.name