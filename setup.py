from setuptools import setup, find_packages
setup(
  name='kanka',
  packages=find_packages(),
  version='0.1.2',
  description='An wrapper/library/whatever for the kanka.io API.',
  author='Poolitzer',
  author_email='deadpool10@web.de',
  url='https://github.com/Poolitzer/kanka',
  keywords=['python-module', 'kanka', 'kanka.io', 'REST-API'],
  classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
  install_requires=[
          'requests',
          'pytz'
      ],
)
