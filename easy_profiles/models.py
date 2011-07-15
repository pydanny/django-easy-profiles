from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.utils.translation import ugettext_lazy as _

from easy_profiles import cachekeys

class ProfileBase(models.Model):
    """ Profiles for users of all types """
    user = models.OneToOneField(User)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30, help_text=_("Middle Name or Initial"), blank=True)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('e-mail address'))
    is_active = models.BooleanField(_('Active account?'), default=True)

    def __unicode__(self):
        return self.username
    
    class Meta:
        abstract = True

    def save(self, **kwargs):
        """ Override save to always populate changes to auth.user model
        """

        user_obj = User.objects.get(username=profile.user.username)
        user_obj.first_name = profile.first_name
        user_obj.last_name = profile.last_name
        user_obj.email = profile.email
        user_obj.is_active = profile.is_active
        user_obj.save()

        super(Profile,self).save(**kwargs)
        
    @property
    def username(self):
        key = cachekeys.key_profile_username(self)
        username = cache.get(key)
        if username is not None:
            return username
        username = self.user.username
        cache.set(key, username, settings.CACHE_TIMEOUT)
        return username
        
    def get_full_name(self):
        """ Short cut method that duplicates user.get_full_name """
        return "{0} {1}".format(self.first_name, self.last_name)
    
    def get_profile_link(self):
        """ breaks MVC but keeps us sane """
        profile_link = '<a href="{0}">{1}</a>'.format(self.get_absolute_url(), self.get_full_name() or self.username)
        return profile_link
        
    @models.permalink
    def get_absolute_url(self):
        return ("profile_detail", (), {"username": self.username})