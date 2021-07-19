import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="code-fetcher",
    version="1.0.3",
    author="Mordy Waldo",
    author_email="imky171@gmail.com",
    description="A package to fetch single files from Github repos instead of cloning the whole thing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mordy-python/code-fetch",
    project_urls={
        "Bug Tracker": "https://github.com/mordy-python/code-fetch/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "code_fetch"},
    packages=setuptools.find_packages(where="code_fetch"),
    python_requires=">=3.6",
)