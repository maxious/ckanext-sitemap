from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
    name='ckanext-sitemap',
    version=version,
    description="sitemap.xml generator for CKAN",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Alex Sadleir',
    author_email='alex.sadleir@linkdigital.com.au',
    url='',
    license='AGPL3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.sitemap'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        sitemap=ckanext.sitemap.plugin:SitemapPlugin
    ''',
)
