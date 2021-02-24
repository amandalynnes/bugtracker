from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from .forms import CustomUserForm, LoginForm
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
