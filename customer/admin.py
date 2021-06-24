from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category, Customer, Splitter

app_name = Customer


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ('name', 'parent', 'sn')
    sortable_by = 'sn'
    list_filter = ['status']


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_name',
                    'related_customer_count', 'related_customer_cumulative_count')
    list_display_links = ('indented_name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(
            qs,
            Customer,
            'category',
            'customer__cumulative_count',
            cumulative=False
        )
        return qs

    def related_customer_count(self, instance):
        return instance.customer_count

    related_customer_count.short_description = 'Related customer (for this specific category)'

    def related_customer_cumulative_count(self, instance):
        return instance.customer_cumulative_count

    related_customer_cumulative_count.short_description = 'Related customer (in tree)'

    def filter_tree_queryset(self, queryset):
        return queryset.filter(name='abc')

    def is_drag_and_drop_enabled(self):
        return False


class SplitterAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    list_filter = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'splitter32']
    list_filter = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Splitter, SplitterAdmin)
