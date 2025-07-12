​	这是一个自动化处理PDF文件的`python`脚本。脚本的目标是利用`kimi API`从PDF文件中提取特定信息，最终以Excel的形式呈现出来。

### Introduction

* **What you should do before you run:**

  *  `trimm`文件里放置的是待处理的PDF格式的文献	

  * `paper/1.prompt`里放置的是不同的提问词

  * `kimiapi.txt`中放置API密钥

  *  `create_file_list.py`用于产生文献列表，运行后得到的文献列表在`info`中。

* **Now,you can run`kimi.ipynb`!**

* 脚本会从本地文件`kimiapi.txt`中读取API密钥，并且初始化与`Moonshot API`的连接。

* 接着脚本读取`prompt`和待处理文献列表。

* 然后脚本开始检查输出文件夹`output`，依次读取和处理文献。

*  脚本在执行过程中，会将`API`相应的元数据（如完成原因，令牌使用量）记录到`record.txt`并打印 

* 最终的结果，会被存放在`output`文件夹中，以`Excel`的形式展现出来。

###  