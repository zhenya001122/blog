import pytest

from django.test.client import Client

from posts.models import Post


class PostFactory:
    pass


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()

    def test_index(self):
        PostFactory.create_batch(5)
        response = self.client.get("/api/posts/")

        assert response.status_code == 200
        assert len(response.data) == 5