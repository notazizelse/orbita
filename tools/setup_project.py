#!/usr/bin/env python3
"""
setup_project.py — scaffold an electronics-engineering project folder
(the same layout used for the Orbita satellite competition project:
docs/, hardware/ with KiCad projects, firmware/, mechanical/, payload/,
ground-station/, testing/, project-management/, manufacturing/,
presentations/).

Usage:
    python setup_project.py [TARGET_DIR]

TARGET_DIR defaults to the current directory. Safe to re-run: existing
files are never overwritten, only missing files/folders are created.
"""
import os
import sys

FOLDERS = {
    "docs/requirements": """# Requirements & Official Documents

Put the official Orbita tournament materials here as you receive them:

- Regulations PDF (current: "Regulations of the International Tournament Orbita")
- Evaluation/judging criteria (published on day 1 of finals)
- IntroSat CubeSat 3U kit manual / datasheets, once the kit arrives (10-20 Sept 2026)
- Any webinar slides or organizer emails with technical constraints

Keep the exact filename + date the document was published, e.g.
`Regulations-of-the-International-Tournament-Orbita-3_2026-08.pdf`,
so you can tell which version you were working from if the rules change.
""",
    "docs/datasheets": """# Component Datasheets

One PDF per part number, named exactly after the part, e.g. `STM32L452RET6.pdf`.
Keep datasheets for everything on the BOM: MCU, radio module, sensors,
power regulators, connectors. This is what you'll actually reference at
2am when debugging a footprint or a register.
""",
    "docs/research": """# Research Notes

Background research that isn't official competition material: notes on
similar CubeSat/CanSat projects, radio propagation notes, stratosphere
environment notes (temperature/pressure profile to ~24 km), competitor
write-ups from past Orbita seasons, etc.

See `orbita-research-and-playbook.md` (or the published web version) for
the initial research summary this project started from.
""",
    "docs/meeting-notes": """# Team Meeting Notes

One markdown file per meeting, named `YYYY-MM-DD-topic.md`. Capture
decisions and action items, not a transcript. This is your paper trail
for the "Researcher" role's documentation requirements.
""",
    "docs/images": "# Reference Images\n\nDiagrams, competitor photos, whiteboard photos, screenshots — anything visual that supports docs elsewhere.\n",

    "hardware/satellite-pcb": """# Satellite PCB — KiCad Project

The flight electronics board(s) that integrate into the IntroSat CubeSat 3U
structure. Open `satellite-pcb.kicad_pro` in KiCad to start.

Suggested subsystem sheets in the schematic (hierarchical sheets):
- Power (battery protection, regulators, power distribution)
- OBC (STM32 MCU, programming/debug header, crystal, reset/boot circuit)
- Communications (radio module, matching network, antenna connector)
- Sensor/Payload interface (connector(s) out to the payload module)
- Interfaces (UART/I2C/SPI headers, test points)

Keep schematic and layout in version control as text (KiCad 7/8 native
format is git-friendly). Do NOT commit KiCad backup files — see the
root `.gitignore`.
""",
    "hardware/satellite-pcb/fab-outputs": """# Fabrication Outputs

Gerbers, drill files, pick-and-place, and BOM exports go here, one
timestamped subfolder per fab run, e.g. `2026-09-15_rev-A/`. Never
overwrite a previous fab-outputs folder — you may need to compare what
actually got built against what you intended.
""",
    "hardware/satellite-pcb/revisions": "# Archived Revisions\n\nZipped or copied snapshots of the KiCad project at each major revision (rev A, rev B, ...) taken right before you send boards to fab. Git history covers this too, but a physical snapshot is a fast sanity check without needing to check out old commits.\n",
    "hardware/ground-station-pcb": """# Ground Station PCB — KiCad Project

Any custom board for the ground station (e.g. a radio front-end,
interface board between SDR/radio and a PC, or an antenna rotator
controller). Same structure as `satellite-pcb/`. If the ground station
uses only off-the-shelf modules with no custom PCB, keep this folder
for wiring diagrams and connector pinouts instead.
""",
    "hardware/ground-station-pcb/fab-outputs": "# Fabrication Outputs\n\nSame convention as the satellite PCB: one timestamped subfolder per fab run.\n",
    "hardware/shared-libraries": """# Shared KiCad Libraries

Custom symbols, footprints, and 3D models used by BOTH boards, kept in
one place so they don't drift apart between projects:

- `symbols/` — .kicad_sym libraries
- `footprints.pretty/` — .kicad_mod footprint libraries
- `3dmodels/` — .step / .wrl 3D models for footprints

Point both KiCad projects at this folder via project-relative library
tables (Preferences > Manage Symbol/Footprint Libraries, use the
`${KIPRJMOD}/../shared-libraries/...` path) so libraries stay portable
when the whole `orbita/` folder is copied or cloned elsewhere.
""",

    "firmware/satellite-obc": """# Satellite Flight Software (STM32)

Onboard computer firmware. STM32 + Arduino IDE is the path of least
resistance for the competition; STM32CubeIDE/PlatformIO with HAL/LL
gives you more control (interrupts, low-power modes, DMA) if you have
time to invest. Structure suggestion:

- `src/` — application code
- `lib/` — drivers for sensors/radio not provided by the framework
- `test/` — unit tests / hardware-in-the-loop test scripts
- `platformio.ini` or `.ioc` (CubeMX project file) at this folder's root
""",
    "firmware/ground-station": """# Ground Station Software

Code that talks to the radio module on the ground side: receiving
telemetry, sending commands, logging. Python is a good fit here (the
regulations call out Python specifically for the radio/ground-station
side). Structure suggestion:

- `src/` — telemetry receiver, command sender, decoder
- `protocol/` — packet format definitions shared conceptually with the
  satellite firmware (keep both sides' packet structs in sync!)
- `logs/` — raw telemetry logs from tests and the actual flight (gitignored, see root .gitignore)
""",
    "firmware/test-scripts": "# Test & Bench Scripts\n\nOne-off scripts used to bring up hardware: UART loopback tests, radio range tests, sensor calibration scripts. Keep them even after the 'real' firmware supersedes them — they're the fastest way to isolate a hardware fault later.\n",

    "mechanical": """# Mechanical / CAD

3D CAD for anything beyond the PCB itself: payload mounting brackets,
structural inserts, the interface between your payload module and the
IntroSat 3U structure.

- `cad/` — native CAD files (Fusion 360 / FreeCAD / SolidWorks) plus
  exported `.step` files (step = the format everyone else can open)
- `drawings/` — dimensioned 2D drawings (PDF/DXF) for manufacturing or review
- `3d-print-files/` — sliced/ready `.stl` and `.3mf` files for printed parts
""",

    "payload": """# Payload / Experiment

The actual science or engineering experiment this satellite carries.
This is the part that's yours to invent — see the task ideas doc for
starting points (spectrometer, IMU-based attitude study, radiation
counter, materials test coupon, camera experiment, etc.)

- `experiment-design/` — concept notes, requirements, success criteria
- `sensor-datasheets/` — datasheets specific to the payload's sensors
- `test-data/` — recorded data from bench tests and the stratospheric flight
""",

    "ground-station": """# Ground Station (System Level)

System-level ground station work that isn't the PCB itself (that's in
`hardware/ground-station-pcb/`) and isn't the software (that's in
`firmware/ground-station/`):

- `rf-design/` — link budget calculations, frequency/channel plan, antenna selection notes
- `antenna/` — antenna build notes, SWR measurements, radiation pattern estimates
- `software/` — tracking scripts, pass-prediction if you attempt Doppler
  correction, telemetry dashboards
""",

    "testing": """# Testing

- `bench-tests/` — day-to-day hardware bring-up and verification test logs
- `stratospheric-launch/` — everything specific to the ~20-24 km balloon
  test: pre-flight checklist, thermal/vacuum considerations, recovered
  data, post-flight analysis
- `test-reports/` — formal writeups you'll reuse in the project defense
""",

    "project-management": """# Project Management

- `timeline.md` — your team's internal schedule against the official
  Orbita deadlines
- `budget.md` — parts cost tracking (useful if your National Committee
  or school needs a budget justification)
- `team-roles.md` — who owns Design/Electrical/Radio/Research per the
  competition's required 4-role team structure, plus your mentor's contact info
- `risk-register.md` — things that could go wrong (kit shipping delay,
  radio range too short, battery certification for the flight, etc.) and your mitigation plan
""",

    "manufacturing": """# Manufacturing

- `purchase-orders/` — what you ordered, from where, tracking numbers
- `assembly-instructions/` — step-by-step build/solder instructions for
  reproducibility (useful if a teammate assembles a board without you)
- `vendor-quotes/` — PCB fab and assembly quotes
""",

    "presentations": """# Presentations

- `slides/` — the competition deliverable decks (max 14 slides / PDF
  per the Cosmonautics Project Contest rules; satellite competition
  defense deck as well)
- `defense-scripts/` — speaking notes for the 7-minute presentation + 3-minute Q&A format
""",
}


GITKEEP_ONLY = [
    "hardware/satellite-pcb/libraries/symbols",
    "hardware/satellite-pcb/libraries/footprints.pretty",
    "hardware/satellite-pcb/libraries/3dmodels",
    "hardware/shared-libraries/symbols",
    "hardware/shared-libraries/footprints.pretty",
    "hardware/shared-libraries/3dmodels",
    "firmware/satellite-obc/src",
    "firmware/satellite-obc/lib",
    "firmware/satellite-obc/test",
    "firmware/ground-station/src",
    "firmware/ground-station/protocol",
    "firmware/ground-station/logs",
    "mechanical/cad",
    "mechanical/drawings",
    "mechanical/3d-print-files",
    "payload/experiment-design",
    "payload/sensor-datasheets",
    "payload/test-data",
    "ground-station/rf-design",
    "ground-station/antenna",
    "ground-station/software",
    "testing/bench-tests",
    "testing/stratospheric-launch",
    "testing/test-reports",
    "manufacturing/purchase-orders",
    "manufacturing/assembly-instructions",
    "manufacturing/vendor-quotes",
    "presentations/slides",
    "presentations/defense-scripts",
]


ROOT_FILES = {
    ".gitignore": """# --- KiCad ---
*.bak
*-bak
_autosave-*
*.kicad_pcb-bak
*.kicad_sch-bak
*.kicad_prl
fp-info-cache
**/*-backups/
*.lck
*.kicad_pro-journal
*-journal
*.rpt.bak

# --- 3D model caches ---
*.3dshapes-cache/

# --- Python ---
__pycache__/
*.pyc
.venv/
venv/

# --- Firmware build artifacts (PlatformIO / STM32CubeIDE / CubeMX) ---
.pio/
Debug/
Release/
*.o
*.elf
*.hex
*.bin
*.map

# --- OS junk ---
.DS_Store
Thumbs.db
desktop.ini

# --- Editor ---
.vscode/
*.swp
""",
}


def write_if_missing(path, content):
    if os.path.exists(path):
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    target = os.path.abspath(target)
    os.makedirs(target, exist_ok=True)

    created, skipped = 0, 0

    for rel, content in ROOT_FILES.items():
        if write_if_missing(os.path.join(target, rel), content):
            created += 1
        else:
            skipped += 1

    for rel, content in FOLDERS.items():
        d = os.path.join(target, rel)
        os.makedirs(d, exist_ok=True)
        if write_if_missing(os.path.join(d, "README.md"), content):
            created += 1
        else:
            skipped += 1

    for rel in GITKEEP_ONLY:
        d = os.path.join(target, rel)
        os.makedirs(d, exist_ok=True)
        if write_if_missing(os.path.join(d, ".gitkeep"), ""):
            created += 1
        else:
            skipped += 1

    print(f"Scaffolded project at {target}")
    print(f"  {created} file(s) created, {skipped} already existed and were left untouched.")
    print("  Next: open KiCad and create your project(s) under hardware/<board-name>/")


if __name__ == "__main__":
    main()
