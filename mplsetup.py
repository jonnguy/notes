""" Setup information for matplotlib 
	http://matplotlib.org

# There are some dependencies.. 

libpng (luckily, this can be installed with brew)
	> brew install libpng

freetype (http://download.savannah.gnu.org/releases/freetype/?C=M;O=D)
	> cd freetype
	> ./configure
	> make #this may not be necessary
	> sudo make install

matplotlib
	> cd matplotlib
	> python setup.py build
	> sudo python setup.py install


"""