from django.shortcuts import render

# Create your views here.
def contact(request):
    context = locals()
    templates = 'contact.html'
    return render(request,templates,context)
