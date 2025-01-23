from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("example.pyx")
)

# ! Only works on laptop, not PC for some reason