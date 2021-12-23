from setuptools import setup, find_packages
from pathlib import Path

# here = Path(__file__).parent.absolute()   # absolute path
# here = Path(__file__).parent.resolve

setup(
    name="franchisee",
    version="0.0.1",
    description="Data analysis of GBK Enterprise",   # optional
    long_description="""
        Data analysis of GBK Enterprise, a franchisee of eFarmers' Hub. The analysis is performed base on
        the requirements discussed during the workshop on December 22-23, 2021.
        """,
    url="https://github.com/rezaabdullah/efh-franchisee",
    author="Abdullah Reza",
    author_email="air.reza@hotmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    keywords="data analysis, data visualization",
    package_dir={"": "script"},
    packages=find_packages(include=["source", "source.*"]),
    python_requires=">= 3.6, <4",
    install_requires=[
        "pathlib==1.0.1",
        "pandas==1.3.5",
        "numpy==1.21.5",
        "jupyter",
        "jupyter-dash==0.4.0",
    ],
    extras_require={
        "interactive": ["jupyter", "jupyter-dash"],
    },
    entry_points={
        "console_scripts": ["franchisee=script.analysis:main"]
    }
)