from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
		'status': 'Working on this project',
		'age': 63,
	}
	return render(request, 'index.html', context)

def detail(request):
	return render(request, 'detail.html')

def search(request):
	return render(request, 'search.html')