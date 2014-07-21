import setuptools

setuptools.setup(
    name="pytest-django-casperjs",
    version="0.1.0",
    url="https://github.com/EnTeQuAk/pytest-django-casperjs",
    author="Christopher Grebs",
    author_email="cg@webshox.org",
    description="Integrate CasperJS with your django tests as a pytest fixture",
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)