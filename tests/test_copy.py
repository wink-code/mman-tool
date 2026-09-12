from mman.utils.copy2 import copy_file
from pathlib import Path


source_path = Path('./test_objs/sub_folder/nuts')
source_path_1 = Path('./test_objs/sub_folder')
target_1 = './test_objs/sub_folder/copy_space'
target_2 = Path(target_1)


def test_1():
    copy_file(source_path, target_1)

def test_2():
    copy_file(source_path, target_2)


def test_3():
    copy_file(source_path_1, target_1)

if __name__ == '__main__':
    test_3()
