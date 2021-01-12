from utility import diff_mask
import cv2

image = ('static/images/' + str(1) + '.png')
mask = ('static/lungs/' + str(1) + '.png')


a = diff_mask(image, mask)
