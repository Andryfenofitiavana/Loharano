from django.shortcuts import render, get_object_or_404
from item.models import Entambarotra
from django.contrib.auth.decorators import login_required

   
@login_required
def index(request):
    items = Entambarotra.objects.filter(mpivarotra=request.user)
    return render(request, 'dashboard/index.html', {
        'items': items,
    })
# Create your views here.
