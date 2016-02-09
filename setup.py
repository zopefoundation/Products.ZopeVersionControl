from setuptools import setup, find_packages

__version__ = '1.1.4dev'

setup(
    name='Products.ZopeVersionControl',
    version=__version__,
    description="Zope Version Control",
    long_description=(open('README.rst').read() + "\n" +
                      open('CHANGES.rst').read()),
    classifiers=[
        'Framework :: Zope2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    license='ZPL',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='https://pypi.python.org/pypi/Products.ZopeVersionControl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.interface',
        'Acquisition',
        'DateTime',
        'transaction',
        'ZODB3',
        'Zope2',
    ],
)
