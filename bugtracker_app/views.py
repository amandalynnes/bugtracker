from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from .forms import CustomUserForm, LoginForm, TicketItemForm
from .models import TicketItem, CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def index_view(request):
    tickets = TicketItem.objects.all().order_by('dt_filed').reverse()

    return render(request, 'index.html', {
        'heading': 'Tickets, Get Your Tickets Here!',
        'tickets': tickets})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'login_view.html', {
        'heading': 'Login Here',
        'form': form})


def ticket_view(request, ticket_id):
    ticket = TicketItem.objects.get(id=ticket_id)
    return render(request, "ticket_view.html", {
        'heading': 'Ticket',
        "ticket": ticket})


def add_ticket(request):
    if request.method == 'POST':
        form = TicketItemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = TicketItem.objects.create(
               title=data['title'],
            #    author=request.user.author,
               description=data['description'],
               ticket_status=data['ticket_status']
            )
            return HttpResponseRedirect(reverse('ticket', args=[new_ticket.id]))

    form = TicketItemForm()
    return render(
        request,
        "add_ticket.html",
        {'form': form}
    )