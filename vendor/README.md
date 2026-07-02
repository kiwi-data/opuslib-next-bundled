Populate `vendor/opus` with the upstream `xiph/opus` source tree before building.

Recommended approach:

1. Add `https://github.com/xiph/opus` as a git submodule at `vendor/opus`.
2. Pin to a released tag.
3. Keep the upstream `COPYING` file in the vendored tree.

The build intentionally fails if `vendor/opus` is missing so wheels never
accidentally fall back to a system `libopus`.
