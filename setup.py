from setuptools import setup, find_packages

setup(
    name="django-statics",
    version='0.1.0',
    description="A reusable Django app for static files",
    long_description=open("README.md").read(),
    author="guoqiao",
    author_email="guoqiao@gmail.com",
    license="MIT",
    keywords="django",
    url="https://github.com/guoqiao/django-statics",
    packages=find_packages(),
    include_package_data=True,
)
