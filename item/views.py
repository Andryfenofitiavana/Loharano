from django.shortcuts import render, get_object_or_404, redirect
from .models import Entambarotra, Sokajy
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, FormEdit
from django.db.models import Q

def detail(request, pk):
    item = get_object_or_404(Entambarotra, pk=pk)
    related_items = Entambarotra.objects.filter(sokajy=item.sokajy, lafo_ve=False).exclude(pk=pk)[0:10]
    return render(request, 'item/detail.html', {
        'item' : item,
        'related_items': related_items,
    })

def browse(request):
    category_id = request.GET.get('category', 0)
    query = request.GET.get('query','')
    sokajy = Sokajy.objects.all()
    items = Entambarotra.objects.filter(lafo_ve=False)
    if query:
        items = items.filter(Q(anarana__icontains=query) | Q(fanazavana__icontains=query))
    if category_id:
        items = items.filter(sokajy_id = category_id)
    return render(request, 'item/browse.html', {
        'items':items,
        'query':query,
        'sokajy':sokajy,
        'category_id':int (category_id),
    })
    
@login_required
def delete(request, pk):
    item = get_object_or_404(Entambarotra, pk=pk, mpivarotra = request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.mpivarotra = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, 'item/form.html', {
        'form' : form,
        'title' : 'Entana vaovao',
    })
    

@login_required
def edit(request, pk):
    item = get_object_or_404(Entambarotra, pk=pk, mpivarotra = request.user)
    if request.method == 'POST':
        form = FormEdit(request.POST, request.FILES, instance=item)
        if form.is_valid():
           form.save()
           return redirect('item:detail', pk=item.id)
    else:
        form = FormEdit(instance=item)
    return render(request, 'item/form.html', {
        'form' : form,
        'title' : 'Hanova entana',
    })