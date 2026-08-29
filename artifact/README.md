# ReadThrough artifact archive

The artifact archive is split into numbered parts to satisfy the hosting
service's per-file upload limit. Download all files named
`ReadThrough_alg.zip.part001` through `ReadThrough_alg.zip.part011` into the
same directory, then run:

```bash
python join_parts.py
```

This reconstructs `ReadThrough_alg.zip` and verifies its SHA-256 checksum.
The expected checksum is:

```text
DFC5F310D90CEC4E16B7A52CAEFE247C34A6EFB56DAC83A66D60BF856D789EE2
```
