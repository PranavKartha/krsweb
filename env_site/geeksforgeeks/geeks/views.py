from django.shortcuts import render

# Create your views here.
def home_view(request):

	# logic of view will be implemented here
	return render(request, "home.html")
