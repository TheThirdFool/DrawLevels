DrawLevels
==========

DrawLevels is a python3 package to enable quickly drawing a level scheme and easilly allowing for the
slow encorporation of additional levels. The idea is that as a project goes forwards you can 
keep appending the file with new levels and transitions. This should be a lot easier than some
of the more fiddly methods that exist. It allows for exact level schemes to be easily drawn.

This is probably not ready for use in publication yet - but this should change with further updates.

Install
=======

To install use:

	pip install DrawLevels

This should give you the most up-to-date version of the package.

A note for installation - this requires the module 'pycairo' in order to render the image.
If not automatically installed, this can also be installed using:
	
	pip install pycairo

## Installation from source

The slightly more complicated but more reliable method to install DrawLevels is to install 
from source. While this sidesteps the convenience given by the package manager 'pip', it
also avoids the problems it can cause. To install first clone the GitHub repository with:

	git clone https://github.com/TheThirdFool/DrawLevels

Then enter the folder:

	cd DrawLevels

Now you can use pip to build the package from source:

	pip install .

This has the advantage of being a surefire way of ensuring installation of the most up-to-date
version of DrawLevels - as the GitHub is regularly updated. However, any further updates will
require a full repeat of this process, rather than updating via pip. 

Usage
=====

There are example level scheme scripts included in the files 'Example.py' and 'Example2.py'.
The level schemes that these produce are saved as 'ExampleLevelScheme.png' and 'ExampleLevelScheme\_2.png'.

Example.py shows the standard level scheme style with a 60Ni decay scheme + an extra few (fake) levels
in a 'branch' where the levels don't span the entire scheme. Example2.py shows the same information but
this time both the real and fake transtions are in seperate branches with only the ground level spanning
the whole diagram.

The python code must include the line:

	include DrawLevels

Then can be run with:

	python3 Example.py

More usage tips can be found on the GitHub wiki.

Thanks for using my maiden package! Enjoy!
