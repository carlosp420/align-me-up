import setuptools

setuptools.setup(
    name="alignme",
    version="0.0.0",
    url="https://github.com/carlosp420/align-me-up",

    author="Carlos Pena",
    author_email="mycalesis@gmail.com",

    description="Take a FASTA file and generate alignments based on gene and consensus sequences for same gene and same individual.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
