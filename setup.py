"""
DNETOOLS v2 Setup Configuration

Professional Network Intelligence Toolkit

Copyright © 2026 Anonymat Labs
Author: Mr Deh H4ck3r

Licensed under Apache License 2.0
"""


from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setup(
    name="dnetools",

    version="2.0.3",

    description=(
        "Professional Network Intelligence Toolkit "
        "for cybersecurity research and ethical hacking"
    ),

    long_description=long_description,

    long_description_content_type="text/markdown",


    author="Mr Deh H4ck3r",

    author_email="anonymatlabs@gmail.com",


    url="https://github.com/AnonymatLabs/dnetools",


    license="Apache-2.0",


    python_requires=">=3.8",


    packages=find_packages(
        include=[
            "core",
            "core.*",
            "modules",
            "modules.*",
            "providers",
            "providers.*",
            "reports",
            "reports.*",
        ]
    ),


    py_modules=[
        "dnetools"
    ],


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

        "Programming Language :: Python :: 3.8",

        "Programming Language :: Python :: 3.9",

        "Programming Language :: Python :: 3.10",

        "Programming Language :: Python :: 3.11",

        "Programming Language :: Python :: 3.12",

        "Operating System :: OS Independent",

        "Topic :: Security",

        "Topic :: System :: Networking",

        "License :: OSI Approved :: Apache Software License",

    ],


    project_urls={

        "Homepage":
            "https://anonymatlab.blogspot.com",

        "Repository":
            "https://github.com/AnonymatLabs/dnetools",

        "Issues":
            "https://github.com/AnonymatLabs/dnetools/issues",

    },

)
