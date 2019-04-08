import codecs
import setuptools
import sys

long_description = codecs.open('README.md', "r").read()

# See https://hynek.me/articles/conditional-python-dependencies/

INSTALL_REQUIRES = [
    "django >= 2.0",
    "requests >= 2.10.0",
    "six >= 1.10.0"
]

setuptools.setup(
    name="django-custom-storage",
    version="0.0.1",
    author="Yelson Chevarrias",
    author_email="chevarrias@gmail.com",
    description="Storage implementation for Django that interacts with Custom Service",
    url="https://github.com/ccapudev/dstorage",
    packages=setuptools.find_packages(exclude=["dstorage_tests", "docs", "test_project"]),
    long_description=long_description,
    package_data={
        '': ['README.md'],
    },
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
)
