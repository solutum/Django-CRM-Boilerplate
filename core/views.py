from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages # show messages to user
from django.http import HttpResponseBadRequest, JsonResponse
import json


def login_user(request):
	# print("login_user")
	# check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Auth
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been logged in!")
			return redirect('dashboard:index')
		else:
			messages.warning(request, "There was an error")
		#return redirect('dashboard:index')

	return render(request, 'login.html') #{'records': records})


def logout_user(request):
	logout(request)

	messages.success(request, "You have been Logged Out")

	return redirect('core:login')


def api_change_dark_mode(request):
	is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
	if is_ajax:
		if request.method == 'POST':
			data = json.load(request)
			request.session['dark_mode'] = data['dark_mode']

			return JsonResponse({'status': 'ok'})
		return JsonResponse({'status': 'Invalid request'}, status=400)
	else:
		return HttpResponseBadRequest('Invalid request')