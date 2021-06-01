import django_filters
from .models import Customer


class CustomerFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')



    def filter_by_order(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)
