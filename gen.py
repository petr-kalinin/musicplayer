#!/usr/bin/python3
import os
import os.path
import jinja2
import shutil
    
with open("template.html") as f:
    text = ''.join(f.readlines())

template = jinja2.Template(text)


os.chdir("music")

shutil.copy("../jquery-3.1.0.slim.min.js", ".")  
shutil.copy("../main.css", ".")
shutil.copy("../main.js", ".")

for directory, subdirs, files in os.walk("."):
    files = filter(lambda f: os.path.splitext(f)[1] == ".mp3", files)
    files = sorted(files)
    subdirs = sorted(subdirs)
    backlink = os.path.relpath(".", directory)
    title = os.path.split(directory)[1]
    rendered = template.render(subdirs=subdirs, files=files, backlink=backlink, title=title)
    with open(os.path.join(directory, "index.html"), 'w') as f:
        f.write(rendered)
    