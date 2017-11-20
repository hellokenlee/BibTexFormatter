# -*- coding:utf-8 -*-
import sys
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

# 需要保留的bibTex项
default_settings = {'ID', "ENTRYTYPE", "author", "title", "year", "journal", "number", "volume", "pages"}

# 格式化函数
def format(origin_file_path, edited_file_path, settings):
	# 读取
	with open(origin_file_path) as bib_file:
		bib_str = bib_file.read()
	bib_database = bibtexparser.loads(bib_str)
	# 处理后的数据库文件
	edited_bib_database = BibDatabase()
	# 逐篇文章处理
	for entry in bib_database.entries:
		edited_bib_database.entries.append({})
		# 逐个条目检查
		for key in entry:
			if key in settings:
				edited_bib_database.entries[-1][key] = entry[key]
	# 写入
	writer = BibTexWriter()
	with open(edited_file_path, 'w') as bib_file:
		bib_file.write(writer.write(edited_bib_database))
	pass

# 简单参数处理
def main():
	if len(sys.argv) == 2:
		format(sys.argv[1], sys.argv[1], default_settings)
	elif len(sys.argv) == 3:
		format(sys.argv[1], sys.argv[2], default_settings)
	elif len(sys.argv) > 2 and sys.argv[2] == '-s':
		settings = {'ID', "ENTRYTYPE"}
		for i in range(3, len(sys.argv)):
			settings.add(sys.argv[i])
		format(sys.argv[1], sys.argv[1], settings)
	elif len(sys.argv) > 3 and sys.argv[3] == '-s':
		settings = {'ID', "ENTRYTYPE"}
		for i in range(4, len(sys.argv)):
			settings.add(sys.argv[i])
		format(sys.argv[1], sys.argv[2], settings)
	else:
		print("Usage:\n  python BibTexFormatter.py source_bib [target_bib] [-s bibKey1 bibKey2 ...]")
		print("[-s(default)]:\n  author journal number pages title volume year\n")
	pass

if __name__ == '__main__':
	main()

