import cv2
import glob
import pandas as pd

def comb_movie(movie_files, out_path):
	fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
	movie = cv2.VideoCapture(movie_files[0])
	fps = movie.get(cv2.CAP_PROP_FPS)
	height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
	width = movie.get(cv2.CAP_PROP_FRAME_WIDTH)

	out = cv2.VideoWriter(out_path, int(fourcc), fps, (int(width), int(height)))

	for movies in movie_files:
		print(movies)
		movie = cv2.VideoCapture(movies)
		if movie.isOpened() == True:
			ret, frame = movie.read()
		else:
			ret = False

		while ret:
			out.write(frame)
			ret, frame = movie.read()

def concat_csv(files, out_path):
	for file_name in files:
		print(file_name)
	data_list = list()
	for data in files:
		data_list.append(pd.read_csv(data))
	df = pd.concat(data_list, axis=0, sort=True)
	
	df.to_csv(out_path, index=False)


ROOT_DIR = "..//20220802_main/"

files = sorted(glob.glob(ROOT_DIR + "*.mp4"))
out_path = ROOT_DIR + "fullstream.mp4"
comb_movie(files, out_path)

files = sorted(glob.glob(ROOT_DIR + "*.csv"))
concat_csv(files, ROOT_DIR + "gaze_concat.csv")
