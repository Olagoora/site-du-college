from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from application.models import Content
from .forms import ContentForm

# Create your views here.
# @staff_member_required
def content_create(request):

    if request.method == "POST":
        form = ContentForm(request.POST)

        if form.is_valid():
            content = form.save(commit=False)
            content.save(using="dynamic")

            return redirect(
                "spip",
                id=content.rubrique_id
            )

    else:
        form = ContentForm()

    return render(
        request,
        "form/content_form.html",
        {
            "form": form,
        }
    )

# @staff_member_required
def content_delete(request, id):

    content = get_object_or_404(
        Content.objects.using("dynamic"),
        id=id
    )

    if request.method == "POST":

        rubrique_id = content.rubrique_id

        content.delete(using="dynamic")

        return redirect(
            "spip",
            id=rubrique_id
        )

    return render(
        request,
        "form/content_delete.html",
        {
            "content": content,
        }
    )