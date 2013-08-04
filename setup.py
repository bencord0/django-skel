import os
from setuptools import setup, find_packages

os.chdir(os.path.dirname(os.path.abspath(os.path.normpath(__file__))))

setup(name='{{ project_name }}',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            '{{ project_name }} = {{ project_name }}.wsgi:main'
            ]
        }
)
