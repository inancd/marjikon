from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, PersonalInfo

@receiver(post_save, sender=CustomUser)
def create_personal_info(sender, instance, created, **kwargs):
    if created:
        PersonalInfo.objects.create(user=instance)