from setuptools import setup, find_packages

setup(
    name="mcleod-tms-client",
    version="0.1.0",
    description="Python client for McLeod TMS API",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    py_modules=["tms_client"],
    package_data={
        "": ["py.typed", "*.pyi"],
    },
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Typing :: Typed",
    ],
)
