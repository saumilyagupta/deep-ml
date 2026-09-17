
def calculate_brightness(img):
	
	if not img or not img[0]:
    	return -1
	expected_len = len(img[0])
	total_val = 0
	total_pixal = 0

	for row in img:
		if len(row) != expected_len:
			return -1
		
		for pixal in row:
			if not (0 <= pixal <=255):
				return  -1
			total_pixal +=1
			total_val += pixal
	return round(total_val/total_pixal, 2)
	
