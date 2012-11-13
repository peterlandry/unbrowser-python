from distutils.core import setup
 
 
setup(
    name = "unbrowser-python",
    version = __import__("unbrowser").__version__,
    author = "Peter Landry",
    author_email = "peter.landry@gmail.com",
    description = "A python client library for Unbrowser.",
    long_description = open("README.md").read(),
    license = "BSD",
    url = "https://github.com/peterlandry/unbrowser-python/",
    packages = [
        "unbrowser",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ]
)