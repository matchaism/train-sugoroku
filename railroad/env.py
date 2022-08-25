"""
JT = {1:"東京", 2:"新橋", 3:"品川"}
JO = {17:"品川", 18:"新橋", 19:"東京", 20:"新日本橋", 21:"馬喰町", 22:"錦糸町", 23:"新小岩"}
JK = {17:"蒲田", 18:"大森", 19:"大井町", 20:"品川", 21:"高輪ゲートウェイ", 22:"田町", 23:"浜松町", 24:"新橋", 25:"有楽町", 26:"東京", 27:"神田", 28:"秋葉原", 29:"御徒町", 30:"上野", 31:"鶯谷", 32:"日暮里", 33:"西日暮里", 34:"田端", 35:"上中里", 36:"王子", 37:"東十条", 38:"赤羽"}
JY = {1:"東京", 2:"神田", 3:"秋葉原", 4:"御徒町", 5:"上野", 6:"鶯谷", 7:"日暮里", 8:"西日暮里", 9:"田端", 10:"駒込", 11:"巣鴨", 12:"大塚", 13:"池袋", 14:"目白", 15:"高田馬場", 16:"新大久保", 17:"新宿", 18:"代々木", 19:"原宿", 20:"渋谷", 21:"恵比寿", 22:"目黒", 23:"五反田", 24:"大崎", 25:"品川", 26:"高輪ゲートウェイ", 27:"田町", 28:"浜松町", 29:"新橋", 30:"有楽町"}
JC = {1:"東京", 2:"神田", 3:"御茶ノ水", 4:"四ツ谷", 5:"新宿", 6:"中野", 7:"高円寺", 8:"阿佐ヶ谷", 9:"荻窪", 10:"西荻窪"}
JB = {3:"西荻窪", 4:"荻窪", 5:"阿佐ヶ谷", 6:"高円寺", 7:"中野", 8:"東中野", 9:"大久保", 10:"新宿", 11:"代々木", 12:"千駄ヶ谷", 13:"信濃町", 14:"四ツ谷", 15:"市ヶ谷", 16:"飯田橋", 17:"水道橋", 18:"御茶ノ水", 19:"秋葉原", 20:"浅草橋", 21:"両国", 22:"錦糸町", 23:"亀戸", 24:"平井", 25:"新小岩", 26:"小岩"}
JU = {1:"東京", 2:"上野", 3:"尾久", 4:"赤羽"}
JA = {8:"大崎", 9:"恵比寿", 10:"渋谷", 11:"新宿", 12:"池袋", 13:"板橋", 14:"十条", 15:"赤羽", 16:"北赤羽", 17:"浮間舟渡"}
JJ = {1:"上野", 2:"日暮里", 3:"三河島", 4:"南千住", 5:"北千住"}
JL = {18:"北千住", 19:"綾瀬", 20:"亀戸", 21:"金町"}
JE = {1:"東京", 2:"八丁堀", 3:"越中島", 4:"潮見", 5:"新木場", 6:"葛西臨海公園"}
JS = {16:"西大井", 17:"大崎", 18:"恵比寿", 19:"渋谷", 20:"新宿", 21:"池袋", 22:"赤羽"}
TWR = {1:"新木場", 2:"東雲", 3:"国際展示場", 4:"東京テレポート", 5:"天王洲アイル", 6:"品川シーサイド", 7:"大井町", 8:"大崎"}
"""


railroad_list = ["総武線・中央線(各駅停車)", "中央線(快速)", "中央線(通勤快速)", "中央線(中央・青海特快)", "中央線(通勤特快)", "京葉線(各駅停車)", "京葉線(快速・通勤快速)", "京浜東北線(各駅停車)", "京浜東北線(快速)", "湘南新宿ライン(宇都宮線・横須賀線直通)(普通・快速)", "湘南新宿ライン(高崎線・東海道線直通)(普通・快速)", "湘南新宿ライン(高崎線・東海道線直通)(特別快速)", "山手線"]
bound_list = ["西荻窪 以西", "中野", "御茶ノ水", "新小岩・小岩 以東", "中央線快速 下り方面", "京葉線 下り方面", "赤羽 以北", "東十条", "上野", "東京", "品川", "蒲田 以南", "西大井 以南", "外回り", "内回り"]
