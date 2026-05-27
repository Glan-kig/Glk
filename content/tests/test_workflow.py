import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from content.models import Article

User = get_user_model()

@pytest.mark.django_db
def test_author_can_create_draft() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='authoruser', password='authorpass', role='author')
    client.force_authenticate(user=user)

    response = client.post('/api/articles/', {'title': 'Draft Article', 'content': '<p>Draft content</p>', 'author': user.id}, format='json')
    assert response.status_code == 201
    assert response.data['status'] == 'draft'

@pytest.mark.django_db
def test_author_cannot_publish() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='authoruser', password='authorpass', role='author')
    client.force_authenticate(user=user)

    article: Article = Article.objects.create(title='Draft Article', content='<p>Draft content</p>', author=user)
    response = client.post(f'/api/articles/{article.id}/publish/')
    assert response.status_code == 403

@pytest.mark.django_db
def test_editor_can_publish() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='editoruser', password='editorpass', role='editor')
    client.force_authenticate(user=user)

    article: Article = Article.objects.create(title='Draft Article', content='<p>Draft content</p>', author=user, status='draft')
    response = client.post(f'/api/articles/{article.id}/publish/')
    assert response.status_code == 200
    assert response.data['status'] == 'published'