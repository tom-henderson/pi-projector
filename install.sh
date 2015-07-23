#!/bin/bash
# From newly installed arch linux image
# Based on instructions from
# http://www.techrepublic.com/blog/opensource/how-to-create-photo-slideshows-with-as-little-software-as-possible/3716

# update and install requred packages
pacman -Syy
pacman -S fbida ttf-inconsolata python

# Set timezone
ln -sf /usr/share/zoneinfo/Pacific/Auckland /etc/localtime 
echo "Pacific/Auckland" > /etc/timezone

# Cron file for scheduling images
cp etc/cron.d/projector /etc/cron.d/projector