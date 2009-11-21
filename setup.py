from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='adi.colortools',
      version=version,
      description="Representing and manipulating colours",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='graphics color colour',
      author='Paul-Michael Agapow',
      author_email='agapow@bbsrc.ac.uk',
      url='http://www.agapow.net/software/adi.colortools',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['adi'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
