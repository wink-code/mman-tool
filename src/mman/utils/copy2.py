import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

def copy_file(source_path:Path, 
              target_dir:str|Path, *,
              verbose:bool=False,
              prefix:str=''):

    """
    put a **file** object into the object directory
    将**文件**对象复制到目标目录下

    source_path: Path, 绝对路径
    """
    dst_file = Path(target_dir) / source_path.name
    try:
        shutil.copy2(source_path, target_dir)
    except PermissionError as e:
        logger.warning(
        "%sCould not preserve metadata for %s "
        "(likely unsupported filesystem): %s. "
        "Falling back to shutil.copyfile.",
        prefix, source_path, e
                )
        shutil.copyfile(source_path, dst_file)
    if verbose:
        logger.info("%sSuccessfully copy '%s' into '%s'", prefix, source_path, target_dir)

