#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

#判定访问的来源是iPhone还是pc
class CheckBrowserMiddware(object):
    def process_request(self, request):
        from_source = request.META['HTTP_USER_AGENT']
        print('from_source: ', from_source)
        if 'MSIE 6.0' in from_source:
            request.session['from_source'] = 'MSIE 6.0'

        elif 'MSIE 7.0' in from_source:
            request.session['from_source'] = 'MSIE 7.0'

        elif 'MSIE 8.0' in from_source:
            request.session['from_source'] = 'MSIE 8.0'

        else:
            request.session['from_source'] = 'browser'
