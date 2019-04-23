import os
from bs4 import BeautifulSoup
import glob
import pandas as pd 
import csv
if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing: " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("boardgames","")
	f = open(one_file_name, "r", encoding="utf-8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	board_table = soup.find("table", {"class": "collection_table"})
	board_rows = board_table.find_all("tr", {"id": "row_"})
	for r in range(len(board_rows)):
		game_set = []
		columns = board_rows[r].find_all("td", {"class": "collection_bggrating"})
		for col in columns:
			game_set.append(col.find(text=True).strip())
		print(game_set[0])
		print(game_set[1])
		print(game_set[2])
		df = df.append({
	    	'Grating': game_set[0],
	    	'Arating': game_set[1],
	    	'votes': game_set[2]
	    	}, ignore_index=True)
df.to_csv("parsed_results/boardgame_ratings_data.csv",index=False)





