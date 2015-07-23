import os


class SlideShow(object):
    def __init__(self, working_dir=None, name=None):
        if name is None:
            raise Exception("Slideshow must be named.")
        self.name = name

        if not working_dir:
            working_dir = "/opt/projector/slideshows"

        if not os.path.exists(working_dir):
            raise Exception(
                "Working directory {} does not exist.".format(working_dir)
                )
        self.working_dir = working_dir

        self.path = os.path.join(self.working_dir, self.name)
        self._slides = []

    def add_slide(self, file=None, duration=None):
        if file is None or duration is None:
            raise Exception("Must enter file path and duration in multiples of 30s for each slide.")

        if not os.path.exists(file):
            raise Exception("File {} doesn't exist.".format(file))

        self._slides.append({
            "file": file,
            "duration": duration
        })

    def build_slideshow(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        else:
            # Delete all contents:
            for file in os.listdir(self.path):
                path = os.path.join(self.path, file)
                os.unlink(path)

        for n, slide in enumerate(self._slides):
            # create a symlink for each slide in self.path
            # for each 30 second period
            for i in range(slide["duration"]):
                os.symlink(
                    slide["file"],
                    os.path.join(
                        self.path,
                        "{}-{}-{}".format(
                            n,
                            i,
                            os.path.split(slide["file"])[1]
                        )
                    )
                )

    def delete_slideshow(self):
        if os.path.exists(self.path):
            for file in os.listdir(self.path):
                path = os.path.join(self.path, file)
                os.unlink(path)
                os.rmdir(self.path)
