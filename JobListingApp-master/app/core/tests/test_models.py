from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_and_mobile_number_successful(self):
        """
        Test user is created with fields email,password and phone number .
        """
        email = "vrushangdev@gmail.com"
        password = "Testpass@123"
        phone_number="0917016396408"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            phone_number=phone_number,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.phone_number,phone_number)

    def test_new_user_email_is_normalized(self):
        """ 
        Test the email for user is normalized
        """
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises value error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def test_new_user_invalid_phone_number(self):
        """
        Test creating new user witth no phone number raises value error .
        """
        email = "vrushangdev@gmail.com"
        password = "Testpass@123"
        phone_number="0917016396408"

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
            email=email,
            password=password,
            phone_number=None,
                )


    def test_create_new_super_user(self):
        """
        Test creating a new super user
        """
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            '07016396408',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertEqual('07016396408',user.phone_number)
