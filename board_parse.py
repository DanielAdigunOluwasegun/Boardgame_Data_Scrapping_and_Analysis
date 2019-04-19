import os
from bs4 import BeautifulSoup
import glob
import pandas as pd 

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
	# board_rows = board_tbody.find("tr", {"id": "row_"})
	# print(board_rows)
	for r in board_rows:
	    game_rank = r.find("td", {"class": "collection_rank"})
	    print(game_rank.text)
	    game_name = r.find("td", {"class": "collection_objectname"}).find('div', {"id": "results_objectname1"}).find('a').text
		# if len(game_names) > 1:
		# 	game_name = game_names[1].find('href').text
		# 	print(game_name)
	    game_grating = r.find("td", {"class": "collection_bggrating"}).get_text('align')
	    game_arating = r.find("td", {"class": "collection_bggrating"}).get_text('align')
	    game_voters = r.find("td", {"class": "collection_bggrating"}).get_text('align')
	    game_pricelist = r.find("td", {"class": "collection_shop"}).find('div', {"class": "aad"}).find('div')
	 	# print(game_rank.text)
	    print(game_name)
	    print(game_grating)
	    print(game_arating)
	    print(game_voters)
	    print(game_pricelist.text)

# 	    df = df.append({
# 	    	'scrapping_time': scrapping_time,
# 	    	'Rank': game_rank,
# 	    	'Name': game_name,
# 	    	'Grating': game_grating,
# 	    	'Arating': game_arating,
# 	    	'votes': game_voters,
# 	    	'price': game_pricelist
# 	    	}, ignore_index=True)
# #print(df)
# df.to_csv("parsed_results2/board_data.csv")
