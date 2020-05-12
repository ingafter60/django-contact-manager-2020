from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Contact

# Create your views here.
# def home(request):
# 	context = {
# 		'contacts': Contact.objects.all(),
# 	}
# 	return render(request, 'index.html', context)

# def detail(request, id):
# 	context = {
# 		'contact': get_object_or_404(Contact, pk=id)
# 	}
# 	return render(request, 'detail.html', context)


# Class based-views
class HomePageView(ListView):
	template_name = 'index.html'
	model 		  = Contact
	context_object_name = 'contacts'

class ContactDetailView(DetailView):
	template_name = 'detail.html'
	model 		  = Contact
	context_object_name = 'contact'