from setuptools import setup

setup(
   name='bark',
   version='0.1.0',
   packages=['bark'],
   install_requires=['encodec', 'funcy', 'tqdm', 'transformers']
)
