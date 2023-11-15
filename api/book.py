from rest_framework import serializers, viewsets
from django_filters import rest_framework as filters
from app.models import Book, Publisher, User


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "publisher",
            "author",
        ]


class Filters(filters.FilterSet):
    publisher = filters.ModelMultipleChoiceFilter(
        queryset=Publisher.objects.all(),
        method="publisher_filter",
    )

    def publisher_filter(self, queryset, name, value):
        # if not value:
        #     return queryset
        return queryset.filter(publisher__in=value)

    author = filters.ModelMultipleChoiceFilter(
        queryset=User.objects.all(),
        method="author_filter",
    )

    def author_filter(self, queryset, name, value):
        # if not value:
        #     return queryset
        return queryset.filter(author__in=value)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Serializer
    filterset_class = Filters
