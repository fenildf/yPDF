# yaoxinPDF

TODO:   
- [ ] Test on Mac OS
http://pynput.readthedocs.io/en/latest/limitations.html#mac-osx
- [ ] Test on Windows XP sp3
- [ ] Test on Windows 7 sp1
- [ ] Test on Windows 8.1
- [ ] Test on Windows 10

### 复制英文PDF文件中的文字时，自动将回车变为空格的 Python 程序。
### A Python application which replaces line feeds into spaces while coping in English literature.

## 用法：
## Usage:

### 安装
### Installation

```
sudo pip3 install pyperclip
git clone https://github.com/gaoyaoxin/yaoxinPDF.git
```

### 使用
### Run

#### 注意！请在运行程序前仔细阅读以免损失您的个人数据！程序会自动创建名为 yaoxinPDF.txt 的文件，如果程序所在目录存在该名字的私人文件，请做好数据备份。请勿在该文件中储存重要数据，因为它会暂存和替换剪切板内容用于程序良好运行。
#### Attention! Please read carefully before running this application in case of lost of your private data! A file named yaoxinPDF.txt will be automatically created by the application. If there already exists a file with the same name, please make sure to make a backup of your private file. Please do not save any precious data in the file because it will only temporarily save and replace data in clipboards.


```
python<version> yaoxinPDF.py
```

程序会在后台自动运行，期间按Ctrl+C键或Ctrl+c键复制的文本会自动格式化并储存在剪切板中，粘贴到文本编辑器时直接可用。  
The application runs automatically at background. During this time, those copied via Ctrl+C or Ctrl+c will be automatically formatted and saved to clipboard for use later in text editors.




### 退出
### Exit

在终端中按Esc键  
Press Esc in the Terminal


## 已知问题：
## Known Bugs:
1.复制多段文字时无法分段。  
Cannot divide paragraphs while coping mulitiple paragraphs.  
2.某些情况下格式化不完全，现用reload()和执行两遍函数暂行解决。  
Sometimes formatting is not thorough, using reload() and double funtion use to temporarily solve.
3.无法粘贴斜体等格式。
Cannot copy format such as *italic*.

### 在 深度 15.5 & 福昕PDF阅读器上测试通过。
### Tested and works at Deepin 15.5 & Foxit Reader.

## 历史
## History
|Time|说明|Note|
|---|---|---|
|Sat, 02 Dec 2017 18:30:30 GMT+8<br>Sat, 02 Dec 2017 10:30:30 GMT|新增 time.sleep(0.1) 延时执行|Added time.sleep(0.1) for delay execution|  
|Sat, 02 Dec 2017 17:44:08 GMT+8<br>Sat, 02 Dec 2017 09:44:08 GMT|初始版本|Initial commit|
