from django.db import models
from django.contrib.auth import get_user_model
from artworks.models import Title
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    score = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(score__gte=1) & models.Q(score__lte=10),
                name=_('Score should be between 1 and 10'),
            ),
            models.UniqueConstraint(
                fields=('title', 'author'),
                name=_('Only one review allowed per title'),
            ),
        ]
        ordering = ('-pub_date',)

    def __str__(self):
        return f'{self.title} - {self.author} - {self.pub_date.strftime("%c")}'


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return (
            f'{self.review} - {self.author} - '
            f'{self.pub_date.strftime("%c")}'
        )
