#!/usr/bin/env python3
"""
Setup script for Emoji PDF Generator
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="emoji-pdf-generator",
    version="1.0.0",
    author="Giuseppe Vitolo",
    author_email="vitologiuseppe17@gmail.com",
    description="A Python tool to generate PDFs with full emoji support",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/GiuseppeVitolo17/Emoji-PDF-Generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Documentation",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "emoji-pdf-generator=emoji_pdf_generator:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["examples/*.html", "examples/*.css", "examples/README.md"],
    },
    keywords="pdf emoji html weasyprint unicode ai assistant chatgpt claude gemini python pdf-generation emoji-support unicode-pdf html-to-pdf weasyprint-pdf emoji-rendering pdf-tool python-pdf emoji-pdf generator tool library",
    project_urls={
        "Bug Reports": "https://github.com/GiuseppeVitolo17/Emoji-PDF-Generator/issues",
        "Source": "https://github.com/GiuseppeVitolo17/Emoji-PDF-Generator",
        "Documentation": "https://github.com/GiuseppeVitolo17/Emoji-PDF-Generator#readme",
    },
)
