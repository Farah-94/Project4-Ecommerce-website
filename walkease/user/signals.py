from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create profile when a new user is registered
        Profile.objects.create(user=instance)
    elif hasattr(instance, 'profile'):
        # Save existing profile on user update
        instance.profile.save()
