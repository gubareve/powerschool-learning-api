from setuptools import setup
import os

setup(
    name="powerschoollearning",
    packages=["powerschoollearning"],
    version="1.0.1",
    description="Python library for powerschool learning.",
    author="gubareve",
    url="https://github.com/gubareve/powerschool-learning-api",
    license="LICENSE",
    long_description_content_type="text/markdown",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    install_requires=[
        open(
            os.path.join(os.path.abspath(os.path.dirname(__file__)), "requirements.txt")
        )
        .read()
        .split("\n")[:-1]
    ],
)
