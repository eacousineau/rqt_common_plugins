#1/usr/bin/env python
from setuptools import setup
import sys
sys.path.insert(0, 'src')

setup(name='robot_monitor',
      version= '0.1.0',
      packages=['robot_monitor'],
      package_dir = {'':'src'},
      install_requires=[],
      author = "Ze'ev Klapow", 
      author_email = "zklapow@willowgarage.com",
      url = "",
      download_url = "", 
      keywords = [],
      classifiers = [
        "Programming Language :: Python", 
        "License :: OSI Approved :: BSD License" ],
      description = "",
      long_description = "",
      license = "BSD"
      )
