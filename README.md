Pi Projector
============

Set of scripts use a Raspberry Pi as a slide player.



```
Example:
breakfast = SlideShow(name="Breakfast")
breakfast.add_slide('/home/projector/slides/breakfast.gif', 10)
breakfast.add_slide('/home/projector/slides/promo1.gif', 1)
breakfast.add_slide('/home/projector/slides/breakfast.gif', 10)
breakfast.add_slide('/home/projector/slides/promo2.gif', 1)
breakfast.build_slideshow()
```