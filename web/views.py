from django.shortcuts import render, redirect, get_object_or_404
from .models import EmergingDJ
from .forms import DJForm, SearchForm


def create_dj(request):
    if request.method == "POST":
        form = DJForm(request.POST, request.FILES)  # Aquí agregamos request.FILES
        if form.is_valid():
            form.save()
            return redirect("create_dj")
    else:
        form = DJForm()
    return render(request, "web/create_dj.html", {"form": form})


def search_dj(request):
    if "query" in request.GET:
        query = request.GET["query"]
        results = EmergingDJ.objects.filter(dj_name__icontains=query)
        return render(request, "web/search_results.html", {"results": results})
    else:
        form = SearchForm()
    return render(request, "web/search.html", {"form": form})


def homepage(request):
    return render(request, "web/homepage.html")


def list_djs(request):
    djs = EmergingDJ.objects.all()
    return render(request, "web/list_djs.html", {"djs": djs})


def edit_dj(request, dj_id):
    dj = get_object_or_404(EmergingDJ, id=dj_id)
    if request.method == "POST":
        form = DJForm(request.POST, request.FILES, instance=dj)
        if form.is_valid():
            form.save()
            return redirect("list_djs")
    else:
        form = DJForm(instance=dj)
    return render(request, "web/edit_dj.html", {"form": form})


def delete_dj(request, dj_id):
    dj = get_object_or_404(EmergingDJ, id=dj_id)
    if request.method == "POST":
        dj.delete()
        return redirect("list_djs")
    return render(request, "web/confirm_delete.html", {"dj": dj})
