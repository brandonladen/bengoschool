from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import GradingLevel


@receiver(post_save, sender=GradingLevel)
def after_saving_grading(sender, created, instance, *args, **kwargs):
    """Change all grading system to false if this is true"""
    if instance.current is True:
        GradingLevel.objects.exclude(pk=instance.id).update(current=False)