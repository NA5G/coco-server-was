# -*- coding: utf-8 -*-

from django.db import models
from users.models import User
from django.utils import timezone

def default_expire_date():
    return timezone.now() + timezone.timedelta(days=7)

class Auction(models.Model):

    product_condition = models.CharField(max_length=100, blank=True)
    original_price = models.PositiveIntegerField(default=0, blank=False)
    immediate_price = models.PositiveIntegerField(default=0, blank=False)
    starting_price = models.PositiveIntegerField(default=0, blank=False)
    # TODO: how do i save value from starting_price?
    current_price = models.PositiveIntegerField(default=0, blank=False)
    transaction_place = models.CharField(max_length=100, null=False)
    expire_date = models.DateTimeField(default=default_expire_date)
    is_active = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)

    def remain_time(self):
        self.expire_date

    def complete(self):
        post = self.post
        post.is_active = False
        post.save()

        # TODO: new deal object
        # bidding: immediately price
        # dealer: posts user
        # buyer: current user
        # auction: self

        self.is_active = False
        self.is_completed = True
        self.save()

    def is_active(self):
        # TODO: compare expire date with current date instead of is_active
        return self.is_active

class Deal(models.Model):

    auction = models.ForeignKey(Auction, related_name='deals', related_query_name='deal')
    dealer = models.OneToOneField(User, related_name='dealer', related_query_name='delaer')
    buyer = models.OneToOneField(User, related_name='buyer', related_query_name='buyer')
    bidding = models.PositiveIntegerField(default=0, blank=False)

    def __unicode__(self):
        return self.auction


class Tag(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Post(models.Model):

    class Meta:
        ordering = ['created_at']

    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    tags = models.ManyToManyField(Tag, related_name='tags', related_query_name='tag')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    comment_count = models.PositiveSmallIntegerField(default=0, null=True)
    auction = models.OneToOneField(Auction)

    def __unicode__(self):
        return self.title


class Photo(models.Model):

    post = models.ForeignKey(Post, related_name='photos', related_query_name='photo')
    image_file= models.ImageField(upload_to='uploaded')

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        super(Post, self).delete(*args, **kwargs)

    def __unicode__(self):
        return "%s" % (self.id)


class Comment(models.Model):

    post = models.ForeignKey(Post, related_name='comments', related_query_name='comment')
    content = models.CharField(max_length=100, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def create_comment(self, post_id, user_id, content):
        new_comment = Comment(post_id=post_id, user_id=user_id, content=content)
        return new_comment

    def __unicode__(self):
        return self.content
