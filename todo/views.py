from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from .models import TodoItem


@require_GET
def index(request):
    items = TodoItem.objects.all()
    return render(request, "todo/index.html", {"items": items})


@require_POST
def add_item(request):
    title = request.POST.get("title", "").strip()
    if title:
        TodoItem.objects.create(title=title)
    return redirect("todo:index")


@require_GET
def health(request):
    return JsonResponse({"status": "ok", "app": "demo-django-app"})