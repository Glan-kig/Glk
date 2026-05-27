import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_create_article() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='editoruser', password='editorpass', role='editor')
    client.force_authenticate(user=user)

    response = client.post('/api/articles/', {'title': 'Test Article', 'content': 'This is a test article.', 'author': user.id}, format='json')
    assert response.status_code == 201
    assert response.data['title'] == 'Test Article'
    assert response.data['content'] == 'This is a test article.'
    assert response.data['author'] == user.id

@pytest.mark.django_db
def test_article_permissions() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='authoruser', password='authorpass', role='subscriber')
    client.force_authenticate(user=user)

    response = client.post('/api/articles/', {'title': 'Unauthorized Article', 'content': 'This should not be created.', 'status': 'published', 'author': user.id}, format='json')
    assert response.status_code == 403

@pytest.mark.django_db
def test_publish_permission() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='authoruser', password='authorpass', role='author')
    client.force_authenticate(user=user)

    article_response = client.post('/api/articles/', {'title': 'Draft Article', 'content': 'This is a draft article.', 'author': user.id}, format='json')
    article_id = article_response.data['id']

    publish_response = client.post(f'/api/articles/{article_id}/publish/')
    assert publish_response.status_code == 403