# Always prefer setuptools over distutils
from setuptools import setup

setup()

# Create package
# python setup.py bdist_wheel
# twine upload dist/*  (This is official repo)

# Bump version
# Make sure you update the install location in the install section of the documentation.
# Update Changelog release
# bumpversion major/minor/patch --allow-dirty
# git push origin [0.1.0]
# On Github, go to tags and use the GUI to push a Release.

