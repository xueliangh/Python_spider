import requests  # 使用requsts套件

## Write File
path = "htmlTest.txt"  # 你檔案想要存放的檔名，如果沒給路徑、直接寫檔名，將存在與你現在所執行的python檔同一個資料夾中
file = open(path, 'w', encoding='utf8')  
# 第一個參數(path): 如果該路徑下，有相同檔名的檔案，將會直接複寫且不可回復。若沒有，系統則會自動幫你開一個新檔案
# 第二個參數('w'): 一般來說，我只用到'w'以及'r'，分別是'寫'與'讀'的意思，其他二進位檔案的讀寫方式，各位有興趣可以自行去研究。如果要讀檔案，直接把'w'改成'r'即可。
# 第三個參數(encoding='utf8'): 指的是開啟這個檔案所使用的編碼，因為windows如果是中文版的，預設打開編碼是cp950(滿討厭的)，所以在寫入檔案的時候，最好用utf8編碼，裡面的字才不會跑掉。

# GET
# 上圖(Http Verb)中的Request URL
url = "https://course.nuk.edu.tw/QueryCourse/QueryCourse.asp" 
re = requests.get(url) 
re.encoding='big5'
# re.encoding='cp950'
# re.encoding='utf8'
# print(re.text)

# POST 找到POST網址 並依照data格式輸入資料
url = "https://course.nuk.edu.tw/QueryCourse/QueryResult.asp" 
data ={
"flag":"1",
"OpenYear":"107".encode('big5'),  #用big5編碼後傳輸
"Helf":"1",
"Pclass":"M",
"Sclass":"CS",
}

re = requests.post(url,data=data)
re.encoding='big5'

file.write(re.text)
file.close()  # 寫完要關掉檔案，才會成功存檔。

## Read File 如果你已經把上面程式碼成功執行，則可以往下試著把它讀出來
path = "htmlTest.txt"  
file = open(path, 'r', encoding='utf8')

# 三種讀取方式，每次打開檔案請擇一使用，若重複使用會出現問題。
# 一、一次全部讀出來
context = file.read()
print(context)


# re.encoding='cp950'
# re.encoding='utf8'
# print(re.text)
