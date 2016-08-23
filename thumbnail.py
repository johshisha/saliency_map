from src.saliency_map import SaliencyMap
from src.utils import OpencvIo
import numpy, cv2, sys

image = 'images/otumami3.jpg'

oi = OpencvIo()
src = oi.imread(image)
sm = SaliencyMap(src)
oi.imshow_array([sm.map])

height, width = sm.map.shape

h = height / 4
w = width / 4

thumb = numpy.array([])
max_score = 0.0

for i in range(3):
	for j in range(3):
		im = sm.map[h*i:h*(i+2), w*j:w*(j+2)]
		print im.mean()
		if im.mean() > max_score:
			max_score = im.mean()
			thumb = src[h*i:h*(i+2), w*j:w*(j+2),:]


oi.imshow(thumb)

