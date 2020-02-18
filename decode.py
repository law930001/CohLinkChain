from PIL import Image

## initialize

de_times = 5

name_load = str(de_times) + ".bmp"

## import img

org_img = Image.open(name_load)

## start decoding 

for de_times_u in range(0, de_times):

	org_img_arr = org_img.load()

	## get weights

	wt = [(0,0,0),(0,0,0)],[(0,0,0),(0,0,0)]

	index = 0
	for i in range(0,2):
		for j in range(0,2):
			wt[i][j] = (org_img_arr[org_img.size[0] - 1, index][0],
				        org_img_arr[org_img.size[0] - 1, index][1],
				        org_img_arr[org_img.size[0] - 1, index][2])
			index += 1

	## left and top padding the img

	pad_img = Image.new("RGB", (org_img.size[0], org_img.size[1]))

	pad_img_arr = pad_img.load()

	## decode the img

	for i in range(0, pad_img.size[1] - 1):
		for j in range(0, pad_img.size[0] - 1):
			## cal r, g, b weights
			ro, go, bo = org_img_arr[j,i][0], org_img_arr[j,i][1], org_img_arr[j,i][2]
			rc, gc, bc = 0, 0, 0
			for a in range(0, 2):
				for b in range(0, 2):
					rc += wt[a][b][0] + (pad_img_arr[j + b, i + a][0])
					gc += wt[a][b][1] + (pad_img_arr[j + b, i + a][1])
					bc += wt[a][b][2] + (pad_img_arr[j + b, i + a][2])
			## assign to bot-right
			while ro < rc:
				ro += 256
			while go < gc:
				go += 256
			while bo < bc:
				bo += 256
			pad_img_arr[j + 1, i + 1] = (ro - rc, go - gc, bo - bc)

	## delete left and top padding

	new_img = Image.new("RGB", (pad_img.size[0] - 1, pad_img.size[1] - 1))

	new_img_arr = new_img.load()

	for i in range(0, new_img.size[0]):
		for j in range(0, new_img.size[1]):
			new_img_arr[i,j] = pad_img_arr[i + 1, j + 1]

	name_save = str(de_times - de_times_u) + "_docoded.bmp"

	new_img.save(name_save)

	print(str(de_times - de_times_u) + "_decoded done ...")

	## return to next times

	org_img = new_img



