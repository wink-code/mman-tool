from pathlib import Path
from .core import gen_the_needed_files_list, bench_copy, VERSION
from argparse import ArgumentParser


def main(argv: list[str]|None=None)->None:
    parser = ArgumentParser("mman_tool")
    parser.add_argument('-V', '--version', action='version', version=VERSION)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--source-root', type=str, default='.')
    parser.add_argument('--target-root', type=str, required=True)

    args = parser.parse_args(argv)
    verbose = args.verbose
    files = gen_the_needed_files_list(
            work_dir=Path(args.source_root), 
            verbose=verbose
            )
    # print(files)
    
    # print(files[0])
    bench_copy(files, args.target_root, 
               source_dir=Path(args.source_root), 
               verbose=verbose)


if __name__ == '__main__':
    main()
