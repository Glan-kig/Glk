import pytest
from django.contrib.auth import get_user_model


User = get_user_model()

@pytest.mark.django_db
def test_user_creation() -> None:
    user: User = User.objects.create_user(username='testuser', password='testpass', role='author')
    assert user.username == 'testuser'
    assert user.role == 'author'
    assert user.check_password('testpass')

@pytest.mark.django_db
def test_admin_role() -> None:
    admin: User = User.objects.create_user(username='adminuser', password='adminpass', role='admin')
    assert admin.role == 'admin'
    assert admin.is_authenticated is True