from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model

def cadastro_views(request):
  if request.method == 'POST':
    form = UsuarioForm(request.POST)

    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data["password"])
      user.save()
      return redirect('autenticacao:login')
  
  else:
    form = UsuarioForm()
  
  return render(request, 'autenticacao/cadastro.html', {'form': form})

def login_views(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']

    User = get_user_model()
    print(User.objects.all().values('email'))
    user = authenticate(request, email=email, password=password)

    if user is not None:
      login(request, user)
      return redirect('api:chamado-create-view')

    else:
      messages.error(request, 'Credenciais Inválidas')

  return render(request, 'autenticacao/login.html')
