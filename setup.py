from setuptools import find_packages, setup


setup(
    name='simpleaccess',
    version="0.1",
    packages=find_packages(
        include=['simpleaccess', 'simpleaccess.*']
    ),
    scripts=['peek.py', 'translate.py'],
    install_requires=[
        'PyYAML==5.4.1',
        'gensim==4.1.2',
        'h5py==3.4.0',
        'numpy==1.21.2'
    ]
)
