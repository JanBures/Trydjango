from django.http import HttpResponse
from django.shortcuts import render
from generators import randoms

# Create your views here.
def home_view(request, *args, **kwargs):
	#print(request.user) # vypíše v konzoli přihlášeného uživatele
	#return HttpResponse("<h1>hello world</h1>")
	rand = randoms.random_int(max=10)
	my_context = {
	"jmeno":"Honza",
	"adresa":"Praha",
	"psc":11000,
	"rand_num":rand
	}
	return render(request, "home.html", my_context)


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})
