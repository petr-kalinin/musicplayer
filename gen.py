#!/usr/bin/python3
import os
import os.path
import jinja2
import shutil
    
backlink_prefix = "../"
files_prefix = "/home/petr/15_16/16_sis/music/music"
output_directory = "output"


with open("template.html") as f:
    text = ''.join(f.readlines())

template = jinja2.Template(text)


os.chdir("music")
output_directory = os.path.join("..", output_directory)

shutil.copy("../jquery-3.1.0.slim.min.js", output_directory)  
shutil.copy("../main.css", output_directory)
shutil.copy("../main.js", output_directory)

for directory, subdirs, files in os.walk("."):
    os.makedirs(os.path.join(output_directory, directory), exist_ok=True)
    files = filter(lambda f: os.path.splitext(f)[1] == ".mp3", files)
    files = sorted(files)
    this_files_prefix = ""
    if files_prefix:
        this_files_prefix = os.path.join(files_prefix, directory)
    files = [(f, os.path.join(this_files_prefix, f)) for f in files]
    subdirs = sorted(subdirs)
    backlink = os.path.join(backlink_prefix, os.path.relpath(".", directory))
    title = os.path.split(directory)[1]
    rendered = template.render(subdirs=subdirs, files=files, backlink=backlink, title=title)
    with open(os.path.join(output_directory, directory, "index.html"), 'w') as f:
        f.write(rendered)
    