"""Allow easy installation of this package.

"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()


setup(
    name="sunrise-repos",
    version="1.0.1",
    author="Taehyun Yoon",
    author_email="taehyun.yoon.fm@gmail.com",
    description="Unarchive batches of GitHub repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/th-yoon/sunrise-repos",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click >= 7.0", "requests >= 2.22.0"],
    setup_requires=["flake8"],
    entry_points={"console_scripts": ["sunrise-repos=sunset_repos.cli:cli"]},
)
