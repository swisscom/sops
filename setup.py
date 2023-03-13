"""
Packaging for sops CLI application.
"""
from pathlib import Path

from setuptools import find_packages, setup


def read_file(filename):
    """Read a text file and return its contents."""
    project_home = Path(__file__).parent.resolve()
    return (project_home / filename).read_text(encoding="utf-8")


setup(
    name="sops",
    version="1.18",
    author="Julien Vehent",
    author_email="jvehent@mozilla.com",
    description="Secrets OPerationS (sops) is an editor of encrypted files",
    license="MPL",
    keywords=["mozilla", "secret", "credential", "encryption", "aws", "kms"],
    url="https://github.com/mozilla/sops",
    packages=find_packages(),
    zip_safe=True,
    long_description=read_file("README.rst"),
    long_description_content_type="text/x-rst",
    python_requires=">=3.7",
    install_requires=[
        "cryptography>=1.4",
        "ruamel.yaml>=0.11.7",
    ],
    extras_require={
        "aws": [
            "boto3>=1.1.3",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={"console_scripts": ["sops = sops:main"]},
)
