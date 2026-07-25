"""Setup script for DNETOOLS v2."""

from setuptools import setup, find_packages

setup(
    name="dnetools",
    version="2.0.0",
    description="Modular cybersecurity and network intelligence CLI toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mr Deh H4ck3r (Daniel Edeny)",
    author_email="anonymatlabs@gmail.com",
    url="https://github.com/AnonymatLabs/dnetools",
    packages=find_packages(include=["dnetools", "dnetools.*"]),
    include_package_data=True,
    install_requires=[
        "rich>=13.7.0",
        "requests>=2.31.0",
        "dnspython>=2.5.0",
        "python-whois>=0.8.0",
        "phonenumbers>=8.13.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "dnetools=dnetools:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.8",
)
