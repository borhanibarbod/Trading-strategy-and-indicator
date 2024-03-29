from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='indicator',
  version='0.0.1',
  description='simple trading strategy',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Barbod Borhani',
  author_email='barbod.borhani@bahcesehir.edu.tr',
  license='MIT',
  classifiers=classifiers,
  keywords='indicator',
  packages=find_packages(),
  install_requires=['']
)