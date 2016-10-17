import os

def get_layout(name):
    header = ""
    with open(os.path.join("layout", name + ".html"), 'r') as f:
        for line in f:
            header += line
    return header

def get_content(name):
    content = ""
    with open(os.path.join("content", name + ".html"), 'r') as f:
        for line in f:
            content += line
    return content

def write_page(name, header, menu, content_string, footer):
    if name != 'index':
        file_name = os.path.join(name + ".html")
    else:
        file_name = name + ".html"
    with open(file_name, 'w') as f:
        f.write(header)
        f.write(menu)
        f.write(content_string)
        f.write(footer)

if __name__ == "__main__":
    header = get_layout("header")
    menu = get_layout("menu")
    footer = get_layout("footer")
    content_names = ['index', 'contact', 'research', 'publications', 'reading_group']
    for name in content_names:
        content_string = get_content(name)
        write_page(name, header, menu, content_string, footer)