from PIL import Image
import random

## import original image

org_img = Image.open("original.bmp")

## define weights randomly

wt = [(1,2,3),(3,2,1)],[(1,2,3),(3,2,1)] # rgb[2][2], 0 ~ 255

def weight_random():
	for i in range(0, 2):
		for j in range(0, 2):
			wt[i][j] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

## initialize

en_times = 5

## do encrypt en_times times

for en_times_u in range(0, en_times):

	## random weight

	weight_random()

	## zero padding

	org_img_arr = org_img.load()

	pad_img = Image.new("RGB", (org_img.size[0] + 2, org_img.size[1] + 2))

	pad_img_arr = pad_img.load()

	for i in range(0, org_img.size[0]):
		for j in range(0, org_img.size[1]):
			pad_img_arr[i + 1, j + 1] = org_img_arr[i, j]

	## cal from weight
	
	new_img = Image.new("RGB", (pad_img.size[0] - 1, pad_img.size[1] - 1))

	new_img_arr = new_img.load()

	for i in range(0, new_img.size[1]):
		for j in range(0, new_img.size[0]):
			## cal r, g, b by mult weight
			rc, gc, bc = 0, 0, 0
			for a in range(0, 2):
				for b in range(0, 2):
					rc += (pad_img_arr[j + b, i + a][0]) + wt[a][b][0]
					gc += (pad_img_arr[j + b, i + a][1]) + wt[a][b][1]
					bc += (pad_img_arr[j + b, i + a][2]) + wt[a][b][2]
					while rc >= 256:
						rc -= 256
					while gc >= 256:
						gc -= 256
					while bc >= 256:
						bc -= 256
			## assign to new img
			new_img_arr[j,i] = (rc, gc, bc)

	## hiding weight

	index = 0
	for i in range(0, 2):
		for j in range(0, 2):
			new_img_arr[new_img.size[0] - 1, index] = (int(wt[i][j][0]), 
								   					   int(wt[i][j][1]), 
								   					   int(wt[i][j][2]))
			index += 1

	## print the randomly weights and the times we encryp

	print(en_times_u + 1,
		  new_img_arr[new_img.size[0] - 1, 0],
	      new_img_arr[new_img.size[0] - 1, 1],
	      new_img_arr[new_img.size[0] - 1, 2],
	      new_img_arr[new_img.size[0] - 1, 3])

	## saving new img

	name = str(en_times_u + 1) + ".bmp"

	new_img.save(name)

	## return to front and do another time

	org_img = new_img



















