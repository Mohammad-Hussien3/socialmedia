from celery import shared_task
from .models import Story

@shared_task
def delete_story_after_24_hours(story_id):
    try:
        story = Story.objects.get(id=story_id)
        story.delete()  # Delete the story after 24 hours
    except Story.DoesNotExist:
        # Handle the case where the story doesn't exist
        pass
