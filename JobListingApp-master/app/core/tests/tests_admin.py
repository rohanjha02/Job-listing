from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    """
    1) make sure user is logged into our client .
    2) user is listed in change:list in django admin panel .
    3) admin can see list of registered users .
    """
    def setUp(self):
        """
         Used to login admin user and create a normal user every time we run this test .
         """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@admin.com',
            password='password123',
            phone_number='07016396408',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='password123',
            phone_number='07016396408',
            name='Test User'
        )

    def test_for_users_listed(self):
        """
         Test that users are listed on user page 
        """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.phone_number)

    def test_user_change_page(self):
        """ Test that the user edit page works """
        url = reverse('admin:core_user_change',args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)

    def test_create_user_page(self):
        """ Test that create user page works """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        
        self.assertEqual(res.status_code,200)

