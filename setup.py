import os
#from setuptools import setup
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-feedback',
    version='0.4.1',
    description='A pluggable user feedback app',
    author='Jared Forsyth',
    author_email='jabapyth@gmail.com',
    license='Apache v2',
    url='http://github.com/unaizalakain/django-feedback/',
    keywords = ['blog', 'django', 'feedback', 'ajax', 'user', 'customer', 'comment'],
    package_data = {'feedback': ['static/feedback/*.js', 'static/feedback/*.css', 'static/feedback/images/*.png', 'CREDITS']},
    packages=[
        'feedback',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
