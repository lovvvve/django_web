#!/bin/env python
# -*- coding: utf-8 -*-
#:Tital: views.py
#:Synopsis: views.py
#:Date: 2013-03-04
#:Version: 1.0
#:Author: lovvvve
#:Options: 


from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
#    html = "<html><body><h1>Now time is %s.</h1></body></html>" % now
#    t = Template("<html><body><h1>It is now {{ current_date }}.</h1></body></html>")
#    t = get_template('current_datetime.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)
    return render_to_response('current_datetime.html',{'current_date': now})

def hours_ahead(request,offsef):
    """docstring for hours_ahead"""
    offsef = int(offsef)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offsef)
#    html = "<html><body><h1>In %s hour(s), it will be %s.</h1></body></html>" % (offsef, dt)
 #   return HttpResponse(html)
    return render_to_response('hours_ahead.html',{'hour_offset': 4, 'next_time': dt})

def my_image(requset):
    image_data = open("./static/1.png","rb").read()
    return HttpResponse(image_data, mimetype="image/png")
