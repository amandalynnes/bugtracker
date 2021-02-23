from django.shortcuts import render, HttpResponseRedirect
from django.utils import timezone
from .forms import CustomUserForm
from .models import TicketItem, CustomUser

# Create your views here.

def index_view(request):
    tickets = TicketItem.objects.all().order_by('dt_filed').reverse()

    return render(request, 'index.html', {
        'heading': 'Get Your Tickets Here, Get Your Tickets!',
        'tickets': tickets})