#!/usr/local/bin/python3

import argparse

def read_file_content(fdir):
    f = open(fdir, "r")
    content = f.read()
    f.close()
    return content

def write_file_content(content, dst):
    f = open(dst, "w")
    f.write(content)
    f.close()

def build_output_from_files(dst, *srcs):
    content = ""
    for src in srcs:
        content += read_file_content(src) + "\n\n"
    write_file_content(content, dst)

build_output_from_files("./out.md", "./sample-files/file1.md", "./sample-files/file2.md")




