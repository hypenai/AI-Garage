from setuptools import setup, find_packages

setup(
    name="ai_garage",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'ai_garage = src.main:main',
        ],
    },
)
