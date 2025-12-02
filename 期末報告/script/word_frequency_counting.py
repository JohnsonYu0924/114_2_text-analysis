import os, json
from collections import Counter


candidates = ['Han', 'Tsai', 'Soong']
mainPath = "/Users/johnsonyu/Desktop/碩二上/文字分析/總統政見發表會 資料檔/114_2_text-analysis/期末報告/tokened_data/"

for cand in candidates:
    subPath = "candidate/" + cand + "_tokened.json"
    with open(mainPath + subPath, "r", encoding="utf-8") as f:
        data = json.load(f)
        # print(data)
        
        data_count = Counter(data)
        print(f"\n---- {cand} ----")
        for i in data_count.most_common(50):
            print(i)
