from setuptools import setup

setup(name='{{ project_name }}',
    packages=['{{ project_name }}'],
    entry_points={
        'console_scripts': [
            '{{ project_name }} = {{ project_name }}.wsgi:main'
        ]
    }
)
