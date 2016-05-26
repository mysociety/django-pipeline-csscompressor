#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-pipeline-csscompressor',
    version='0.1',
    description="A django-pipeline compressor to compress css files using csscompressor",
    author='mySociety',
    author_email='programmers@mysociety.org',
    url='https://github.com/mysociety/django-pipeline-csscompressor',
    py_modules=['django_pipeline_csscompressor'],
    license='LICENSE.txt',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    install_requires=[
        "django-pipeline>=1.6.8",
        "csscompressor>=0.9.4",
    ],
)
