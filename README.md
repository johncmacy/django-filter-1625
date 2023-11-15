# django-filter-1625

Demonstrates the issue reported in [django-filter issue #1625](https://github.com/carltongibson/django-filter/issues/1625).

The `book` API is configured with filters for `publisher` and `author`, both of which are `ModelMultipleChoiceFilter`s.

The following tests demonstrate the unexpected behavior. With the filter methods like this, 3 of the 4 tests fail:

``` py
    def publisher_filter(self, queryset, name, value):
        return queryset.filter(publisher__in=value)
```

- test_no_filters_submitted (fail)
- test_with_publisher_filter (fail)
- test_with_author_filter (fail)
- test_with_publisher_and_author_filters (pass)

After adding the following if statement to both publisher and author filters, all four tests pass:

``` py
    def publisher_filter(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(publisher__in=value)
```
