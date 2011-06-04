from distutils.core import setup

setup(
    name='django-asterisk',
    version='0.1',
    description='Phone call queuing and management for the Django web framework using an Asterisk server',
    long_description=open('README').read(),
    author='Maximiliano Bertacchini',
    author_email='maxiberta@gmail.com',
    url='https://github.com/maxiberta/django-asterisk',
    packages=[
        'django_asterisk',
    ],
    requires=['pyst'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Telephony',
    ]
)

