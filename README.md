# Orbita — Satellite Construction Competition Project

Project workspace for the **International Space Tournament "Orbita"**
Satellite Construction Competition (IntroSat CubeSat 3U kit,
stratospheric balloon flight). Set up 10 September 2026.

Start here: **`docs/research/orbita-research-and-playbook.md`** —
covers what the tournament is, how past seasons ran, the 2026 technical
requirements, a ground-station explainer, KiCad workflow notes for this
project, and a task list broken out by team role.

## Folder map

| Folder | What lives here |
|---|---|
| `docs/` | Official requirements, datasheets, research notes, meeting notes, images |
| `hardware/` | KiCad projects: `satellite-pcb/`, `ground-station-pcb/`, `shared-libraries/` |
| `firmware/` | STM32 flight software, ground-station Python code, bring-up test scripts |
| `mechanical/` | CAD for structure/payload mounting, drawings, 3D-print files |
| `payload/` | The experiment itself: design notes, sensor datasheets, test data |
| `ground-station/` | System-level ground station: RF/link-budget design, antenna, software |
| `testing/` | Bench tests, the stratospheric-launch checklist and results, test reports |
| `project-management/` | Timeline, budget, team roles, risk register |
| `manufacturing/` | Purchase orders, assembly instructions, vendor quotes |
| `presentations/` | Competition slide decks and defense speaking notes |
| `tools/` | `setup_project.py` — the script that generated this structure (reusable for a future project) |

Every folder has its own `README.md` explaining what belongs in it in more
detail. Empty folders that don't need one keep a `.gitkeep` placeholder so
they survive being committed to git (git doesn't track empty directories).

## Getting started with KiCad

1. Open KiCad → **File > New Project** inside `hardware/satellite-pcb/`,
   name it `satellite-pcb`. Repeat in `hardware/ground-station-pcb/` if
   your team is designing a custom ground-station board.
2. Point both projects' library tables at `hardware/shared-libraries/`
   for any custom symbols/footprints/3D models you create, so they don't
   drift apart between the two boards.
3. Set up hierarchical schematic sheets (Power / OBC / Communications /
   Payload Interface) — see section 5 of the playbook doc for why.
4. Lock the PCB edge-cuts outline to the IntroSat 3U mounting pattern
   before placing components.

## Version control

This folder is set up with a KiCad-aware `.gitignore` at the root
(excludes KiCad backup/autosave files, firmware build artifacts, and raw
telemetry logs). If you haven't already:

```
git init
git add .
git commit -m "Initial project scaffold"
```

## Re-using this structure for a future project

`tools/setup_project.py` is a standalone, rerunnable version of the
script that built this folder. Run it against a new empty folder to
scaffold the same layout for your next competition or project:

```
python tools/setup_project.py /path/to/new/project
```

It only creates missing files/folders — safe to re-run here too if you
ever want to restore a deleted README stub.
