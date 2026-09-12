from pathlib import Path

import pytest

from migrate_program import core


@pytest.fixture
def src_root(tmp_path:Path) -> Path:
    root = tmp_path / "src"
    root.mkdir()
    (root / ".targets").write_text(
            "apple\n"
            "\n"
            "missing\n"
            "sub_folder/nuts\n"
            )
    (root / "apple").write_text("a")
    (root / "sub_folder").mkdir()
    (root / "sub_folder" / "nuts").write_text("n")
    return root


def test_gen_list_skip_missing(src_root: Path):
    result = core.gen_the_needed_files_list(work_dir=src_root, verbose=False)
    assert result == ["apple", "sub_folder/nuts"]

def test_gen_list_verbose_warns(src_root: Path, caplog):
    with caplog.at_level("WARNING"):
        core.gen_the_needed_files_list(work_dir=src_root, verbose=True)
    assert any("missing" in r.message for r in caplog.record)

def test_bench_copy_creates_dirs(src_root: Path, tmp_path: Path):
    dst = tmp_path / "src"
    dst.mkdir()
    files = core.gen_the_needed_files_list(work_dir=src_root)
    core.bench_copy(files, dst, source_dir=src_root)

    assert (dst / "apple").read_text() == "a"
    assert (dst / "sub_folder" / "nuts").read_text() == "n"
    assert not (dst / "midding").exists()


