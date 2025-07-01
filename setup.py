from setuptools import setup, find_packages

setup(
    name='ckanext-mitema',
    version='0.0.1',
    description='Tema personalizado para CKAN',
    author='Tu Nombre',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    package_dir={'': 'ckanext'},        # ?? importante
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [ckan.plugins]
        ckanext-mitema=ckanext.mitema.plugin:MiTemaPlugin

        [ckan.templates]
        ckanext-mitema=ckanext.mitema
    ''',
)