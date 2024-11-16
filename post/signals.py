from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Reaction, Notification, Mention

@receiver(post_save, sender=Reaction)
def create_reaction_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            sender=instance.profile,
            receive=instance.post.profile,
            content=f'{instance.profile.user.username} Liked your post'
        )


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            sender=instance.profile,
            receive=instance.post.profile,
            content=f'{instance.profile.user.username} commented on your post'
        )


@receiver(post_save, sender=Mention)
def create_metion_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            sender=instance.profile,
            receive=instance.post.profile,
            content=f'{instance.profile.user.username} mentioned you'
        )