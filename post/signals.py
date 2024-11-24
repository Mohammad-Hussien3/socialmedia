from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Comment, Reaction, Notification, Mention
from usermanagement.models import Profile

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
def create_mention_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            sender=instance.profile,
            receive=instance.post.profile,
            content=f'{instance.profile.user.username} mentioned you'
        )


@receiver(m2m_changed, sender=Profile.followers.through)
def create_follow_notification(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        for pk in pk_set:
            follower_user = Profile.objects.get(id=pk)
            Notification.objects.create(
                sender=follower_user,
                receive=instance,
                content=f'{instance} followed you'
            )