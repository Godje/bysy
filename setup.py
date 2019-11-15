from setuptools import setup;
import bysy;

setup(
		name="bysy",
		version="0.9.2",
		description="Self-management time logging tool",
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
			"Intended Audience :: Developers",
			# "License :: Mozilla Public License 2.0",
			# "Programming Language :: Python :: 2.7.15"
			]
		);
