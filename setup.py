from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in emails/__init__.py
from emails import __version__ as version

setup(
	name="emails",
	version=version,
	description="email",
	author="shinil",
	author_email="shinilshinu97@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
