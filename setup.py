try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name="gsheet_api",
      version="0.1",
      author="Branden Colen",
      author_email="brandencolen@gmail.com",
      description=("Easily and efficiently manage a Google Sheet"),
      keywords="google sheet api pandas dataframe easy",
      packages=['gsheet_api'],
      url="https://github.com/brandenc40/gsheet-api")