#!/usr/bin/env python
from distutils.core import setup

setup(name='dec2bin',
      version='1.0',
      description='Turn decimal into binary',
      author='Andre Rossi Korol',
      author_email='anrobits@yahoo.com.br',
      maintainer='Andre Rossi Korol',
      maintainer_email='anrobits@yahoo.com.br',
      url='https://github.com/andrekorol/dec2bin',
      py_modules=['dec2bin'],
      license='GNU GPLv3',
      platforms='POSIX, MacOS, Windows',
      long_description='dec2bin is a Python function that takes an integer or floating '
                       'point as parameter and returns the binary representation of that number.',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Framework :: IDLE',
          'Framework :: IPython',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
      )
