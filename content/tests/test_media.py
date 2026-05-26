import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from content.models import Media

User = get_user_model()

@pytest.mark.django_db
def test_upload_media() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='editoruser', password='editorpass', role='editor')
    client.force_authenticate(user=user)

    file = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
    response = client.post('/api/media/', {'file' : file, 'uploaded_by': user.id}, format='multipart')
    assert response.status_code == 201
    assert "file" in response.data
    assert response.data['uploaded_by'] == user.id

@pytest.mark.django_db
def test_author_cannot_upload_media() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='authoruser', password='authorpass', role='author')
    client.force_authenticate(user=user)

    file = SimpleUploadedFile("unauthorized.jpg", b"file_content", content_type="image/jpeg")
    response = client.post('/api/media/', {'file' : file, 'uploaded_by': user.id}, format='multipart')
    assert response.status_code == 403