import os, json, re
path_datacan = "/Users/johnsonyu/Desktop/碩二上/文字分析/總統政見發表會 資料檔/114_2_text-analysis/期末報告/tokened_data/date_candidate"
dirlist_Han = [i for i in os.listdir(path_datacan) if re.search(r"[0-9]+_Han\S+", i)]
print(dirlist_Han)

def Candi_combiner(candidate):
    path_datacan = "/Users/johnsonyu/Desktop/碩二上/文字分析/總統政見發表會 資料檔/114_2_text-analysis/期末報告/tokened_data/date_candidate/"
    patter = r"[0-9]+_" + candidate + r"\S+"
    dirlist = [i for i in os.listdir(path_datacan) if re.search(patter, i)]
    
    combine_result = []
    dataName = ""
    for data in dirlist:
        with open(path_datacan + data, 'r', encoding="utf-8") as f:
            data = re.sub(r"[0-9]+_", "", data)
            dataName = re.sub(r"_tokened", "", data)
            opened_data = json.load(f)
            for i in opened_data:
                combine_result.append(i)
    print(dataName)
    
    path_candi = "/Users/johnsonyu/Desktop/碩二上/文字分析/總統政見發表會 資料檔/114_2_text-analysis/期末報告/tokened_data/candidate/"
    with open(path_candi + data, "w", encoding="utf-8") as f:
        json.dump(combine_result, f, ensure_ascii=False, indent=4)
        print('hi')
        os.close

candidates = ['Han', 'Tsai', 'Soong']
for cand in candidates:
    Candi_combiner(cand)