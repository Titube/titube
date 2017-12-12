# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from portal.models import Categoria, Video



def home(request):

	#categorias = Categoria.objects.filter(titulo__in=("Windows","Acompanhamento de Sessão"))

	categorias = Categoria.objects.filter(titulo__in=("Windows","Acompanhamento de Sessão"))	

	context = {
			"categorias":categorias
	}

	template  = loader.get_template('portal/home.html')
	return HttpResponse(template.render(context, request))


