from setuptools import setup

setup(name='{{ project_name }}',
    packages=[
        '{{ project_name }}',
        '{{ project_name }}.apps',
        '{{ project_name }}.libs',
        '{{ project_name }}.settings',
        ],
    entry_points={
        'console_scripts': [
            '{{ project_name }} = {{ project_name }}.wsgi:main'
            ]
        }
)
