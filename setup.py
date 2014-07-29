from setuptools import setup, find_packages

from notifications import __version__

setup(
    name='django-notifications-hq',
    version=__version__,
    description='GitHub notifications alike app for Django.',
    long_description=open('README.rst').read(),
    author='Brant Young',
    author_email='brant.young@gmail.com',
    url='http://github.com/brantyoung/django-notifications',
    install_requires=[
        'django>=1.4',
        'django-model-utils>=2.0.3'
    ],
    packages=['notifications',
              'notifications.templatetags',
              'notifications.migrations'
          ],
    package_data={'notifications': [
        'templates/notifications/*.html']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        'Topic :: Utilities',
    ],
    tests_require=["Django", "django-model-utils"],
    test_suite="runtests.runtests",
)
