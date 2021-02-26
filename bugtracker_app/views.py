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
               description=data['description'],
            #    ticket_status=data['ticket_status'],
               filed_by=request.user
            )
            return HttpResponseRedirect(reverse('ticket', args=[new_ticket.id]))
    form = TicketItemForm()
    return render(request,
    "add_ticket.html",
    {'form': form}
    )

"""
localhost:8000/edit/4
"""

def ticket_edit(request, ticket_id):

    context = {}
    ticket = TicketItem.objects.get(id=ticket_id)

    if request.method == 'POST':
        form = TicketItemForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()
            return HttpResponseRedirect(reverse('ticket', args=[ticket.id]))

    form = TicketItemForm(
        initial={'title': ticket.title, 'description': ticket.description, 'ticket_status': ticket.ticket_status}
    )
    context.update({'form': form})
    return render(
        request,
        'add_ticket.html',
        context
        )
        

def author_edit(request, author_id):
   
    context = {}
    author_obj = CustomUser.objects.get(id=author_id)

    if request.method == 'POST':
        form = CustomUserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            author_obj.username = data['username']
            author_obj.email = data['email']
            author_obj.save()
            return HttpResponseRedirect(reverse('author', args=[author_obj.id]))

    form = CustomUserForm(
        initial={'username': author_obj.username, 'email': author_obj.email}
    )
    context.update({
        "author": author_obj,
        'form': form})
    return render(
        request,
        'author_view.html',
        context
        )



def author_view(request, author_id):

    author_obj = CustomUser.objects.get(id=author_id)
    tickets = TicketItem.objects.filter(filed_by=author_obj)

    return render(request, "author_view.html", {
        "author": author_obj,
        "tickets": tickets
    })


def new_ticket(request, ticket_id):
    ticket = TicketItem.objects.filter(id=ticket_id).first()
    ticket.ticket_status = 'NW'
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.filed_by = request.user
    ticket.save()
    return HttpResponseRedirect(reverse('ticket', args=[ticket.id]))



def ip_ticket(request, ticket_id):
    ticket = TicketItem.objects.filter(id=ticket_id).first()
    ticket.ticket_status = 'IP'
    ticket.assigned_to = request.user
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket', args=[ticket.id]))



def dn_ticket(request, ticket_id):
    ticket = TicketItem.objects.filter(id=ticket_id).first()
    ticket.ticket_status = 'DN'
    ticket.completed_by = ticket.assigned_to
    ticket.assigned_to = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket', args=[ticket.id]))



def in_ticket(request, ticket_id):
    ticket = TicketItem.objects.filter(id=ticket_id).first()
    ticket.ticket_status = 'IN'
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket', args=[ticket.id]))

