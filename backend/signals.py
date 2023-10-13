from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.create_user_profile()
