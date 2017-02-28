from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from school_app.models import School, Course, Enquiry
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    country_code = request.GET.get("country", None)
    if "all" == country_code:
        country_code = None
        
    query = request.GET.get("q", None)
    results = School.objects.all()
    if country_code is not None:
        results = results.filter(country_code=country_code)

    if query is not None:
        results = results.filter(name__icontains=query)

    print("country_code %s\n" % (country_code))
    print("results %s" % (results))

    return render(request, 'search.html', {'results': results.all()})

def detail(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    courses = Course.objects.filter(school__id=school_id)
    print("courses %s" %(courses))
    return render(request, "detail.html", {'school': school, 'courses': courses})

def save_enquiry(request):
    enquiry = Enquiry()
    enquiry.interest = request.POST.get('interest', '')
    enquiry.question = request.POST.get('question', '')
    enquiry.name = request.POST.get('name', '')
    enquiry.email = request.POST.get('email', '')
    enquiry.number = request.POST.get('number', '')
    enquiry.save()

    return render(request, 'ask.html')
