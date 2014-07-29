"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.utils import override_settings
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now


from notifications import notify
from notifications.models import Notification
from notifications.utils import py_str


class NotificationTest(TestCase):

    def setUp(self):
        settings.USE_TZ = True

    @override_settings(USE_TZ=True)
    @override_settings(TIME_ZONE='Asia/Shanghai')
    def test_use_timezone(self):
        from_user = User.objects.create(username="from", password="pwd", email="example@example.com")
        to_user = User.objects.create(username="to", password="pwd", email="example@example.com")
        notify.send(from_user, recipient=to_user, verb='commented', action_object=from_user)
        notification = Notification.objects.get(recipient=to_user)
        delta = now() - notification.timestamp
        self.assertTrue(delta.seconds < 60)

    @override_settings(USE_TZ=False)
    @override_settings(TIME_ZONE='Asia/Shanghai')
    def test_disable_timezone(self):
        from_user = User.objects.create(username="from2", password="pwd", email="example@example.com")
        to_user = User.objects.create(username="to2", password="pwd", email="example@example.com")
        notify.send(from_user, recipient=to_user, verb='commented', action_object=from_user)
        notification = Notification.objects.get(recipient=to_user)
        delta = now() - notification.timestamp
        self.assertTrue(delta.seconds < 60)

    def test_utf8(self):
        ustr = u"\N{SNOWMAN}"
        from_user = User.objects.create(username="from", password="pwd", email="example@example.com")
        to_user = User.objects.create(username="to2", password="pwd", email="example@example.com")
        notify.send(from_user, verb="unicode'd " + ustr, recipient=to_user)
        notification = Notification.objects.get(recipient=to_user)
        self.assertIn(ustr, py_str(notification))
