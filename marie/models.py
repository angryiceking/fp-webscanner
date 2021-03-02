from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fp_template_base64 = models.TextField()
    fp_bmp_base64 = models.TextField(null=True, blank=True)
    fp_encode_wsq = models.TextField(null=True, blank=True)
    fp_image_dimension = models.CharField(max_length=255, blank=True)
    fp_image_nfiq = models.TextField(null=True, blank=True)
    fp_image_wsq_size = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     instance.save()