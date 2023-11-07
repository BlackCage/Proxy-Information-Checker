from setuptools import setup, find_packages

setup(
    name="proxy_information",
    version="0.1",
    description="A tool to verify proxy information.",
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