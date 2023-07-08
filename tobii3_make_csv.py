import csv
import statistics

GAZE_DATA = "./2022-04-22assistant/gazedata"
CSV_TS = "./2022-04-22assistant/gaze_timestamp.csv"
CSV_FR = "./2022-04-22assistant/gaze_frame.csv"

label_ts = ["timestamp", "x", "y"]
label_fr = ["frame", "x", "y"]
elements_ts = list()
elements_fr = list()

def make_ts_csv():
	with open(GAZE_DATA, "r") as f:
		for data in f:
			data = data.strip("\n")
			data = eval(data)
			if len(data["data"]) != 0:
				element = {"timestamp" : data["timestamp"],
					    "x" : data["data"]["gaze2d"][0],
					    "y" : data["data"]["gaze2d"][1]}
			else:
				element = {"timestamp" : data["timestamp"],
					    "x" : 0,
					    "y" : 0}
			elements_ts.append(element)
			
	with open(CSV_TS, "w", newline="") as c:
		writer = csv.DictWriter(c, fieldnames=label_ts)
		writer.writeheader()
		writer.writerows(elements_ts)

	return elements_ts

def make_fr_csv(elements_ts):
	for i in range(int(len(elements_ts) / 4) + 1):
		x_list = list()
		y_list = list()
		count = 0
		while count < 4:
			try:
				gaze_x = elements_ts[i * 4 + count]["x"]
				gaze_y = elements_ts[i * 4 + count]["y"]
				count += 1
			except IndexError:
				count = 4
			if gaze_x != 0 and gaze_y != 0:
				x_list.append(gaze_x)
				y_list.append(gaze_y)
		if len(x_list) == 0 and len(y_list) == 0:
			med_x = 0
			med_y = 0
		else:
			med_x = statistics.median(x_list)
			med_y = statistics.median(y_list)
		frame = {"frame" : i + 1, "x" : med_x, "y" : med_y}
		elements_fr.append(frame)

	with open(CSV_FR, "w", newline="") as e:
		writer = csv.DictWriter(e, fieldnames=label_fr)
		writer.writeheader()
		writer.writerows(elements_fr)

ts = make_ts_csv()
make_fr_csv(ts)
