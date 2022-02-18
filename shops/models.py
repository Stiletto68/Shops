from django.db import models
from django.contrib import admin


class Organization(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.CharField('Description', max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'


class TimeStampedModel(models.Model):
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Extensions(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Shop(Extensions):
    organization = models.ForeignKey(Organization, related_name='shops', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=100)
    description = models.CharField(' Description', max_length=100)
    address = models.CharField('Address', max_length=100)
    index = models.IntegerField('Index')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        unique_together = ['organization', 'index']
        ordering = ['index']
        verbose_name = 'Shop'
        verbose_name_plural = 'Shop'


class ShopInlineAdminView(admin.TabularInline):
    model = Shop
    extra = 1
    classes = ['collapse']
    fieldsets = (
        ('', {
            'fields': ('name',
                       'description',
                       'address',
                       'index',
                       'is_deleted')
        }),
    )
    allow_add = True
