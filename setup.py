from setuptools import setup

requires_list = [
    'colorama==0.2.7',
    'coverage==3.7.1',
    'mock==1.0.1',
    'nose==1.3.0',
    'rauth==0.6.2',
    'requests==1.2.3',
]

setup(name='buffer-python',
      version='1.07',
      platforms='any',
      description='Python library for Buffer App',
      author='Vlad Temian',
      author_email='vladtemian@gmail.com',
      url='https://github.com/bufferapp/buffer-python',
      packages=['buffpy', 'buffpy.managers', 'buffpy.models'],
      include_package_data=True,
      install_requires=requires_list,
      classifiers=[
          'Programming Language :: Python :: 2.7',
      ]
)
