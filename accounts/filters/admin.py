import django_filters
from accounts.models.admin import Admin


class AdminFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    email = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    first_name = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")
    last_name = django_filters.CharFilter(field_name="user__username", lookup_expr="icontains")

    class Meta:
        model = Admin
        fields = ["username", "email", "first_name", "last_name"]
