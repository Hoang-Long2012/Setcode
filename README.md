# Setcode

A tiny command-line utility that exits with the specified exit code.

## Installation

### From release

Download latest version from [Release page](https://github.com/Hoang-Long2012/setcode/releases/latest) and extract.

### From source

- Clone this repository:

```
git clone https://github.com/Hoang-Long2012/setcode.git
```

- Run:

```
cd setcode/src
python setcode.py <CODE>
```

### Build executable

- Install PyInstaller:

```
pip install pyinstaller
```

- Build:

```
pyinstaller --onefile setcode.py
```

## Usage

```
setcode [-h] [-v] code
```

### Arguments

| Argument | Description       |
| -------- | ----------------- |
| `code`   | Exit code to use. |

### Options

| Option            | Description                        |
| ----------------- | ---------------------------------- |
| `-h`, `--help`    | Show the help message and exit.    |
| `-v`, `--version` | Show the program version and exit. |

## Examples

Exit successfully:

```
setcode 0
```

Exit with code `1`:

```
setcode 1
```

Exit with code `42`:

```
setcode 42
```

## Why?

Sometimes you just need a command that does one thing:

```
Exit with this code.
```

That's it.

## License

This project is licensed under the MIT License.  
See [LICENSE](LICENSE) for license information.

Copyright (c) 2026 Hoàng Long
