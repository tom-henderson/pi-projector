#!/bin/bash
# From newly installed arch linux image
# Based on instructions from
# http://www.techrepublic.com/blog/opensource/how-to-create-photo-slideshows-with-as-little-software-as-possible/3716

# update and install requred packages
pacman -Syy
pacman -S fbida ttf-inconsolata

# Set timezone
ln -sf /usr/share/zoneinfo/Pacific/Auckland /etc/localtime 
echo "Pacific/Auckland" > /etc/timezone

# Utility scripts for playing a slide and a folder of slides:
chmod +x /root/play-slide
chmod +x /root/startup-slide

# Cron file for scheduling images
mv pi-projector.cron /etc/cron.d/