from setuptools import setup, find_packages

setup(
    name="maze-solver",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "tk>=8.6",
    ],
    author="mln",
    author_email="martonmilan@proton.me",
    description="An automatic maze generator and solver application with GUI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/milanmarton/maze-solver",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
