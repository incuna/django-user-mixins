from setuptools import find_packages, setup


version = '0.0.1'


install_requires = (
    'incuna_mail>=4.1.0,<4.2.0',
    'incuna-pigeon>=0.1.0,<1.0.0',
)

extras_require = {
    'avatar': [
        'django-imagekit>=3.2',
    ],
}

setup(
    name='django-user-mixins',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='User model mixins.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    keywords='django user mixin',
    author='Incuna',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-user-mixins/',
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
