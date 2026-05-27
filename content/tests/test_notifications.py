import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from content.models import Article, Notification

User = get_user_model()

@pytest.mark.django_db
def test_notification_created_on_draft() -> None:
    client: APIClient = APIClient()
    author: User = User.objects.create_user(username='authoruser', password='authorpass', role='author')
    editor: User = User.objects.create_user(username='editoruser', password='editorpass', role='editor')
    client.force_authenticate(user=author)

    response = client.post('/api/articles/', {'title': 'Draft Article', 'content': '<p>Test</p>', 'author': author.id}, format='json')
    assert response.status_code == 201

    notifications = Notification.objects.filter(recipient=editor)
    assert notifications.count() == 1
    assert "Nouvel article en attente" in notifications.first().message