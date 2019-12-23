import bysy;

import codecs;
import os;
import sys;

from setuptools import find_packages, setup;

with open("README.md", "r") as fh:
	long_description = fh.read();

setup(
		name="bysy",
		version="1.1",
		description="Self-management time logging tool",
		long_description=long_description,
		long_description_content_type="text/markdown",
		url="https://github.com/Godje/bysy",
		author="Daniel Mayovskiy",
		author_email="daniel.mayovskiy@gmail.com",
		license="MPL 2.0",
		packages=["bysy"],
		keywords=["time", "logging", "management"],
		zip_safe=False,
		entry_points={"console_scripts": ["bysy=bysy.__main__:main"]},
		include_package_data=True,
		classifiers=[
			"Development Status :: 5 - Production/Stable",
			"Environment :: Console",
			"Intended Audience :: Developers",
			# "License :: Mozilla Public License 2.0 (MPL 2.0)",
			"Programming Language :: Python :: 2.7",
			"Topic :: Utilities"
			]
		);
