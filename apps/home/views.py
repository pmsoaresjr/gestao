# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Cliente
from .forms import ClienteForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        clientes = Cliente.objects.all()
        # print(f"clientes : {clientes}")
        
        context["clientes"] = Cliente.objects.all()


        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def cliente_lista(request):
    context = {}
    clientes = Cliente.objects.all()
    # print(f"clientes : {clientes}")
        
    context["clientes"] = Cliente.objects.all()
    html_template = loader.get_template('home/cliente.html')
    # print(html_template)
    
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def cadastrar_cliente(request): 
    print("debug estou na função cadastrar cliente")

    context = {}
    form =  ClienteForm(request.POST or None)
    html_template = loader.get_template('home/cliente-registro.html')
    context['form'] = form
    if str(request.method) == 'POST':
        print(f"validação do form [cadastrar cliente] {form.is_valid()}")
        if form.is_valid():
            cliente = form.save()
            messages.success(request,  'Cliente cadastrado com sucesso!')
            return redirect('/cliente',cliente_lista=cliente_lista)
            # return redirect('visualizar_cliente', cliente.id)
            #return render(request,'visualizar_cliente.html',{'cliente' : form.cleaned_data})
        else:
            print(form.errors.as_data())
            messages.error(request,  'Erro ao cadastrar o cliente. Contate o administrador')
            
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def deletar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    # print(cliente)  
    cliente.delete() 
    messages.success(request,  'Cliente Deletado com sucesso')
    return redirect('/cliente',cliente_lista=cliente_lista)

@login_required(login_url="/login/")
def atualizar_cliente(request,id):
    print("debug estou na função atualizar cliente")
    print(f"id [atualizar cliente]: {id}")
    context = {}
    html_template = loader.get_template('home/cliente-registro.html')
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    context['form'] = form
    if form.is_valid():
        print(f"validação do form [atualizar cliente] {form.is_valid()}")

        form.save()
        return redirect('/cliente',cliente_lista=cliente_lista)
    # context = {"form": form}
    # return render(request, html_template, context)
    return HttpResponse(html_template.render(context, request))