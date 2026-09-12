from pathlib import Path
# from sys import path

# print(path)
# from mman import main
import mman.core as main

# print(dir(migrate_program))
# migrate_program.src.main.gen_the_needed_files_list()

def test_1():
    objs = main.gen_the_needed_files_list(
            work_dir=Path('./tests/test_objs/'),
            verbose=True
            )
    print(objs)

def test_2():
    objs = main.gen_the_needed_files_list()
    print(objs)


if __name__ == '__main__':
    test_1()
    # $ uv run tests/test_print_lines.py                                                 10:14:10
    # file 'tests/test_objs/banana doesn't exist.
    # ['apple', 'orange', 'sub_folder/nuts']


