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
        'Classifier: Development Status :: 4 - Beta',
        'Classifier: Environment :: Web Environment',
        'Classifier: Framework :: Django',
        'Classifier: Intended Audience :: Developers',
        'Classifier: Intended Audience :: System Administrators',
        'Classifier: Intended Audience :: Telecommunications Industry',
        'Classifier: License :: OSI Approved :: MIT License',
        'Classifier: Operating System :: OS Independent',
        'Classifier: Programming Language :: Python',
        'Classifier: Topic :: Communications :: Telephony',
    ]
)

