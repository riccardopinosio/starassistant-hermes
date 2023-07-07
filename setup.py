"""Setup script for starassistant-hermes package"""
from pathlib import Path

import setuptools

this_dir = Path(__file__).parent

# -----------------------------------------------------------------------------

# Load README in as long description
long_description: str = ""
readme_path = this_dir / "README.rst"
if readme_path.is_file():
    long_description = readme_path.read_text(encoding="utf-8")

requirements_path = this_dir / "requirements.txt"
with open(requirements_path, "r", encoding="utf-8") as requirements_file:
    requirements = requirements_file.read().splitlines()

version_path = this_dir / "VERSION"
with open(version_path, "r", encoding="utf-8") as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name="starassistant-hermes",
    version=version,
    author="Michael Hansen",
    author_email="mike@rhasspy.org",
    url="https://github.com/riccardopinosio/starassistant-hermes",
    packages=setuptools.find_packages(),
    package_data={"rhasspyhermes": ["py.typed"]},
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    python_requires=">=3.7",
)
