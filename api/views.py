from django.shortcuts import render

from api.models import Publication

# Create your views here.


def publication_list(request):
    publications = Publication.objects.all()
    print(publications.values_list())
    return render(request, "publication_list.html", {"publications": publications})
    
