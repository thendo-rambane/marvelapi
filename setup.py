from distutils.core import setup

setup(
    name='marvelapiwrapper',
    version='0.1.0',
    author='T.R Rambane',
    author_email='rambane.t.r@gmail.com',
    packages=['marvelapiwrapper', 'marvelapiwrapper.tests'],
    url='https://github.com/FateXii/marvelapi',
    license='LICENSE',
    description='A marvel api wrapper',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "bs4 = *",
        "requests = *",
    ],
)
