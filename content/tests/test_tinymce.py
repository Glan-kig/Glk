import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_create_article_with_tinymce_html() -> None:
    client: APIClient = APIClient()
    user: User = User.objects.create_user(username='editoruser', password='editorpass', role='editor')
    client.force_authenticate(user=user)

    html_content = "<p>This is a <strong>test article</strong> with <em>HTML</em> content.</p>"
    response = client.post('/api/articles/', {
        'title': 'Test Article with TinyMCE', 
        'content': html_content, 
        'author': user.id
    }, format='json')
    
    assert response.status_code == 201
    assert response.data['title'] == 'Test Article with TinyMCE'
    assert response.data['content'] == html_content
    assert response.data['author'] == user.id
    assert '<p>' in response.data['content']
    assert '<em>' in response.data['content']