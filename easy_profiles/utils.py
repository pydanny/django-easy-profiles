from django.conf import settings
from django.core.cache import cache

from easy_profiles.cachekeys import key_profile_getprofile
from easy_profiles.models import Profile

def get_profile(user):
    
    """ Rather than throw an error on get_profile, we just return None.
        Makes handling of anonymous users in non-loggedin areas easier.
    """
    if user.is_anonymous():
        return None

    try:
        key = key_profile_getprofile(user)
        profile = cache.get(key)
        if profile is not None:
            return profile
        profile = user.get_profile()
        cache.set(key, profile, settings.CACHE_TIMEOUT)
        return profile
    except Profile.DoesNotExist:
        return None
