from django.test import TestCase
from TAScheduler.models import User
from django.core.exceptions import ValidationError

class UserModelTests(TestCase):

    def test_create_user(self):
        user = User.objects.create(
            username="testuser",
            email="testuser@example.com",  # Corrected to 'email'
            password="password123",
            first_name="Test",
            last_name="User",
            is_admin=False,
            is_instructor=False,
            is_ta=True
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")  # Corrected to 'email'
        self.assertTrue(user.is_ta)
        self.assertFalse(user.is_admin)

    def test_get_role_admin(self):
        user = User.objects.create(
            username="adminuser",
            email="admin@example.com",  # Corrected to 'email'
            password="password123",
            is_admin=True
        )
        self.assertEqual(user.get_role(), "Administrator")

    def test_create_user_with_missing_email(self):
        user = User(
            username="testuser",
            password="password123"
        )
        # Validate the model, expecting a ValidationError
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_create_user_with_missing_username(self):
        user = User(
            email="testuser@example.com",  # Corrected to 'email'
            password="password123"
        )
        # Validate the model, expecting a ValidationError
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_get_role_instructor(self):
        user = User.objects.create(
            username="instructor",
            email="instructor@example.com",  # Corrected to 'email'
            password="password123",
            is_instructor=True
        )
        self.assertEqual(user.get_role(), "Instructor")

    def test_get_role_ta(self):
        user = User.objects.create(
            username="tauser",
            email="ta@example.com",  # Corrected to 'email'
            password="password123",
            is_ta=True
        )
        self.assertEqual(user.get_role(), "TA")

    def test_get_role_no_role(self):
        user = User.objects.create(
            username="norole",
            email="norole@example.com",  # Corrected to 'email'
            password="password123"
        )
        self.assertEqual(user.get_role(), "No Role")

    def test_user_str_method(self):
        user = User.objects.create(
            username="testuser",
            email="testuser@example.com",  # Corrected to 'email'
            password="password123",
            first_name="Test",
            last_name="User"
        )
        self.assertEqual(str(user), "Test User (testuser@example.com)")  # Corrected to 'email'
