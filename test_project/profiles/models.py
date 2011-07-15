from easy_profiles.models import ProfileBase


class Profile(ProfileBase):
    pass
    
class MultipleProfileBase(models.Model):    
    """ Use when your project has more than one app"""
    pass