import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="remote-cirq",
    version="0.0.3",
    author="Floq Team",
    author_email="floq-devs@google.com",
    description="Cirq based client for running quantum circuits on the "
                "cloud with the Floq Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'cirq>=0.9.1',
        'requests>=2.24.0',
        'marshmallow>=3.10.0',
        'marshmallow-dataclass>=8.3.1',
        'marshmallow-enum>=1.5.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
