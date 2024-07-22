from setuptools import setup, find_packages

setup(
    name='sefoo-agent',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Hier Abhängigkeiten hinzufügen
    ],
    entry_points={
        'console_scripts': [
            'sefoo-agent=sefoo_agent.sefoo_agent:main',
        ],
    },
)
