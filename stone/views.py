from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Tree
from .forms import TreeForm


def forest(request):
    forest = Tree.objects.all()
    return render(request, "forest.html", {'trees': forest})

def addtree(request):
    if request.method == "POST":
        form = TreeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(forest)
    else:
        form = TreeForm()

        # new_tree = Tree()
        # new_tree.name = request.POST.get("name")
        # new_tree.genus = request.POST.get("genus")
        # new_tree.species = request.POST.get("species")
        # new_tree.native = True if request.POST.get("native") == "on" else False
        # new_tree.conifer = True if request.POST.get("conifer") == "on" else False
        # new_tree.save()

    return render(request, "addtree.html", {'form': form})

def edittree(request, tree_id):
    tree = get_object_or_404(Tree, pk=tree_id)
    if request.method == "POST":
        form = TreeForm(request.POST, instance = tree)
        if form.is_valid():
            form.save()
            return redirect(forest)
    else:
        form = TreeForm(instance = tree)

    


   
    return render(request, "edittree.html", {'form': form})

