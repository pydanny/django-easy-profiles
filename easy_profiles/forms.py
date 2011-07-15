from django import forms

from easy_profiles.models import ProfileBase

class ProfileForm(forms.ModelForm):
    
    class Meta:
        
        excludes = (
                    'user',
                    )
        model = Profile

