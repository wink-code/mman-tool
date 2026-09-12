# Migrate Man

A small CLI tool that copies a selected set of files from a source root into
a target root, preserving their relative paths.

It reads a `.targets` file that lists, one per line, the relative paths of
the files you want to copy. Think of it as a minimal, host-side version
of Dockerfile's `COPY` instruction.

## Install
```shell
uv tool install mann-tool
```

Or from a local build:
```shell
uv build
uv tool install --force dist/*.whl
```
## Usage

```shell
mm copy --source-root=./src --target-root=./dist
```

- `--source-root`: the directory that `.targets` and the listed files are relative to.
Defaults to the current directory.
- `--target-root`: the directory to copy into. Required.

## The `.target` file
A plain text file, one relative path per line. Empty lines are ignored.
Lines starting with `#` are treated as comments.

```text
# front-end assets
index.html
assets/index.js
assets/index.css

# nested paths are supported
sub_folder/nuts
```

Paths are relative to `--source-root`. Files that do not exist are skipped, with 
a warning if `-v` is set.

## Example


Given:
```
projects/
|____ .targets
|____ index.html
|____ assets/
        |____ index.js
```
with `.targets`:
```
index.html
assets/index.js
```

Then:
```shell
mkdir ./out/
mm copy --source-root=./projects --target-root=./out
```
products:
```
out/
|____ index.html
|____ assets/
        |_____ index.js
```

## Status
Early statge. Currently only supports local file copying; no glob patterns,
no remote targets, no parallel copy.

## Roadmap
- Auto-generate `.targets` from include/exclude patterns.
- `-vv` / `-vvv` for progressively more verbose logging.
- Windows path support.

## License

MIT. See [LISENCE](LISENCE).
