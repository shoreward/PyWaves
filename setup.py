from setuptools import setup

setup(name='PyWaves',
      version='0.8.1',
      description='Object-oriented library for the Waves blockchain platform',
      url='http://github.com/pywaves/pywaves',
      author='PyWaves Developers',
      author_email='dev@pywaves.org',
      license='MIT',
      packages=['pywaves'],
      keywords = ['waves', 'blockchain', 'analytics'],
      install_requires=[
	    'base58',
            'pyblake2',
            'python-axolotl-curve25519',
            'requests'
      ]
      )
