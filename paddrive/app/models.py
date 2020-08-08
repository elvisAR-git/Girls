from django.db import models
from django.utils.timezone import now
# Create your models here.


class HomepageSlides(models.Model):
    hq_image = models.ImageField(null=True, upload_to="slides")
    main_title = models.CharField(max_length=100, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.main_title


class Blog(models.Model):
    hq_image = models.ImageField(null=True)
    main_title = models.CharField(max_length=100, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    link = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, default=now)

    # author

    author_name = models.CharField(
        max_length=50, blank=True, default="Unkown Author", null=True)
    author_pic = models.ImageField(null=True, blank=True)
    author_remarks = models.TextField(
        blank=True, default="No remarks", null=True)

    # empasis or extract

    extract = models.TextField(blank=True, default="No quote", null=True)

    def __str__(self):
        return self.main_title


class Mission(models.Model):
    mission_statement = models.CharField(max_length=100, blank=True, null=True)
    mission_description = models.TextField()
    img_1 = models.ImageField(null=True)
    img_2 = models.ImageField(null=True)
    date_published = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    img = models.ImageField(null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    target = models.IntegerField()
    raised = models.IntegerField()

    # calcutated property
    @property
    def percentage(self):
        p = (self.raised * 100) / self.target
        return int(p)


class SocialEvents(models.Model):
    img = models.ImageField(null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(null=True, blank=True, max_length=50)
    # optional
    iframe = models.TextField(null=True, blank=True)


class Admins(models.Model):
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(max_length=40, blank=True, null=True)
    twitter_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    web_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Quotes(models.Model):
    img = models.ImageField(null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(max_length=40, blank=True, null=True)
    quote = models.CharField(max_length=256, blank=True, null=True)


class Stats(models.Model):
    stat_1 = models.IntegerField(null=True, blank=True)
    stat_2 = models.IntegerField(null=True, blank=True)
    stat_3 = models.IntegerField(null=True, blank=True)


class ContactInformation(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_1 = models.CharField(max_length=16)
    phone_2 = models.CharField(max_length=16)
    email = models.EmailField()


class Feedback(models.Model):
    message = models.TextField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)


class Photo(models.Model):
    img = models.ImageField()
    caption = models.CharField(max_length=256)
