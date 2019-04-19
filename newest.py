import os
from bs4 import BeautifulSoup
import glob
import pandas as pd 


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
			# game_set.append(col.get_text())
			game_set.append(col.find(text=True).strip())
		print(game_set)




		# game_grating = r.find("td", {"class": "collection_bggrating"}).get_text('align')
		# game_arating = r.find("td", {"class": "collection_bggrating"}).get_text('align')
		# game_voters = r.find("td", {"class": "collection_bggrating"}).get_text('align')[2]
		# print(game_grating)
		# print(game_arating)
		# print(game_voters)