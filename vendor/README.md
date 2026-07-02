`vendor/opus` is tracked as a git submodule pointing at upstream
`https://github.com/xiph/opus`.

After cloning this repository, run:

```bash
git submodule update --init --recursive
```

The submodule should stay pinned to a released upstream tag.

The build intentionally fails if `vendor/opus` is missing so wheels never
accidentally fall back to a system `libopus`.
