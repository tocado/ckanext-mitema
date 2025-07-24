from setuptools import setup, find_packages

setup(
    name='mitema',
    version='0.0.1',
    description='Tema personalizado para CKAN',
    author='Tu Nombre',
    license='MIT',
    packages=find_packages("ckanext"),
    package_dir={'': '.'},
    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [ckan.plugins]
        mitema=ckanext.mitema.plugin:MiTemaPlugin
        
        [ckan.templates]
        mitema=ckanext.mitema
    ''',
)