本資料夾有下列檔案：

1. **依「場次」的逐字稿(.md)，共 4 份。**
   - 191218\_政見發表會
   - 191225\_政見發表會
   - 191227\_政見發表會
   - 191229\_辯論會

2. **"處理逐字稿.ipynb"，共 1 份。**\
   該檔案目標：
   - candiTrans(file_name, candidate_name):
     可以輸入.md 檔名和要抓的候選人名，就會跑出該場次、該候選人的發言串列，並有初步清理（"\n"），方便下一步進行 token 跟清理，有空會繼續把清理的方法寫完整。
   - 將上面結果轉為.json
   - 清理和 tokenize
   - 將上面結果批次轉為.json

3. **依「場次」、「候選人」的逐字稿(.json)，共 12 份。**\
   e.g.
   - 191218_Han
   - ...懶得打

4. **3.的_cleaned版，共12份**
   - 

4. **情緒分析辭典(.txt)，共 2 份**。
   - 正面詞無重複\_9365 詞
   - 負面詞無重複\_11230 詞
   
     來源：Lun-Wei Ku and Hsin-Hsi Chen (2007). Mining Opinions from the Web: Beyond Relevance Retrieval. Journal of American Society for Information Science and Technology, Special Issue on Mining Web Resources for Enhancing Information Retrieval, 58(12), pages 1838-1850.

5. **停用詞辭典(.txt)，共 1 份**。
