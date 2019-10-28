from django.shortcuts import render
from .models import IconGrid, ImageShowCase, Testimonial

# Create your views here.
def index(request):
    grids = IconGrid.objects.all()
    showcases = ImageShowCase.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, "index.html", {'grids': grids, 'showcases': showcases, 'testimonials': testimonials })

