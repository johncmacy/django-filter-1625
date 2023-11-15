import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.test_settings")
django.setup()

from django.test import TestCase
from rest_framework.test import APITestCase
from app.models import Book, Publisher, User


class BookTestCase(APITestCase):
    @classmethod
    def create_user(cls, username, password):
        user = User.objects.create(username=username)
        user.set_password(password)
        return user

    @classmethod
    def setUpTestData(cls):
        cls.author = cls.create_user("user1", "password")

        cls.publisher = Publisher.objects.create(name="Pub 1")

        Book.objects.create(
            title="Book",
            description="About something",
            publisher=cls.publisher,
            author=cls.author,
        )

    def test_no_filters_submitted(self):
        response = self.client.get("/api/book/")

        self.assertEquals(len(response.json()), 1)

    def test_with_publisher_filter(self):
        response = self.client.get("/api/book/", {"publisher": self.publisher.pk})

        self.assertEquals(len(response.json()), 1)

    def test_with_author_filter(self):
        response = self.client.get("/api/book/", {"author": self.author.pk})

        self.assertEquals(len(response.json()), 1)

    def test_with_publisher_and_author_filters(self):
        response = self.client.get(
            "/api/book/",
            {
                "publisher": self.publisher.pk,
                "author": self.author.pk,
            },
        )

        self.assertEquals(len(response.json()), 1)
