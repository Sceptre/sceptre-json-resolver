from setuptools import setup, find_packages

__version__ = "0.0.1"

# More information on setting values:
# https://github.com/Sceptre/project/wiki/sceptre-resolver-template

# lowercase, use `-` as separator.
RESOLVER_NAME = "sceptre-resolver-template"
# One line summary description
RESOLVER_DESCRIPTION = "Resolvers to convert values to and from JSON strings"
# if multiple use a single string with comma separated names.
RESOLVER_AUTHOR = "Sceptre"
# if multiple use single string with commas.
RESOLVER_AUTHOR_EMAIL = "sceptreorg@gmail.com"
RESOLVER_URL = "https://github.com/sceptre/{}".format(RESOLVER_NAME)

with open("README.md") as readme_file:
    README = readme_file.read()

install_requirements = [
    "sceptre>=3.2",
]

test_requirements = [
    "pytest>=6.0",
]

setup_requirements = ["pytest-runner>=6.0"]

setup(
    name=RESOLVER_NAME,
    version=__version__,
    description=RESOLVER_DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    author=RESOLVER_AUTHOR,
    author_email=RESOLVER_AUTHOR_EMAIL,
    license="Apache2",
    url=RESOLVER_URL,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    py_modules=["resolver.to_json", "resolver.from_json"],
    entry_points={
        "sceptre.resolvers": [
            "from_json=resolver.from_json:FromJsonResolver",
            "to_json=resolver.to_json:ToJsonResolver",
        ]
    },
    include_package_data=True,
    zip_safe=False,
    keywords="sceptre, sceptre-resolver",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Environment :: Console",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    test_suite="tests",
    install_requires=install_requirements,
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    extras_require={"test": test_requirements},
)
