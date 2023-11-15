from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import book

router = DefaultRouter()

router.register("book", book.BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
