from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Question
from django.core.urlresolvers import reverse


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days)
    return Question.objects.create(question=question_text, pub_date=time)


def create_choice(question, choice_text, votes):
    return question.choice_set.create(choice_text=choice_text, votes=votes)


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
        create_question("Test", -30)
        # q = create_question("Test", -30)
        # q.save()
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], ['<Question: Test>'])

    def test_detail_view_with_all(self):
        q=create_question("Test", -30)
        response = self.client.get(reverse('polls:detail', args=(q.id,)))
        self.assertEqual(response.status_code, 200)

    def test_vote_view(self):
        q = create_question("Test", -30)
        c = create_choice(q, "choice_a", 10)
        response = self.client.post('/polls/%d/vote/' % q.id, data={'choice': c.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(c.votes, 10)


    def test_results_view(self):
        q=create_question("Test", -30)
        response = self.client.get(reverse('polls:results', args=(q.id,)))
        self.assertEqual(response.status_code, 200)