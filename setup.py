from setuptools import setup, find_packages


setup(name='Products.ZopeVersionControl',
      version='1.0a2',
      description="Zope Version Control",
      long_description=open("CHANGES.txt").read(),
      classifiers=[
        'Framework :: Zope2',
      ],
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      url='http://pypi.python.org/pypi/Products.ZopeVersionControl',
      packages=find_packages(),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'zope.interface',
        # 'Acquisition',
        # 'DateTime',
        # 'transaction',
        # 'ZODB3',
        # 'Zope2',
      ],
      )
