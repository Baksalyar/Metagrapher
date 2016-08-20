from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Metagrapher',
    version='1.0.0',

    description='Transliteration module, that helps to reduce strings written in different languages to identifier (URI, for instance), consisting only from english letters and numbers.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/Baksalyar/Metagrapher',

    # Author details
    author='Andrey Baksalyar',
    author_email='andreybaksalyar@ya.ru',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Internationalization',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
    ],

    # What does your project relate to?
    keywords='translit transliteration slugify slug translate languages url uri metagraphy',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)