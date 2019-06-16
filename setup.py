from setuptools import find_packages, setup


def read(filename):
    with open(filename) as f:
        return f.read()

setup(name='cannycam',
      version='0.0.1',
      description='A facial and anatomical recognition program',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Image Recognition'
      ],
      url='http://github.com/cooltoast/CannyCam',
      author='cooltoast',
      license='MIT',
      packages=find_packages(),
      install_requires=read('requirements.txt').splitlines(),
      entry_points={
          'console_scripts': [
              'cannycam=cannycam.cannycam:main',
              'haarcam=cannycam.haarcam:main',
              'cannyhaarcam=cannycam.cannyhaarcam:main'
          ]
      },
      include_package_data=True,
      zip_safe=False)
