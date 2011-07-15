from setuptools import setup, find_packages
 
version = '0.1.0'
 
LONG_DESCRIPTION = open("README.rst").read()
 
setup(
    name='django-easy-profiles',
    version=version,
    description="django-easy-profiles",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='forms,django,profiles,middleware',
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/django-easy-profiles',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)