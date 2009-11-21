#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
A class for representing colours.

Long description.

"""
# Created by Paul-Michael Agapow on 2009-11-19.

__docformat__ = 'restructuredtext en'



### IMPORTS ###

import colorsys
import types

from adi.colortools import impl

__all__ = [
	'RgbColor',
]


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

class RgbColor (impl.ReprObj):
	"""
	
	"""
	
	_repr_fields = [
		'red',
		'green',
		'blue',
		'alpha',
	]
	
	## Lifecycle
	def __init__ (self, color_spec=None):
		"""
		Class c'tor.
		
		:Parameters:
			color_spec
				A 3- or 4-tuple of ints or floats.
		
		"""
		# set to safe values
		self.red = self.green = self.blue = 0
		self.alpha = 1.0
		# initialise from color specification
		if (color_spec is None):
			# default
			pass
		elif (hasattr (color_spec, '__len__')):
			# if passed a sequence
			self._init_from_rgb_tuple (color_spec)
		elif (isinstance (color_spec, basestring)):
			# if passed a string
			if (color_spec.starts_with ('#')):
				# ... a hex string
				self._init_from_hexstring (color_spec[1:])
			else:
				# ... a color name
				self._init_from_name (color_spec)
		else:
			# shouldn't get here
			raise ValueError (
				"unrecognised color specification '%s'" % color_spec)
				
	## INTERNAL 
	def _init_from_rgb_tuple (self, color_spec):
		"""
		Initialise color from an RGB triplet, integer or float.
		"""
		# do we have a 3- or 4-tuple?
		if (len (color_spec) == 3):
			# ... an rgb triplet
			triplet = color_spec
		elif (len (color_spec) == 4):
			# ... an rgba quadruplet
			triplet = color_spec[:3])
			self.alpha = color_spec[3]
		else:
			# shouldn't get here
			raise ValueError (
				"rgb tuple '%s' should have 3 or 4 elements" % color_spec)
		# are they int or floats?
		val_types = [is_int (x) for x in triplet]
		if (False in val_types):
			# spec contains floats, check & convert
			self._validate_float_color_value (color_spec)
			triplet = [int (x*255 + 0.5) for x in color_spec]
		else:
			# spec contains ints, check
			self._validate_ints_color_value (color_spec)
			triplet = color_spec
		# set values
		self.red, self.green, self.blue = triplet[0], triplet[1], triplet[2]

	def _init_from_hexstring (self, hexstrn):
		"""
		Initialise color from an hexidecimal string.
		"""
		if hexstrn.startswith ('#'):
			hexstrn = hexstrn[1:]
		# allow for one or two characters per channel or wider
		len_strn = len (hexstrn)
		assert (len_strn % 3 == 0), \
			"hex string '%s' cannot be divided evenly into three channels"
		width = len_strn / 3
		channels = [hexstrn[x*3:(x+1)*3] for x in range(3)]
		channels = [int (x, 16) for x in channels]
		adjust = math.pow (16, 2-width)
		channels = [int (x * channel) for x in channels]
		

	def _validate_int_color_value (self, triplet):
		"""
		Assert that color values are in the correct range (0-255).

		Used in initialisation.
		"""
		for val in triplet:
			assert (0 <= val <= 255), \
				"color value '%s' is outside allowed range 0-255" % val

	def _validate_float_color_value (triplet):
		"""
		Assert that color values are in the correct range (0.0-1.0).

		Used in initialisation.
		"""
		for val in triplet:
			assert (0.0 <= val <= 1.0), \
				"color value '%s' is outside allowed range 0.0-1.0" % val
				
				
	@classmethod
	def from_rgb (cls, color_spec):
		new_clr = cls()
		new_clr._init_from_rgb_tuple (color_spec)
		return new_clr
		
	
	## Accessors
	def to_rgb (self):
		return (self.red, self.green, self.blue)
		
	to_rgb256 = to_rgb
		
	def to_rgba (self):
		return (self.red, self.green, self.blue, self.alpha)
		
	to_rgba256 = to_rgba

	def to_rgbfloat (self):
		"""
		Return the colour as a triplet of floats, from 0 to 0.1.
		"""
		triplet = [x/255.0 for x in self.to_rgb256 ()]
		return tuple (triplet)
		
	def to_rgbafloat (self):
		"""
		Return the colour as a 4-tuple of floats, from 0 to 0.1, followed by the alpha.
		"""
		triplet = [x/255.0 for x in self.to_rgb256 ()]
		return tuple (triplet)
		
	def to_hls (self):
		return colorsys.rgb_to_hls (*self.to_rgbfloat())
		
	def to_yiq (self):
		return colorsys.rgb_to_yiq (*self.to_rgbfloat())

	def to_hsv (self):
		return colorsys.rgb_to_hsv (*self.to_rgbfloat())
		
	def to_cmyk ():
		# TODO: check
		c = 1.0 - (self.red / 255.0)
		m = 1.0 - (self.green / 255.0)
		y = 1.0 - (self.blue / 255.0)
		k = min (c, m, y, 1.0)
		
		c = (C - k) / (1 - k)
		m = (M - k) / (1 - k)
		y = (Y - k) / (1 - k)
		
		return c * 100, m * 100, y * 100, k * 100


### UTILITIES

def is_int (val):
	"""
	Is this value an integer or integer-like?
	
	This is needed for sniffing out the type of color specifications, telling
	RGB integer triplets (e.g. 15, 127, 0) from float triplets (e.g. 0.058,
	0.49, 0.0). If we just test for type, specialised types like those in Numpy
	(e.g. unsigned shorts) might fail. So we test by using the mod operation as
	well, which has the different failing that "round" floats (e.g. 0.0 and
	1.0) will test True
	"""
	return (type (val) == types.IntType) or (val % 1 == 0))


### TEST & DEBUG ###

def _doctest ():
    import doctest
    doctest.testmod()


### MAIN ###

if __name__ == '__main__':
    _doctest()


### END ######################################################################
