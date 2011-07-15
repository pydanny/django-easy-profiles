from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.generic import list_detail

from easy_profiles.forms import ProfileForm
from easy_profiles.models import Profile
    

@login_required
def profile_detail(request, username, template_name="profiles/profile_detail.html"):
    
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    
    return render_to_response(template_name,
        {
            "profile": profile,
            "activities": Activity.objects.filter(author=user)
        },
        context_instance=RequestContext(request)
    )
    
@login_required
def profile_edit(request, template_name="profiles/profile_edit.html"):

    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    
    if form.is_valid():
        form.save()
        msg = 'Profile edited'
        messages.add_message(request, messages.INFO, msg)
        return HttpResponseRedirect(reverse("profile_detail", kwargs={"username":profile.user.username }))

    return render_to_response(template_name,
        {
            "profile": profile,
            "form": form,
        },
        context_instance=RequestContext(request)
    )
    
@login_required
def profile_list(request, page=None, template_name="profiles/profile_list.html"):
    """
    List all public profiles 
    """ 
    qs = Profile.objects.filter(is_active=True).order_by("last_name", "first_name")

    return list_detail.object_list(
            request,
            qs,
            allow_empty=True, 
            template_name=template_name, 
            template_object_name='profile', 
            paginate_by=25,
            page=page,
        )