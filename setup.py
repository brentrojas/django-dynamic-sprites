from setuptools import setup, find_packages

setup(
    name='django-dynamic-sprites',
    version='0.1.4',
    description='A way to generate sprites based on objects created by the application user.',
    long_description=open('README.rst').read(),
    author='Vinicius Mendes',
    author_email='vbmendes@gmail.com',
    url='https://github.com/vbmendes/django-dynamic-sprites',
    download_url='https://github.com/vbmendes/django-dynamic-sprites/downloads',
    license='BSD',
    packages=find_packages(exclude=('ez_setup', 'tests', 'example')),
    install_requires=[
        'Pillow>=2.8.1',
        'unidecode>=0.04.9',
    ],
    tests_require=[
        'django>=1.1',
    ],
    scripts=[
        'scripts/generate_sprite.py'
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
    ],
)
