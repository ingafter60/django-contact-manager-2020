from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Contact
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView

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

def search(request):
	if request.GET:
		search_term = request.GET['search_term']
		search_results = Contact.objects.filter(
			Q(name__icontains=search_term) |
			Q(email__icontains=search_term) |
			Q(info__icontains=search_term) |
			Q(gender__iexact=search_term) |
			Q(date_added__icontains=search_term) |
			Q(phone__iexact=search_term) 
		)
		context = {
			'search_term': search_term,
			'contacts': search_results
		}
		return render(request, 'search.html', context)	
	else:
		return redirect('home')	

class ContactCreateView(CreateView):
	# use Contact model and store its value in 'model'
	model = Contact 
	# template name to render the form to create contact object
	template_name = 'create.html'
	# fields to display in the template from the Contact model / table
	fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
	# where to go (go to home page) when object is successfully created
	success_url = '/'


class ContactUpdateView(UpdateView):
	# use Contact model and store its value in 'model'
	model = Contact 
	# template name to render the form to create contact object
	template_name = 'update.html'
	# fields to display in the template from the Contact model / table
	fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
	
	# where to go (go to detail page based on pk) when object is successfully created
	def form_valid(self, form):
		instance = form.save()
		return redirect('detail', instance.pk)