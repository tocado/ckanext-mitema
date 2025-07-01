from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='mitema',
    version=version,
    description='Tema personalizado para CKAN',
    author='Tu Nombre',
    license='MIT',
    namespace_packages=['mitema'],
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [ckan.plugins]
        mitema=ckanext.mitema.plugin:MiTemaPlugin

        [ckan.templates]
        mitema=ckanext.mitema
    ''',
)