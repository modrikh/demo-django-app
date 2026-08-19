from django.test import TestCase
from django.urls import reverse

from .models import TodoItem


class TodoModelTests(TestCase):
    def test_creation(self):
        item = TodoItem.objects.create(title="Test")
        self.assertEqual(item.done, False)
        self.assertIsNotNone(item.created_at)


class TodoViewTests(TestCase):
    def test_index_lists_items(self):
        TodoItem.objects.create(title="Item A")
        response = self.client.get(reverse("todo:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Item A")

    def test_add_creates_item(self):
        response = self.client.post(reverse("todo:add"), {"title": "Nouveau"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TodoItem.objects.count(), 1)

    def test_add_ignores_empty(self):
        self.client.post(reverse("todo:add"), {"title": "   "})
        self.assertEqual(TodoItem.objects.count(), 0)

    def test_health(self):
        response = self.client.get(reverse("todo:health"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")