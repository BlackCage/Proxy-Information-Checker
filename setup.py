from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="proxy_information",
    version="0.1",
    description="A tool to verify proxy information.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="BlackCage",
    author_email="blackcage_faq@proton.me",
    url="https://github.com/BlackCage/Proxy-Information-Checker",
    packages=find_packages(),
    install_requires=[
        "requests",
        "fake-useragent",
    ],
    classifiers=[
        "Topic :: Internet :: Proxy Servers",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
