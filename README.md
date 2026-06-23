# DBReader
豆瓣帖子留存

本工具展示效果： https://harlorpavelski-rgb.github.io/DBReader/

本仓可作展示位想要发声的媎妹可以把自己的网页用issu提给我或把想法的内容整理成 txt\docx\md文件放在issu提给我，我代发在老地址

2026\6\23 新增txt\docx\md文件读取阅读功能，txt\docx文件放在根目录则分类在'其他'，放在标签文件夹下，则分类在该标签中
 md文件以这个结构放置则在post标签下
📦 project-root
├── 📄 index.html
├── 📂 posts
│   ├── 📄 article.md
│   └── 📂 images
│       └── 📷 photo.png
图片文件路径请写
![描述文字](images/photo.png)

![描述文字](./images/photo.png)

本工具需要下载python与pycharm


需要使用本阅读器的媎妹先fork莴苣媎妹的帖子爬取工具的仓 https://github.com/Hua27-Hua/douban-group-archive-tool 并拉取代码到本地


fork本仓后把代码拉到本地仓中，将本仓export_single_html.py文件里的内容全选复制后 将 帖子爬取工具内的 同名文件export_single_html.py 里的内容全部替换（能记得文件层级的媎妹也可以直接替换文件）后在使用帖子爬取工具


按照莴苣媎妹的教程得到帖子html文件后将_single_html_exports文件内的帖子文件复制进本阅读器文件夹的根目录，文件结构从外到内为： 标签名文件夹 - 帖子名文件夹 - 帖子具体html页，无标签的帖子也可以直接把帖子文件夹放在根目录帖子会自动整理在“其他”标签。同标签的帖子放在同一标签文件夹下。(具体参考示例文件夹(可删))


放好文件后运行generate_menu.py文件获得层级目录 


点开index.html文件运行 多刷新几次后查看效果


确认效果无误后把博文帖子文件(包括标签文件夹,检查'未进行版本管理的文件'中有无遗漏)、menuData.js一起提交并push进自己的仓，在GitHub代码页的Setting中的pages中托管即可成为网页版。不想开放网页的话,也可本地使用pycharm运行index.html查看

任何问题先直接截图或口述给ai

