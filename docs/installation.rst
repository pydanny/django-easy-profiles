============
Installation
============

This document will explain how django-easy-profiles into your project. django-easy-maps tries to be as unobtrusive as possible, so you should
be able to add or remove components of this app with minimal difficulty.

Prerequisites
=============

django-easy-profiles has been tested with the following:

 * Python 2.6.x and Python 2.7.x
 * Django 1.3.x
 
Installation Fundamentals
==========================

First fetch the package from PyPI::

    pip install django-easy-profiles

Add django-easy-profiles to your INSTALLED_APPS::

    INSTALLED_APPS = [
        # ...
        "easy_profiles",
    ]

Wire django-easy-profiles into your URLconf::

    urlpatterns = patterns("",
        # ...
        url(r"^profiles/", include("idios.urls"))
    )