# ARC-24 + CONVECT — recommended mission

International Space Tournament «Орбита» (spaceeducation.info), 2026 season.
Decision record, 12 September 2026. Supersedes `MAGSEP-mission-spec.md`,
which was written against the wrong competition.

**One board, one question: what happens to a circuit board when the air goes away.**
Two coupled experiments sharing one independent variable — ambient pressure,
swept continuously by the balloon from 1013 mbar to ~29 mbar at 24 km.

| | Score |
|---|---|
| ARC-24 — PCB dielectric breakdown across the pressure sweep | 87.9 / 100 |
| CONVECT — collapse of convective cooling vs pressure | 86.6 / 100 |

They share a board, sensors and a flight, so fly both. CONVECT is also the
insurance: no high voltage, no approval needed, still a complete result.

---

## 1. Competition facts (official documents)

[Tournament page](https://spaceeducation.info/en/orbita/) ·
[Regulations PDF, updated 25 June 2026](https://spaceeducation.info/wp-content/uploads/2026/08/Regulations-of-the-International-Tournament-Orbita-3.pdf)

- **Final: 26 October – 1 November 2026.** Forum 31 October.
- **Preparation: 10 September – 26 October.** Kits ship 10–20 September.
  Minimum 3 general webinars + 3 individual expert consultations.
- Platform: free **3U CubeSat kit without payload**, based on IntroSat.
- **Stratospheric launch, up to 24 km** — the environment IS available at judging.
- Team: exactly 4 (ages 12–18, optionally one university student ≤21) + mentor
  who may not do technical work.
- Roles: **Engineer** (payload design, 3D, integration) · **Programmer**
  (electronics, data/comms software, MCU) · **Researcher** (scientific
  justification, modelling, interpretation, presentation) · **Radio Technician**
  (radio module + ground station software).
- Deliverables at final: integrated CubeSat with payload, ground station
  software + testing documentation, defence before the Expert Council.
- Scoring: preparatory-stage work + defence. **Rubric published only on day 1.**
- Missing a mandatory assignment on time = disqualification.

**44 days to the final. ~8 days to the PCB fab deadline.**

## 2. Why the flight is a sweep, not an exposure

Two or three hours is far too short to *change* anything — no useful dose, no
material ageing, no biology. But the ascent carries the payload continuously
through two decades of pressure and ~70 °C of temperature. It hands you a
**curve**, not a before-and-after. Every strong mission treats pressure or
temperature as a swept independent variable.

ISA pressure: 1013 mbar ground · 120 at 15 km · 55 at 20 km · **29 at 24 km**.

## 3. ARC-24 physics

Air's breakdown voltage depends on pressure × gap distance and is **not
monotonic** — Paschen's law, minimum ~327 V near 7.5 Torr·mm for air.
At 24 km (~22 Torr) a 0.3 mm gap has pd ≈ 6.6 Torr·mm: **ordinary PCB
clearances sit at their most vulnerable exactly at this competition's ceiling.**

Gap sizing (computed for this report; ISA + Paschen with A=15/cm·Torr,
B=365 V/cm·Torr, γ=0.01 — design estimates, not measurements):

| Gap | p at its Paschen minimum | Altitude | In flight? |
|---|---|---|---|
| 0.10 mm | 111 mbar | 15.5 km | yes |
| 0.15 mm | 74 mbar | 18.1 km | yes |
| 0.20 mm | 56 mbar | 19.9 km | yes |
| 0.30 mm | 37 mbar | 22.5 km | yes |
| 0.50 mm | 22 mbar | 25.8 km | just above — control |

At a fixed 500 V, each gap breaks down over a *band* of altitudes:

| Gap | Breakdown band | Observation during ascent |
|---|---|---|
| 0.10 mm | 6.7 – 19.9 km | arcs, then **self-extinguishes at ~19.9 km** |
| 0.20 mm | 11.3 – 24.3 km | arcs from 11.3 km, still arcing at ceiling |
| 0.30 mm | 13.9 – 26.9 km | arcs from 13.9 km |
| 0.50 mm | 17.2 km up | arcs late |
| 2.00 mm | 26.1 km up | **never** — negative control |

That staircase — breakdowns appearing at four predicted altitudes in a
predicted order, and a narrow gap *recovering* as it passes its minimum — is
the whole experiment. It cannot be explained by "it was high so it arced."

**Why not in a lab:** reaching these pressures needs a controlled vacuum
chamber. The balloon gives a clean, slow, monotonic sweep for free.

**The open question:** classical Paschen assumes uniform parallel-plate
fields. A PCB is not that. The one directly relevant measurement
([arXiv 2010.06570](https://arxiv.org/pdf/2010.06570)) found **405 V at 5 mbar**
for a real PCB trace vs 327 V classical, plus unexplained saturation below
10⁻² mbar — but in a vacuum chamber, mostly *below* stratospheric pressures,
on one geometry. Nobody has flown an array of PCB gap geometries, coated and
uncoated, through the real stratospheric sweep and compared it to both
classical Paschen and IPC-2221.

**The standard you get to test:** IPC-2221 sets conductor clearance by
voltage and treats external conductors differently below/above **3050 m**,
with a smaller allowance for permanently coated conductors. Your flight goes
8× higher. Coated vs uncoated at 24 km asks whether that coating allowance
holds where it has never been characterised.

## 4. Board design (this is the PCB-learning part)

- **Gap array:** 5 widths (0.10/0.15/0.20/0.30/0.50 mm) × 2 surface treatments
  (bare, conformal-coated) = 10 cells.
- **Geometry held constant:** identical pad shape, copper thickness, corner
  radius across all cells. Geometry shifts the whole curve, so it must be the
  controlled variable.
- **Current limiting:** 10 MΩ in series per cell → 60 µA max at 600 V. This is
  both the safety measure and the measurement principle.
- **Detection:** low-side sense resistor per cell into a multiplexed ADC at
  ≥100 Hz; breakdown = current *step* from leakage floor to limit. Optional
  photodiode for independent optical confirmation.
- **Voltage measurement:** 100 MΩ : 100 kΩ divider into its own ADC channel.
  Measure the applied voltage; the boost converter will drift with temperature.
- **Two modes alternating:** fixed 500 V hold (gives the altitude staircase)
  and 0→600 V ramp over ~20 s (gives onset voltage per cell → the curve itself).
- **Pressure sensor rated below 29 mbar**, logged on the same timestamp.
  Measure pressure directly — never infer from model altitude.
- **Layout:** HV section isolated with guard ring + slot, away from OBC and
  radio, own return path. Discharges radiate broadband.

## 5. CONVECT (same board)

Four matched heated elements, each at known constant power, each with its own
temperature sensor, differing only in surrounding copper: bare pad · large
pour · thermal via array to an inner plane · deliberately thermally-relieved
pad. R_th = ΔT / P, plotted against pressure through the ascent.

Tells a PCB designer **how much of the cooling their ground testing shows is
convection that will not exist in space — per layout technique.** This is the
rigorous version of "map the heat on the board": a measured collapse of a heat
transfer mechanism against a swept variable, not a thermal photograph.

## 6. Experimental design

- **Independent:** pressure (swept, measured). Secondary: gap width, surface
  treatment, copper structure, applied voltage.
- **Dependent:** onset voltage per cell; breakdown state vs pressure; R_th per structure.
- **Controls:** 2 mm gap (must never fire); identical twin board tested on the
  ground before and after; unpowered cells monitored for leakage; isolated pad
  as low-conduction reference.
- **Repetitions:** ramp repeats every ~60 s → ~100 onset measurements per cell;
  descent re-traverses the same pressures (built-in repeat + hysteresis check).
- **Covariate:** Geiger count rate. Cosmic rays supply seed electrons for
  breakdown initiation, and the Regener–Pfotzer maximum (~15–26 km) sits inside
  the flight band. Resolving the coupling in one flight is unlikely; proposing
  and testing it is what a researcher does.
- **Uncertainty:** propagate pressure accuracy, **fab etch tolerance on gap
  width (typically ±20% — ask your fab house)**, divider tolerance and its temp
  drift, ADC noise. Band every plotted point.
- **Falsification:** if onsets don't follow a Paschen-shaped curve, or narrow
  gaps don't extinguish above their minima, classical theory fails for this
  geometry — plausible given the arXiv result, and interesting, not a failure.

**Figures:** onset voltage vs pd with classical Paschen overlaid (the defence
centrepiece) · altitude staircase · coated vs bare at matched pd · ascent vs
descent hysteresis · R_th vs pressure for four structures · onset scatter vs
Geiger rate.

## 7. Safety — read before ordering

Several hundred volts. Made safe by **current limiting by design**, not care:
10 MΩ per cell caps current at tens of µA; HV fully enclosed, no exposed
conductors; bleed resistors discharge on power-down; interlocked off on the
ground. **Mentor must review. Organizers must approve in writing before you
travel.** If refused → fly CONVECT + context sensors, still a complete mission.

## 8. Risks

| # | Risk | Mitigation |
|---|---|---|
| R1 | Organizers refuse HV payload | Ask in the first expert consultation, in writing, this week. CONVECT is the fallback |
| R2 | Etch tolerance ≠ designed gaps | Measure every gap under magnification post-fab; analyse with *measured* widths |
| R3 | Discharges disturb OBC/radio | Separation, guard ring, slot, filtered supply; log packet errors as a secondary result |
| R4 | Moisture/contamination leakage mistaken for breakdown | Clean and bake; monitor unpowered cells; require a current *step*, not a slow rise |
| R5 | Boost converter drifts at −55 °C | Measure applied voltage; freezer-qualify; keep HV block insulated |
| R6 | Balloon falls short of 24 km | Four events already by 22.5 km; narrow gaps produce data from 6.7 km up |
| R7 | **PCB fab lead time misses the flight** | **Order by ~20 Sept.** Perfboard fallback with machined gaps |
| R8 | Payload doesn't fit IntroSat structure | Measure the kit the day it arrives, before finalising outline |
| R9 | Payload not recovered → data lost | Log to SD *and* downlink a reduced live summary — puts Radio Technician on critical path |
| R10 | Council reads it as a stunt | Open with IPC-2221 altitude derating + the arXiv measurement, then show hardware |

## 9. BOM (planning estimates, not quotes)

| Item | Qty | Est. |
|---|---|---|
| Custom PCB, 2-layer, gap array | 5 | ~3,000 ₽ |
| Adjustable HV module 0–1 kV, low current | 2 | ~4,000 ₽ |
| 10 MΩ 1% HV-rated resistors | 20 | ~800 ₽ |
| 100 MΩ + 100 kΩ divider resistors | 6 | ~600 ₽ |
| Analog mux + precision op-amps | 4 | ~1,200 ₽ |
| Barometric sensor rated **below 29 mbar** | 2 | ~2,000 ₽ |
| Temperature sensors | 8 | ~900 ₽ |
| Precision heater resistors | 8 | ~400 ₽ |
| Geiger counter module | 1 | ~5,000 ₽ |
| Conformal coating | 1 | ~1,500 ₽ |
| SD module, connectors, harness, enclosure | — | ~2,000 ₽ |
| **Total** | | **~21,400 ₽** (~16,000 ₽ without Geiger) |

Many common barometric sensors bottom out at 300 mbar — check the low-pressure
limit before ordering.

## 10. Schedule — 44 days

| Window | Exit criterion |
|---|---|
| Sep 12–15 | HV approval question sent in writing; kit measured on arrival; parts ordered from two suppliers each |
| Sep 16–20 | KiCad schematic + layout done; Paschen prediction spreadsheet written. **Board files to fab by 20 Sept** |
| Sep 21–30 | Firmware: ramp/hold sequencing, multiplexed sampling, event detection, logging; GS telemetry format; freezer-test converter and sensors |
| Oct 1–8 | Board arrives; every gap measured under magnification; sea-level tests confirm *nothing* breaks down at ground pressure (a control measurement); divider calibrated |
| Oct 9–16 | Any low-pressure access (university chamber, sealed jar + hand pump) for partial validation; otherwise full 3-hour unattended end-to-end rehearsal |
| Oct 17–24 | Integration into 3U structure, insulation, vibration check, pre-flight checklist. Defence built with the prediction plot drawn **before** flight |
| Oct 25–26 | Travel; two of every critical spare packed |
| Oct 26–Nov 1 | Final tasks, launch, recovery, analysis, defence |

**The one date that matters: ~20 September for the PCB order.**

## 11. Work split (the four official roles)

- **Engineer** — board outline and 3U integration, gap-array geometry, guard
  ring and isolation slot, HV enclosure, insulation, post-fab gap measurement.
- **Programmer** — ramp/hold sequencing, ≥100 Hz multiplexed sampling, event
  detection distinguishing a true current step from leakage drift, SD logging,
  reduced live telemetry.
- **Researcher** — the Paschen prediction computed and plotted *before* flight,
  IPC-2221 framing, uncertainty propagation, covariate analysis, defence narrative.
- **Radio Technician** — ground station and live summary downlink, which is the
  backup copy of the headline result if the payload is not recovered.

All four roles carry something the defence depends on — which matters when each
of you is individually assessed.

## 12. Sources

- [Tournament page](https://spaceeducation.info/en/orbita/) · [Regulations PDF](https://spaceeducation.info/wp-content/uploads/2026/08/Regulations-of-the-International-Tournament-Orbita-3.pdf)
- [Paschen curve for a PCB trace in low vacuum (arXiv 2010.06570)](https://arxiv.org/pdf/2010.06570)
- [Paschen's law — equation and air coefficients](https://en.wikipedia.org/wiki/Paschen%27s_law)
- [IPC-2221B conductor spacing tables and the 3050 m threshold](https://www.smpspowersupply.com/ipc2221pcbclearance.html)
- [Using an IPC-2221 calculator for high-voltage design (Altium)](https://resources.altium.com/p/using-an-ipc-2221-calculator-for-high-voltage-design)
- [NASA-HDBK-4007 Spacecraft High-Voltage Paschen and Corona Design Handbook](https://standards.nasa.gov/standard/NASA/NASA-HDBK-4007)
- [Hands et al. (2016), Space Weather — Pfotzer–Regener maximum in dose equivalent](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016SW001402)
- [Measurement of the Regener–Pfotzer maximum with different detectors](https://pubmed.ncbi.nlm.nih.gov/36005953/)
- [TASEC-Lab — convective heat transfer on stratospheric balloon missions (Acta Astronautica)](https://www.sciencedirect.com/science/article/pii/S0094576522001862)
- [NASA — Ballooning for Biologists: near-space environment by altitude](https://ntrs.nasa.gov/api/citations/20190025902/downloads/20190025902.pdf?attachment=true)
