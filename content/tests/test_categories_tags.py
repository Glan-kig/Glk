import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from content.models import Category, Tag

User = get_user_model()

@pytest.mark.django_db
def test_create_category() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='editoruser', password='editorpass', role='editor')
    client.force_authenticate(user=user)

    response = client.post('/api/categories/', {'name': 'Test Category'}, format='json')
    assert response.status_code == 201
    assert response.data['name'] == 'Test Category'

@pytest.mark.django_db
def test_create_tag() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='editoruser', password='editorpass', role='editor')
    client.force_authenticate(user=user)

    response = client.post('/api/tags/', {'name': 'Test Tag'}, format='json')
    assert response.status_code == 201
    assert response.data['name'] == 'Test Tag'

@pytest.mark.django_db
def test_author_cannot_create_category() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='authoruser', password='authorpass', role='author')
    client.force_authenticate(user=user)

    response = client.post('/api/categories/', {'name': 'Unauthorized Category'}, format='json')
    assert response.status_code == 403

@pytest.mark.django_db
def test_author_cannot_create_tag() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='authoruser', password='authorpass', role='author')
    client.force_authenticate(user=user)

    response = client.post('/api/tags/', {'name': 'Unauthorized Tag'}, format='json')
    assert response.status_code == 403