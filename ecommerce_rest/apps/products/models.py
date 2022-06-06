from apps.base.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class MeasureUnit(BaseModel):

    description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("MeasureUnit")
        verbose_name_plural = _("MeasureUnits")

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):

    description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("CategoryProduct")
        verbose_name_plural = _("CategoryProducts")

    def __str__(self):
        return self.description


class Indicator(BaseModel):

    discount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("Indicator")
        verbose_name_plural = _("Indicators")

    def __str__(self):
        return f'{self.category_product} - {self.discount_value}%'


class Product(BaseModel):

    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
