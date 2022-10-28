# x86-manual

yet another `Intel(r) 64 and IA-32 Architectures Software Developer’s Manual` scrap

## make dependencies

- `go-md2man`
- `gzip`
- `pandoc`
- `wget`

## usage

```bash
# clone Félix Cloutier's site
make scrap

# convert into man
make populate

# install
make install
```
