from setuptools import setup, find_packages

__version__ = '2.0.0'

setup(
    name='Products.ZopeVersionControl',
    version=__version__,
    description="Zope Version Control",
    long_description=(open('README.rst').read() + "\n" +
                      open('CHANGES.rst').read()),
    classifiers=[
        'Development Status :: 6 - Mature',
        'Framework :: Zope :: 2',
        'Framework :: Zope :: 4',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='version control',
    license='ZPL',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='https://pypi.org/project/Products.ZopeVersionControl/',
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
        'six',
        'ZODB',
        'Zope2',
    ],
    entry_points={
        'zodbupdate.decode': [
            'decodes = Products.ZopeVersionControl:zodbupdate_decode_dict',
        ],
    },
)
