from pathlib import Path
import logging
from collections.abc import Collection
from .utils.copy2 import copy_file
from .meta import *


logger = logging.getLogger(__name__)

## If I want to move the source codes on my dev computer into the target machine, which steps should I take?

#### First, I need to make clear what files to 'copy' and what the structure is like to match. 其实不需要去match pattern, 只需要指定root,
#### 在这里其实就是work_dir.

#### ps: 我这里都是精确匹配.

#### Second, Copy them into a temporary space.

#### Third, match the target path on target machine, and then we copy them.

## I need a protocol, which we name it `Mmana, in which the target objects are recored in and the parser will 
## read it. 


def gen_the_needed_files_list(target_file_path=TARGET_FILES_PATTERN ,*, 
                              work_dir:Path|None=None,
                              verbose:bool=False)->list[str]:
    """
    generate the file paths that exists.
    生成存在的目标文件的路径. 
    """
    if work_dir is None:
        work_dir = Path.cwd() 
    
    abs_target_path = work_dir / target_file_path

    if not abs_target_path.exists():
        logger.error(f"'{abs_target_path}'not found.")
        return []

    file_paths = []
    for path in abs_target_path.read_text().splitlines():
        if not path or path.rstrip().startswith(COMMENT_PREFIX): 
            continue
        if not (abs_path:=(work_dir / path)).exists():
            if verbose:
                logger.warning(f"file '{abs_path}' doesn't exist.")
            continue
        # if not (abs_path:=(work_dir / path)).exists() and verbose:
        #     logger.warning(f"file '{abs_path} doesn't exist.")
        #     continue 
        # 此处的逻辑有问题, 只有当verbose=True的时候, 才会跳过.
        file_paths.append(path)
    return file_paths



def bench_copy(relative_file_paths: Collection[str], 
               target_root: Path, *, 
               source_dir:Path|None=None, 
               verbose:bool=False):
    """
    bench copy the files into target root, keeping the relative path
    批复制文件到目标目录下面
    relative_file_paths: the relative path collection, of which the root is source_dir.
    """
    if source_dir is None:
        source_dir = Path.cwd()
    if not Path(target_root).exists():
        logger.error(f"'{target_root}' not found.")
        return 

    total = len(relative_file_paths)
    for i, path in enumerate(relative_file_paths):
        parent = Path(path).parent
        source_path = source_dir / path
        target_path = target_root / parent
        target_path.mkdir(exist_ok=True, parents=True)
        copy_file(Path(source_path), target_path, verbose=verbose, prefix=f'[{i+1}/{total}] ')



