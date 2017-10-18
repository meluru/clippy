from __future__ import unicode_literals

from setuptools import setup, find_packages


setup(
    name='indico_clippy',
    version='0.0.1',
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'indico>=1.9.11.dev17'
    ],
    entry_points={
        'indico.plugins': {'clippy = indico_clippy.plugin:ClippyPlugin'}
    }
)
