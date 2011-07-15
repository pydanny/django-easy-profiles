def key_profile_getprofile(user):
    return "auth:models:user:getprofile:{0}".format(user.id)

def key_profile_username(profile):
    return "profiles:models:profile:username:{0}".format(profile.id)
        
def key_profile_translate(profile, language):
    return "profiles:profile:translate:%s:%s" % (profile.id, language)