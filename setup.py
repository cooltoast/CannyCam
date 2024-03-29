from setuptools import find_packages, setup

import versioneer


def read(filename):
    with open(filename) as f:
        return f.read()


setup(
    name="cannycam",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="A facial and anatomical recognition program",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    url="http://github.com/cooltoast/CannyCam",
    author="cooltoast",
    license="MIT",
    packages=find_packages(),
    install_requires=read("requirements.txt").splitlines(),
    extras_require={"docs": read("docs_requirements.txt").splitlines()},
    entry_points={
        "console_scripts": [
            "cannycam=cannycam.cannycam:main",
            "haarcam=cannycam.haarcam:main",
            "cannyhaarcam=cannycam.cannyhaarcam:main",
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
