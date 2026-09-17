from myfind.core import MATCHED_FILE_NAME, find_matched_file_paths

from mman.cli import run


def test_force(tmp_path):
    (tmp_path / "src").mkdir(exist_ok=True)
    (tmp_path / "dst").mkdir(exist_ok=True)

    (tmp_path / "src" / "apple").mkdir(exist_ok=True)
    (tmp_path / "src" / "banana").mkdir(exist_ok=True)
    (tmp_path / "src" / "orange").mkdir(exist_ok=True)

    (tmp_path / "src" / "apple" / "file1").write_text("file1")
    (tmp_path / "src" / "apple" / "file2").write_text("file2")
    (tmp_path / "src" / "apple" / "file3").write_text("file3")

    (tmp_path / "src" / "banana" / "file1.py").write_text("print('hello world')")
    (tmp_path / "src" / "banana" / "file1.pyc").write_text("\x1389413")

    (tmp_path / "src" / "orange" / "file1.css").write_text("css content")
    (tmp_path / "src" / "orange" / "file2.html").write_text("<html></html>")
    (tmp_path / "src" / "orange" / "file3.js").write_text("function() {};")

    (tmp_path / "src" / MATCHED_FILE_NAME).write_text(
        "apple/*\nbanana/*.py\norange/*.css\norange/*.html\norange/*.js"
    )

    run(
        source_root=tmp_path / "src",
        target_root=tmp_path / "dst",
        force=True,
        verbose=True,
    )

    # print(list((tmp_path / "dst" / "apple").iterdir()))
    # print(list((tmp_path / "dst" / "banana").iterdir()))
    # print(list((tmp_path / "dst" / "orange").iterdir()))

    assert set(p.name for p in (tmp_path / "dst" / "apple").iterdir()) == {
        f"file{i}" for i in range(1, 4)
    }
    assert set(p.name for p in (tmp_path / "dst" / "banana").iterdir()) == {"file1.py"}
    assert set(p.name for p in (tmp_path / "dst" / "orange").iterdir()) == {
        "file1.css",
        "file2.html",
        "file3.js",
    }

    assert (tmp_path / "src" / MATCHED_FILE_NAME).exists()


def test_debug(tmp_path):
    # ...同样的造数...
    (tmp_path / "src").mkdir(exist_ok=True)
    (tmp_path / "dst").mkdir(exist_ok=True)

    (tmp_path / "src" / "apple").mkdir(exist_ok=True)
    (tmp_path / "src" / "banana").mkdir(exist_ok=True)
    (tmp_path / "src" / "orange").mkdir(exist_ok=True)

    (tmp_path / "src" / "apple" / "file1").write_text("file1")
    (tmp_path / "src" / "apple" / "file2").write_text("file2")
    (tmp_path / "src" / "apple" / "file3").write_text("file3")

    (tmp_path / "src" / "banana" / "file1.py").write_text("print('hello world')")
    (tmp_path / "src" / "banana" / "file1.pyc").write_text("\x1389413")

    (tmp_path / "src" / "orange" / "file1.css").write_text("css content")
    (tmp_path / "src" / "orange" / "file2.html").write_text("<html></html>")
    (tmp_path / "src" / "orange" / "file3.js").write_text("function() {};")

    (tmp_path / "src" / MATCHED_FILE_NAME).write_text(
        "apple/*\nbanana/*.py\norange/*.css\norange/*.html\norange/*.js"
    )

    result = find_matched_file_paths(
        (tmp_path / "src" / MATCHED_FILE_NAME).read_text().splitlines(),
        work_dir=tmp_path / "src",
    )
    # print(result)
    assert set(result) == {
        "apple/file1",
        "apple/file2",
        "apple/file3",
        "banana/file1.py",
        "orange/file1.css",
        "orange/file2.html",
        "orange/file3.js",
    }
