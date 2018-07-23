from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'aboutus/blog.html')

def contact(request):
    return render(request, 'aboutus/contact.html')

def team(request):
    return render(request, 'aboutus/team.html')