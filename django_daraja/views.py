# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_daraja.mpesa import utils

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'

def index(request):
    return render(request, 'dataoffers/bingwasokoni.html')

def oauth_success(request):
	r = cl.access_token()
	return JsonResponse(r, safe=False)

@csrf_exempt
def process_deal(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')

        if not amount or not phone_number:
            return render(request, 'dataoffers/bingwasokoni.html', {'error': 'Invalid form submission'})
        
        amount = int(amount)
        account_reference = 'EMMKASH BINGWA DATA'
        transaction_desc = 'Data Deal Purchase'
        callback_url = stk_push_callback_url

        # Initiate STK push
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        return render(request, 'dataoffers/bingwasokoni.html', {'message': 'Payment initiated. Please check your phone.'})

    return render(request, 'dataoffers/bingwasokoni.html', {'error': 'Invalid request method'})

def stk_push_success(request):
	phone_number = '254112735877'
	amount = 1
	account_reference = 'EMMKASH BINGWA DATA'
	transaction_desc = 'STK Push Description'
	callback_url = stk_push_callback_url
	r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
	return JsonResponse(r.response_description, safe=False)

def business_payment_success(request):
	phone_number = config('B2C_PHONE_NUMBER')
	amount = 1
	transaction_desc = 'Business Payment Description'
	occassion = 'Test business payment occassion'
	callback_url = b2c_callback_url
	r = cl.business_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)

def salary_payment_success(request):
	phone_number = config('B2C_PHONE_NUMBER')
	amount = 1
	transaction_desc = 'Salary Payment Description'
	occassion = 'Test salary payment occassion'
	callback_url = b2c_callback_url
	r = cl.salary_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)

def promotion_payment_success(request):
	phone_number = config('B2C_PHONE_NUMBER')
	amount = 1
	transaction_desc = 'Promotion Payment Description'
	occassion = 'Test promotion payment occassion'
	callback_url = b2c_callback_url
	r = cl.promotion_payment(phone_number, amount, transaction_desc, callback_url, occassion)
	return JsonResponse(r.response_description, safe=False)
