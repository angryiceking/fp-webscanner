from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    fp_template_base64 = forms.CharField(widget=forms.Textarea)
    fp_bmp_base64 = forms.CharField(widget=forms.Textarea, required=False)
    fp_encode_wsq = forms.CharField(widget=forms.Textarea, required=False)
    fp_image_nfiq = forms.CharField(widget=forms.Textarea, required=False)
    fp_image_wsq_size = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'fp_template_base64', 'fp_bmp_base64', 'fp_encode_wsq', 'fp_image_nfiq', 'fp_image_wsq_size')