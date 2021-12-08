import sys

src_file_name = sys.argv[1]
dst_file_name = sys.argv[2]

with open(src_file_name, "r") as src_file:
    content = src_file.read().replace("\t", " " * 4)
    with open(dst_file_name, "w") as dst_file:
        dst_file.write(content)
