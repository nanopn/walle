from time import time

import cv2

class Camera(object):


    def __init__(self):
        # Camera 0 is the integrated web cam on my netbook
        self.camera_port = 0

        # Number of frames to throw away while the camera adjusts to light levels
        self.ramp_frames = 3


        # Now we can initialize the camera capture object with the cv2.VideoCapture class.
        # All it needs is the index to a camera port.
        self.camera = cv2.VideoCapture(self.camera_port)

        # Captures a single image from the camera and returns it in PIL format
    def get_image(self):
        # read is the easiest way to get a full image out of a VideoCapture object.
        retval, im = self.camera.read()
        return im


    def get_frame(self):
        return self.get_image


    def get_image_tostring(self):
        for i in range(self.ramp_frames):
            temp = self.get_image()
        # read is the easiest way to get a full image out of a VideoCapture object.
        retval, im = self.camera.read()
        if retval:
            return im.tostring()

    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
        for i in range(self.ramp_frames):
            temp = self.get_image()
        print("Taking image...")
        # Take the actual image we want to keep
        camera_capture = self.get_image()
        file = 'images/test_image_%s.jpg' % (time())
        # A nice feature of the imwrite method is that it will automatically choose the
        # correct format based on the file extension you provide. Convenient!
        cv2.imwrite(file, camera_capture)
        # You'll want to release the camera, otherwise you won't be able to create a new
        # capture object until your script exits
        #del(self.camera)
        return open(file, 'rb').read()