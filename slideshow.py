#!/bin/python

import os

WORKING_DIRECTORY = "/home/pi/menus/slides/slideshows/"

class SlideShow(object):
	def __init__(self, working_dir=None, name=None):
		if name is None:
			raise Exception("Slideshow must be named.")
		self.name = name

		if not os.path.exists(working_dir):
			raise Exception("Working directory {} does not exist.".format(working_dir))
		self.working_dir = working_dir
		
		self._slides = []

	def add_slide(self, file=None, duration=None):
		if file is None or duration is None:
			raise Exception("Must enter file path and duration in multiples of 30s for each slide.")

		self._slides.append({
			"file": file,
			"duration": duration
		})

	def build_slideshow(self):
		_path = os.path.join(self.working_dir, self.name)
		
		if not os.path.exists(_path):
			os.makedirs(_path)
		else:
			# delete all symlinks from _path

		for n, slide in enumerate(self._slides):
			# create a symlink for each slide in _path for each 30 second period, like:
			# /1-1-file1.gif
			# /1-2-file1.gif
			# /2-1-file2.gif
			for i in range(slide["duration"]):
				os.symlink(
					slide["file"], 
					os.path.join(
						_path,
						"{}-{}-{}".format(
							n,
							i,
							os.path.split(slide["file"])[1]
						)
					)
				)	