import os
from bs4 import BeautifulSoup
import glob
import pandas as pd 
from bs4 import diagnose 
if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing: " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("boardgames","")
	f = open(one_file_name, "r", encoding="utf-8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	for i in range(1,1065):
		board_table = soup.find("table", {"class": "collection_table"})
		board_rows = board_table.find_all("tr", {"id": "row_"})
		# board_rows = board_tbody.find("tr", {"id": "row_"})
		# print(board_rows)
		for r in board_rows:
		    game_rank = r.find("td", {"class": "collection_rank"}).get_text('a')
		    print(game_rank)
		    #currency_short_name = r.find("td", {"class": "currency-name"}).find("span",{"class": "curreny-symbol"}).find("a").text
		    # game_name = r.find("td", {"class": "collection_name"}).find("div",{"id": "results_objectname1"})
		    # # .find_all('a')
		    # .find_all("div",{"id": "results_objectname1"}).find_next_siblings("a")
		    # game_name = r.find("td", {"id": "CEcell_objectname1"}).find("div", {.get_text('a')
		    # print(game_name)
		    # .prettify())
		    # print(game_name)
	# table=source.find('table', {'class': 'wikitable sortable'})
	# abbs=table.find_all('b')
	# values = [ele.text.strip() for ele in abbs]
	# print(values)
	# table = source.find('table', class_='wikitable')
	# abbs = table.find_all('b')

	# abbs_list = [i.get_text().strip() for i in abbs]
	# print(abbs_list)
	# # 
	# table = source.find(class_='wikitable sortable').find_all('b')
	# b_arr = '\n'.join([x.text for x in table])
	# print(b_arr)
	# 	    game_grating = r.find("td", {"class": "collection_bggrating"})
	# 	    game_arating = r.find("td", {"class": "collection_bggrating"})
	# 	    game_voters = r.find("td", {"class": "collection_bggrating"})
	# 	    game_pricelist = r.find("td", {"class": "collection_shop"})
	#	 	#print(game_rank)
	# 	    #print(game_name)
	# 	    #print(game_grating)
	# 	    #print(currency_market_cap)
	# 	    #print(currency_price)
	# 	    #print(currency_volume)
	# 	    #print(currency_supply)
	# 	    #print(currency_change)

	# 	    df = df.append({
	# 	    	'scrapping_time': scrapping_time,
	# 	    	'name': equity_name,
	# 	    	'sector': equity_sector,
	# 	    	'price': equity_price,
	# 	    	'change': equity_change,
	# 	    	'YTD': equity_ytd,
	# 	    	'date': equity_date
	# 	    	}, ignore_index=True)
	# #print(df)
	# df.to_csv("parsed_results2/nse_dataset.csv")
