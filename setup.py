from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='urlparser',
    version='0.1',
    author='R. NAVEEN NITHYA KALYAN',
    author_email='naveennithyakalyan@gmail.com',
    packages=find_packages(),
     entry_points={
        'console_scripts': [
            'urlparser = urlparser:read_urls',
        ],
     },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating system :: OS Independent',],

)
