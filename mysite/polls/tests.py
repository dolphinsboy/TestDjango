from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Question


class QuestionMethodTest(TestCase):
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        f_q = Question(question="CCC", pub_date=time)
        self.assertEqual(f_q.was_published_recently(), False)