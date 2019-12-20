import bysy;

import codecs;
import os;
import re;
import sys;

from setuptools import find_packages, setup;

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

long_description = read('README.rst');

setup(
		name="bysy",
		version="1.0",
		description="Self-management time logging tool",
		long_description=long_description,
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
			"Development Status :: 4 - Beta",
			"Environment :: Console",
			"Intended Audience :: Developers",
			"License :: Mozilla Public License 2.0",
			"Programming Language :: Python :: 2.7.15",
			"Topic :: Time Tracking"
			]
		);
