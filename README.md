# DBReader
豆瓣帖子留存



本工具需要下载python与pycharm


需要使用本阅读器的媎妹先fork莴苣媎妹的帖子爬取工具的仓 forkhttps://github.com/Hua27-Hua/douban-group-archive-tool并拉取代码到本地


fork本仓后把代码拉到本地仓中，将export_single_html.py文件里的内容全选后 将 帖子爬取工具内的 同名文件export_single_html.py 里的内容全部替换（能记得文件层级的媎妹也可以直接替换文件）


按照莴苣媎妹的教程得到帖子html文件后将文件复制进本阅读器文件夹的根目录，文件排列从外到内为： 标签名文件夹 - 帖子名文件夹 - 帖子具体html页，无标签的帖子也可以直接把帖子文件夹放在根目录帖子会自动整理在“其他”标签


放好文件后运行generate_menu.py文件获得层级目录 


点开index.html文件运行 多刷新几次后查看效果


最后把放置的帖子文件、menuData.js一起push进自己的仓在Setting中的pages中托管
