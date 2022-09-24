from http.client import HTTPResponse
from django.shortcuts import render
from last import task1


a=0
b=0
def output(request,a,b):
    return(task1.finder(request,a,b))

