from pathlib import Path
import sys
from .core import gen_the_needed_files_list, bench_copy, VERSION, TARGET_FILES_PATTERN
from argparse import ArgumentParser
from myfind.core import MATCHED_FILE_NAME, find_matched_file_paths


def run(source_root: Path,
        target_root: Path,
        *, 
        force: bool,
        verbose: bool
     ) -> None:

    targets_file = source_root / TARGET_FILES_PATTERN
    if force or not targets_file.exists():
        # gen the `.targets` file fisrt
        pattern_file = source_root / MATCHED_FILE_NAME
        if not pattern_file.exists():
            raise FileNotFoundError(pattern_file)

        with open(pattern_file, encoding='utf-8') as f:
            patterns = f.read().splitlines()

        patterns = [pattern.strip() for pattern in patterns if pattern.strip()]

        lines = find_matched_file_paths(
                patterns, 
                work_dir=source_root
                )

        with open(targets_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines)+'\n')

    files = gen_the_needed_files_list(
            work_dir=source_root,
            verbose=verbose
            )

    bench_copy(files, target_root, source_dir=source_root, verbose=verbose)




def main(argv: list[str]|None=None)->int:
    parser = ArgumentParser("mman_tool", 
                            description=f"Default pattern file: {MATCHED_FILE_NAME!r}, "
                            f"output file is: {TARGET_FILES_PATTERN!r}",
                            )
    parser.add_argument('-V', '--version', action='version', version=VERSION)
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--source-root', type=Path, default=Path('.'))
    parser.add_argument('--target-root', type=Path, required=True)
    parser.add_argument('--force', action='store_true')

    args = parser.parse_args(argv)


    try:
        run(source_root=args.source_root,
            target_root=args.target_root,
            force=args.force,
            verbose=args.verbose
            )
    except FileNotFoundError as e:
        print(f"error: file not found: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
