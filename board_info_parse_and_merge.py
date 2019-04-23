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
		columns = board_rows[r].find("td", {"class": "collection_rank"})
		game_set.append(columns.text.strip())
		print(game_set[0])
		columns = board_rows[r].find("td", {"class": "collection_objectname"}).find('a').text
		game_set.append(columns.strip())
		print(game_set[1])
		df = df.append({
	    	'Rank': game_set[0],
	    	'Name': game_set[1]
	    	}, ignore_index=True)
df.to_csv("parsed_results/boardgame_info_data.csv",index=False)


df1 = pd.read_csv('parsed_results/boardgame_info_data.csv')
df2 = pd.read_csv('parsed_results/boardgame_ratings_data.csv')

df_concat = pd.concat([df1, df2], axis=1)
# print(df_concat.head())
df_concat.to_csv("parsed_results/boardgame_dat.csv", index=False, encoding='utf-8')


df = pd.read_csv('parsed_results/boardgame_dat.csv')
df = df.drop(df.columns[[0]], axis=1)
df.to_csv("parsed_results/boardgame_data.csv", index=False, encoding='utf-8')


