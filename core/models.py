from django.db import models


class Target(models.Model):
    email = models.EmailField('Email address', null=False, blank=False)
    redirect_uri = models.URLField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + str(self.created_at)


class Activity(models.Model):
    target = models.ForeignKey(Target, related_name='activity', on_delete=models.SET_NULL, null=True)
    remote_addr = models.TextField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.target.email + str(self.created_at)
