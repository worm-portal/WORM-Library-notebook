import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WORMdemo",
    version="0.0.4",
    author="Grayson Boyer",
    author_email="gmboyer@asu.edu",
    description="Retrieve WORM Portal demos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={},
    packages=['WORMdemo'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[],
    include_package_data=True,
    #package_data={'': ['*.r', '*.min', '*.csv']},
    zip_safe=False
)

