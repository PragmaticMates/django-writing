#!/usr/bin/env python
from setuptools import setup


setup(
    name='django-writing',
    version='2.0.1',
    description='Basic blog app for Django',
    long_description=open('README.md').read(),
    author='Pragmatic Mates',
    author_email='info@pragmaticmates.com',
    maintainer='Pragmatic Mates',
    maintainer_email='info@pragmaticmates.com',
    url='https://github.com/PragmaticMates/django-writing',
    packages=[
        'writing',
        'writing.migrations'
    ],
    include_package_data=True,
    install_requires=('django', 'markdown', 'martor', 'django-tinymce'),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 3 - Alpha'
    ],
    license='BSD License',
    keywords="django blog article category writing",
)
