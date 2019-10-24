from setuptools import setup;
import bysy;

setup(
		name="bysy",
		version="0.3",
		description="Self-management time logging tool",
		url="https://github.com/Godje/bysy",
		author="Daniel Mayovskiy",
		author_email="daniel.mayovskiy@gmail.com",
		license="MIT",
		packages=["bysy"],
		zip_safe=False,
		entry_points={"console_scripts": ["bysy=bysy.__main__:main"]},
		include_package_data=True
		);
