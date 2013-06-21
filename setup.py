from distutils.core import setup


setup(
    name="django-statics",
    version=__import__("statics").__version__,
    description="A reusable Django app for static files",
    long_description=open("docs/usage.txt").read(),
    author="guoqiao",
    author_email="guoqiao@gmail.com",
    url="https://github.com/guoqiao/django-statics",
    packages=[
        "statics",
        #"statics.management",
        #"statics.management.commands",
    ],
    package_dir={"statics": "statics"},
    classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
