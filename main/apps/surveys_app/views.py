# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(req):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def new(req):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)