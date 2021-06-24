from django.db import models
from django.shortcuts import render
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(MPTTModel):
    STATUS = (
        ('true', 'True'),
        ('false', 'False'),
        ('splitter32', 'Splitter32'),
        ('splitter2', 'Splitter2')
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=255)
    gps = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    sn = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Splitter(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=150)


# Create your models here.
class Customer(MPTTModel):
    STATUS = (
        ('true', 'True'),
        ('false', 'False')
    )
    splitter32 = models.ForeignKey(Category, on_delete=models.CASCADE,
                                   blank=True, null=True, related_name='category')
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    gps = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=150, blank=True, null=True)
    ont = models.CharField(max_length=150, blank=True, null=True)
    service_id = models.CharField(max_length=150, blank=True, null=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.address

    def get_absolute_url(self):
        return reverse('show_customers', kwargs={'pk': self.pk})


def home(request):
    return render(request, 'home.html')


class Snippet(MPTTModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)
