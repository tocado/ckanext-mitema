from setuptools import setup, find_packagesAdd commentMore actions

setup(
    name='ckanext-mitema',
    version='0.0.1',
    description='Tema personalizado para CKAN',
    author='Adrian Figueroa',
    license='MIT',
    packages=find_packages(),  # ?? importante

    include_package_data=True,
    zip_safe=False,
    entry_points='''
        [ckan.plugins]
        mitema=ckanext.mitema.plugin:MiTemaPlugin

        [ckan.templates]
        mitema=ckanext.mitema
    ''',
