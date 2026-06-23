import os
import json
import re


def get_html_title(file_path, default_title):
    """读取 HTML 文件提取 <title>，提取不到则用文件名"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if title_match:
                return title_match.group(1).strip()
    except Exception:
        pass
    return default_title


def is_valid_file(file_name):
    """检查文件是否属于系统所支持的阅读格式"""
    name_lower = file_name.lower()
    # 排除掉主页 index.html 自身
    if name_lower == "index.html":
        return False
    valid_extensions = ['.html', '.htm', '.txt', '.md', '.docx']
    return any(name_lower.endswith(ext) for ext in valid_extensions)


def get_distinct_post_title(file_name, base_title):
    """
    根据文件后缀，为非 HTML 文件生成带格式区分的独立标题，
    防止同名的 .md / .docx / .txt 发生覆盖。
    """
    ext = os.path.splitext(file_name)[1].lower()
    if ext in ['.html', '.htm']:
        return base_title
    elif ext == '.md':
        return f"{base_title} (Markdown)"
    elif ext == '.docx':
        return f"{base_title} (Word)"
    elif ext == '.txt':
        return f"{base_title} (Txt)"
    return f"{base_title} ({ext[1:].upper()})"


def generate_menu():
    current_dir = os.getcwd()

    # 临时存放分类数据的字典 { 分类名: { 帖子名: [页面列表] } }
    structure = {}

    # ========================================================
    # 第一步：直接扫描 py 程序所在【真·根目录】下的散落文件 -> 归类到“其他”
    # ========================================================
    root_items = os.listdir(current_dir)
    root_files = [f for f in root_items if os.path.isfile(os.path.join(current_dir, f)) and is_valid_file(f)]

    if root_files:
        category = "其他"
        if category not in structure:
            structure[category] = {}

        for file in root_files:
            file_path = os.path.join(current_dir, file)
            base_name = os.path.splitext(file)[0]

            if file.lower().endswith('.html') or file.lower().endswith('.htm'):
                page_title = get_html_title(file_path, base_name)
            else:
                page_title = base_name

            post_title = get_distinct_post_title(file, page_title)

            if post_title not in structure[category]:
                structure[category][post_title] = []

            structure[category][post_title].append({
                "title": page_title,
                "path": f"./{file}"
            })

    # ========================================================
    # 第二步：循环遍历子文件夹
    # ========================================================
    for level1_item in root_items:
        level1_path = os.path.join(current_dir, level1_item)

        # 只处理文件夹
        if not os.path.isdir(level1_path):
            continue

        sub_items = os.listdir(level1_path)
        has_valid_files_directly = any(is_valid_file(f) for f in sub_items)
        has_sub_dirs = any(os.path.isdir(os.path.join(level1_path, s)) for s in sub_items)

        # ─── 情况 A：只有一层文件夹（【核心修改点】直接使用该文件夹名字作为标签分类） ───
        if has_valid_files_directly:
            category = level1_item  # 使用当前文件夹的名字作为分类标签！

            if category not in structure:
                structure[category] = {}

            for file in sub_items:
                if not is_valid_file(file):
                    continue
                file_path = os.path.join(level1_path, file)
                base_name = os.path.splitext(file)[0]

                if file.lower().endswith('.html') or file.lower().endswith('.htm'):
                    page_title = get_html_title(file_path, base_name)
                else:
                    page_title = base_name

                post_title = get_distinct_post_title(file, page_title)

                if post_title not in structure[category]:
                    structure[category][post_title] = []

                structure[category][post_title].append({
                    "title": page_title,
                    "path": f"./{level1_item}/{file}"
                })

        # ─── 情况 B：有两层文件夹（两层深度的传统帖子分类归类） ───
        elif has_sub_dirs:
            category = level1_item  # 第一层文件夹名作为分类名

            if category not in structure:
                structure[category] = {}

            for level2_item in sub_items:
                level2_path = os.path.join(level1_path, level2_item)
                if not os.path.isdir(level2_path):
                    continue

                for file in os.listdir(level2_path):
                    if not is_valid_file(file):
                        continue
                    file_path = os.path.join(level2_path, file)
                    base_name = os.path.splitext(file)[0]

                    if file.lower().endswith('.html') or file.lower().endswith('.htm'):
                        page_title = get_html_title(file_path, base_name)
                    else:
                        page_title = base_name

                    post_title = get_distinct_post_title(file, level2_item)

                    if post_title not in structure[category]:
                        structure[category][post_title] = []

                    structure[category][post_title].append({
                        "title": page_title,
                        "path": f"./{level1_item}/{level2_item}/{file}"
                    })

    # ────────────────────────────────────────────────────────
    # 第三步：格式化并进行排序（确保“其他”永远在最后面）
    # ────────────────────────────────────────────────────────
    menu_data = []

    sorted_categories = sorted([c for c in structure.keys() if c != "雪花" and c != "其他"])
    # 也可以根据您的喜好排序，这里使用标准排序。如果存在“其他”，放到最后
    if "其他" in structure:
        sorted_categories.append("其他")

    for cat_name in sorted_categories:
        posts_map = structure[cat_name]
        posts_list = []

        for p_title, pages in posts_map.items():
            if not pages:
                continue
            pages.sort(key=lambda x: x['title'])

            posts_list.append({
                "title": p_title,
                "total_pages": len(pages),
                "pages": pages
            })

        if posts_list:
            posts_list.sort(key=lambda x: x['title'])
            menu_data.append({
                "category": cat_name,
                "posts": posts_list
            })

    # 写入 menuData.js
    js_content = f"var thispost = {json.dumps(menu_data, ensure_ascii=False, indent=4)};"
    with open("menuData.js", "w", encoding="utf-8") as js_file:
        js_file.write(js_content)

    print("☀️ 智能分类目录树重新编译完成！")


if __name__ == "__main__":
    generate_menu()