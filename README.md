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

Usage
=====

There are example level scheme scripts included in the files 'Example.py' and 'Example2.py'.
The level schemes that these produce are saved as 'ExampleLevelScheme.png' and 'ExampleLevelScheme\_2.png'.

Example.py shows the standard level scheme style with a 60Ni decay scheme + an extra few (fake) levels
in a 'branch' where the levels don't span the entire scheme. Example2.py shows the same information but
this time both the real and fake transtions are in seperate branches with only the ground level spanning
the whole diagram.

Thanks for using my maiden package! Enjoy!
