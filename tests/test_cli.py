# tests/test_cli.py

from mman_tool.cli import main
from mman_tool import core


def test_cli_end_to_end(tmp_path):
    src = tmp_path / "src"
    dst = tmp_path / "dst"
    src.mkdir()
    dst.mkdir()

    (src / ".targets").write_text("apple\nmissing\nsub/nuts\n")
    (src / "apple").write_text("a")
    (src / "sub").mkdir()
    (src / "sub" / "nuts").write_text("n")

    main([
        "--source-root", str(src),
        "--target-root", str(dst),
        "-v",
        ])

    assert (dst / "apple").exists()
    assert (dst / "sub" / "nuts").exists()
