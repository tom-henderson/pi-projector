#!/usr/bin/python
# This script is run on startup
# Use it to configure which slideshow to start playing
# based on the time of day.

from datetime import datetime
import subprocess

current_time = datetime.now()

slideshow = 'Default'

if current_time.hour >= 12:
    slideshow = 'Alternate'

play_slideshow_command = '/opt/projector/play-slide-show {}'.format(slideshow)

subprocess.call(
    play_slideshow_command,
    shell=True
)
