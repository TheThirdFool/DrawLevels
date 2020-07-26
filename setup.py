
import setuptools
with open("README.md", "r") as fh:
	long_description = fh.read()


setuptools.setup(
	name='DrawLevels',  
	version='0.2.8',
	packages=['DrawLevels'] ,
	author="TheThirdFool",
	author_email="danielfh.dfh@gmail.com",
	url = "https://github.com/TheThirdFool/DrawLevels",
	description="A package for quickly generating simple nuclear level schemes.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	install_requires=['pycairo'],
	keywords="Nuclear Physics Level Scheme",
	#packages=setuptools.find_packages(),
	classifiers=[
	    "Programming Language :: Python :: 3",
	    "Programming Language :: Python :: 3.6",
	    "Programming Language :: Python :: 3.7",
	    "Programming Language :: Python :: 3.8",
	    "License :: OSI Approved :: MIT License",
	    "Operating System :: OS Independent",
	],
)



