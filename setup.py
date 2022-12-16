from setuptools import find_packages
from setuptools import setup


version = '3.1.0'

setup(
    name='Products.ZopeVersionControl',
    version=version,
    description="Zope Version Control",
    long_description=(open('README.rst').read() + "\n" +
                      open('CHANGES.rst').read()),
    classifiers=[
        'Development Status :: 6 - Mature',
        'Framework :: Zope :: 4',
        'Framework :: Zope :: 5',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='version control',
    license='ZPL 2.1',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='https://github.com/zopefoundation/Products.ZopeVersionControl',
    project_urls={
        'Issue Tracker': ('https://github.com/zopefoundation/'
                          'Products.ZopeVersionControl/issues'),
        'Sources': ('https://github.com/zopefoundation/'
                    'Products.ZopeVersionControl'),
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
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
