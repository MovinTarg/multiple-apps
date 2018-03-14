# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(req):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

def login(req):
    response = "placeholder for users to login"
    return HttpResponse(response)

def register(req):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)
