# Shared KiCad Libraries

Custom symbols, footprints, and 3D models used by BOTH boards, kept in
one place so they don't drift apart between projects:

- `symbols/` — .kicad_sym libraries
- `footprints.pretty/` — .kicad_mod footprint libraries
- `3dmodels/` — .step / .wrl 3D models for footprints

Point both KiCad projects at this folder via project-relative library
tables (Preferences > Manage Symbol/Footprint Libraries, use the
`${KIPRJMOD}/../shared-libraries/...` path) so libraries stay portable
when the whole `orbita/` folder is copied or cloned elsewhere.
