# opuslib-next-bundled

Python bindings to `libopus`, with the compiled shared library bundled inside
platform wheels.

## Goals

- Support Python 3.9 and newer
- Preserve the `opuslib-next` Python API as much as practical
- Publish wheels that do not depend on a system-installed `libopus`
- Keep source builds reproducible by vendoring `xiph/opus`

## Installation

```bash
pip install opuslib-next-bundled
```

Wheels are intended to contain `libopus` directly. Source builds require a
populated `vendor/opus` tree.

## Usage

```python
import opuslib_next
```

By default the package loads the bundled shared library from
`opuslib_next/_native`. To force use of a system library for debugging:

```bash
OPUSLIB_NEXT_USE_SYSTEM_LIB=1 python -c "import opuslib_next"
```

## Development

```bash
python -m pip install -U build
python -m build
pytest
```

The CMake build fails fast if `vendor/opus` is missing. Populate it before
building wheels.

## Upstream Attribution

This project is derived in part from:

- [`kalicyh/opuslib-next`](https://github.com/kalicyh/opuslib-next), whose
  Python binding layer provided the compatibility base
- [`xiph/opus`](https://github.com/xiph/opus), whose codec implementation is
  bundled into built wheels

See `NOTICE` and `LICENSES/` for the preserved third-party notices.

## Repository

Source repository: <https://github.com/kiwi-data/opuslib-next-bundled>
