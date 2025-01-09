from setuptools import setup

setup(name='NetComp2',
      version='0.0.1',
      description='Network Comparison 2',
      license='MIT',
      author='Peter Wills, Kai Streiling',
      author_email='peter.e.wills@gmail.com, kai.streiling@gmail.com',
      packages=[
          'netcomp2',
          'netcomp2.linalg',
          'netcomp2.distance'
      ],
      url='https://github.com/uvest/NetComp',
      install_requires=[
          'numpy>=1.11.3',
          'scipy>=0.18',
          'networkx>=3.0.0'
      ]
     )
