from importlib.metadata import version, PackageNotFoundError

try:
    VERSION = version('mman-tool')
except PackageNotFoundError:
    VERSION = "0.0.0-dev"

TARGET_FILES_PATTERN = '.targets'
COMMENT_PREFIX = '#'
