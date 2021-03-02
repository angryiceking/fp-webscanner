from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import UserRegistrationForm


# Create your views here.

class MarieBiscuit(View):

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'index.html', {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            fp_template_base64 = request.POST.get('fp_template_base64')
            fp_bmp_base64 = request.POST.get('fp_bmp_base64')
            fp_encode_wsq = request.POST.get('fp_encode_wsq')
            fp_image_height = request.POST.get('fp_image_height')
            fp_image_width = request.POST.get('fp_image_width')
            fp_image_resolution = request.POST.get('fp_image_resolution')
            fp_image_quality = request.POST.get('fp_image_quality')
            fp_image_nfiq = request.POST.get('fp_image_nfiq')
            fp_image_wsq_size = request.POST.get('fp_image_wsq_size')
            fp_image_dimension = {
                "height": fp_image_height,
                "width": fp_image_width,
                "resolution": fp_image_resolution,
                "quality": fp_image_quality
            }
            user = User.objects.get(username=username)
            user_profile = UserProfile(
                user_id=user.id,
                fp_template_base64=fp_template_base64,
                fp_bmp_base64=fp_bmp_base64,
                fp_encode_wsq=fp_encode_wsq,
                fp_image_dimension=fp_image_dimension,
                fp_image_nfiq=fp_image_nfiq,
                fp_image_wsq_size=fp_image_wsq_size
            )
            user_profile.save()
            print('profile saved', fp_image_dimension, username)
        else:
            print('invalid')
        return HttpResponse('nice, a successfull post request on my index page, hmm', status=200)