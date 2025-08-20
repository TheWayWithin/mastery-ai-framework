"""
MASTERY-AI Framework Library Setup Configuration
A comprehensive AI optimization assessment framework
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mastery-ai",
    version="0.1.0",
    author="TheWayWithin",
    author_email="",
    description="A comprehensive AI optimization assessment framework with 148 atomic factors across 8 pillars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheWayWithin/mastery-ai-framework",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0.0",
        "numpy>=1.21.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.23.0",
        "rich>=13.0.0",
        "click>=8.0.0",
        "jinja2>=3.0.0",
        "python-multipart>=0.0.6",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "sphinx>=6.0.0",
        ],
        "viz": [
            "matplotlib>=3.5.0",
            "seaborn>=0.12.0",
            "plotly>=5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "mastery-ai=mastery_ai.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)