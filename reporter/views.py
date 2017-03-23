from django.shortcuts import render
from .models import Case, Report, Author
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    
    num_cases=Case.objects.all().count()
    num_reports=Report.objects.all().count()
    num_authors=Author.objects.all().count()
    
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Unresolved cases (status = 'u')
    num_cases_unresolved=Case.objects.filter(status__exact='u').count()
    
    return render(
        request,
        'index.html',
        context={'num_cases':num_cases,'num_reports':num_reports,'num_cases_unresolved':num_cases_unresolved, 'num_authors':num_authors, 'num_visits':num_visits},
    )

class CaseListView(LoginRequiredMixin, generic.ListView):
    model = Case
    paginate_by = 10

class CaseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Case

class CaseCreate(CreateView):
    model = Case
    fields = '__all__'

class CaseUpdate(UpdateView):
    model = Case
    fields = '__all__'

class CaseDelete(DeleteView):
    model = Case
    success_url = reverse_lazy('cases') # Redirect to Cases list

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors') # Redirect to Authors list

class ReportCreate(CreateView):
    model = Report
    fields = '__all__'
    success_url = reverse_lazy('cases') # Redirect to Cases list

class ReportUpdate(UpdateView):
    model = Report
    fields = '__all__'
    success_url = reverse_lazy('cases') # Redirect to Cases list

class ReportDelete(DeleteView):
    model = Report
    success_url = reverse_lazy('cases') # Redirect to Cases list