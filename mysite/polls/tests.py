from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Question
from django.core.urlresolvers import reverse


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days)
    # return Question.objects.create(question=question_text, pub_date=time)
    return Question(question=question_text, pub_date=time)


class QuestionMethodTest(TestCase):
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        f_q = Question(question="CCC", pub_date=time)
        self.assertEqual(f_q.was_published_recently(), False)

    def test_index_view_with_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_index_view_with_all(self):
        q = create_question("Test", -30)
        q.save()
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], ['<Question: Test>'])