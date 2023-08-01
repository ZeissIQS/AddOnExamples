# -*- coding: utf-8 -*-

import gom
import cv2
import numpy as np

def get_image ():
	measurement = gom.app.project.measurement_series['Scan 1'].measurements['M1']
	acquisition = gom.api.project.get_image_acquisition (measurement, 'left camera',[0])[0]

	image = np.array (measurement.images['left camera'].data.rgb )[0]
	return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def image_to_png (image):
	_, data = cv2.imencode(".png", image)
	return data.tobytes()

DIALOG=gom.script.sys.create_user_defined_dialog (file='display_image.gdlg')

image = get_image ()

DIALOG.image.data = image_to_png (cv2.resize (image, (1024, 768)))

gom.script.sys.show_user_defined_dialog (dialog=DIALOG)


