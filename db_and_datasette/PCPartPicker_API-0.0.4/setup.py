from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PCPartPicker_API",
    version="0.0.4",
    description="An unofficial API to access & scrape data from pcpartpicker.com",
    long_description=long_description,
    url="https://github.com/thatguywiththatname/PcPartPicker-API",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    keywords="PCPartPicker API scraping",
    packages=find_packages(exclude=["contrib", "docs", "tests", "examples"]),
    install_requires=["beautifulsoup4", "requests"]
)
