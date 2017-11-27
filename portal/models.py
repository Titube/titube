# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Video(models.Model):
	titulo = models.CharField(max_length=250)
	video = models.FileField(null=True, blank=True)
	imagem = models.FileField(null=True, blank=True)
	categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE, null=True)

	def __unicode__(self):
		return u'%s' %(self.titulo)


class Categoria(models.Model):
	titulo = models.CharField(max_length=250)


	def __unicode__(self):
		return u'%s' %(self.titulo)

