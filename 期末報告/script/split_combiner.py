import os, json, re
# with open("/Users/johnsonyu/Desktop/碩二上/文字分析/總統政見發表會 資料檔/114_2_text-analysis/期末報告/cleaned_data/191218_Han_cleaned.json", "r", encoding="utf-8") as f:
#     f = json.load(f)
#     myText = " ".join(f)
# print(myText)

path = "/Users/johnsonyu/Desktop/碩二上/文字分析/總統政見發表會 資料檔/114_2_text-analysis/期末報告/raw_data/"
os.chdir(path)
dirList = [i for i in os.listdir(path) if i.endswith(".json")]
print(dirList)

def combiner(data_name, savefolder_path):
    with open(data_name, "r", encoding="utf-8") as f:
        f = json.load(f)
        myText = " ".join(f)
        data_name = re.sub(r".json", "_combine.txt", data_name)
    with open(savefolder_path + data_name, "w", encoding="utf-8") as f:
        f.write(myText)
        
        
path = "/Users/johnsonyu/Desktop/碩二上/文字分析/總統政見發表會 資料檔/114_2_text-analysis/期末報告/raw_data/combine/"
for i in dirList:
    print(i)
    combiner(i, path)