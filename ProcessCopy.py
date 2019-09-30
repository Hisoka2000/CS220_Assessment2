import os
import shutil
from concurrent.futures import ProcessPoolExecutor
from time import sleep

def copyFiles(src, dest):
	src_files = os.listdir(src)
	for file_name in src_files:
		full_file_name = os.path.join(src, file_name)
		if os.path.isfile(full_file_name):
			shutil.copy(full_file_name, dest)

def main():
	print("Please input the folder to copy files from")
	src = input()
	print("Please input the folder to paste the files into")
	dest = input()
	executor = ProcessPoolExecutor(5)
	future = executor.submit(copyFiles, (src), (dest))

if __name__ == '__main__':
	main()
