# Payload Mission Ideas — Larva / Insect Biology Track

Compiled 12 September 2026, building on last year's larva-study mission.
This is research material for drafting your paper, not a finished
methods section — cite the primary sources directly once you pick a
final design.

A note on last year's project: I couldn't find a public write-up of your
own team's 2025 larva experiment (student team reports for this kind of
tournament generally aren't published online), so this document instead
compiles the real published science on flying insect larvae to near-space
and orbit — the literature your paper should be citing and positioning
itself against — plus concrete mission variants for this season built from
it.

## 1. What the published science actually shows

**Drosophila melanogaster (fruit fly), Foton-M4 (44.5 days, 2014) and
ISS (12 days).** Larvae were housed in 50 ml Falcon-type tubes with
standard nutrient medium, in BB-2 blocks inside BB-1F flight hardware.
Findings: reduced expression of metabolic, morphogenesis, cell
differentiation and cytoskeletal-organization genes during flight — more
pronounced on the *shorter* 12-day mission than the 44.5-day one, which
is a genuinely counterintuitive result worth engaging with in your
introduction. No morphological abnormalities were observed. Within 12–24
hours of return to Earth, transcription patterns largely reversed
(morphogenesis/cytoskeletal genes back up, cuticle/proteolytic genes back
down), and fertility was preserved across generations. Source: [PLOS ONE
— Development of Drosophila melanogaster under different duration space
flight](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0166885).

**NASA Drosophila Habitat hardware** (design reference, not a flight
result). Aluminum cassettes with mesh screens on opposing faces for
passive gas exchange, removable food trays swapped without a glovebox,
passive temperature/humidity control "to ISS levels," and an in-flight
camera for day/night-cycled video of the whole cassette over a ~24-day
culture. This is a good structural analog for a shoebox-scale payload
chamber. Source: [NASA — Drosophila Habitat hardware
development](https://ntrs.nasa.gov/api/citations/20190001070/downloads/20190001070.pdf).

**Stratospheric balloon biology, generally (NASA HASP program —
"Ballooning for Biologists").** This is the closest precedent to what
you're actually doing (balloon, not orbit) and the most citable methods
reference for your paper. Key numbers for your introduction/methods:
at ~32–36 km, pressure is ~0.96 kPa and temperature ~‑73°C; ionizing
radiation runs ~0.064–0.18 mGy/day (comparable to Mars-rover surface
measurements); UV intensity reaches 86–109 W/m², dominated by UVC
(200–280 nm) that never reaches the ground because the ozone layer
absorbs it — meaning a stratospheric flight is one of very few ways to
expose a living sample to UVC at all. Organisms flown successfully:
bacterial endospores, fungal spores, lichens, moss, algae, cyanobacteria,
yeast, tardigrades — the common thread is that they tolerate extended
dormancy without active life support. Landing shock is ~10 g vertical,
~5 g transverse. Source: [NASA — Ballooning for Biologists: Mission
Essentials for Flying Life Science Experiments to Near
Space](https://ntrs.nasa.gov/api/citations/20190025902/downloads/20190025902.pdf?attachment=true).

**MARSBOx** — a stratospheric balloon payload testing fungal and
bacterial endurance as a Mars-analog mission, same rationale (stratosphere
≈ closest Earth analog to Martian surface radiation/UV/pressure). Source:
[Frontiers in Microbiology —
MARSBOx](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.601713/full).

**Tenebrio molitor (mealworm) behavioral/radiation sensitivity
(ground-based studies).** Mealworm larvae show measurable behavioral
change under weak electromagnetic/UV irradiation, and their toll immune
pathway responds to low-intensity UVB. This matters for your design
because it means *behavior* (not just survival/mass) is a legitimate,
literature-supported outcome variable for a mealworm experiment — and
mealworms are cheap, robust, legal to ship/handle, and easy to source
locally, which is exactly why they're a strong choice for a
resource-constrained student payload. Sources: [Weak electromagnetic
irradiation effects on Tenebrio molitor
behavior](https://link.springer.com/article/10.1007/s11055-010-9335-z),
[Low-intensity UVB and the toll pathway in Tenebrio
molitor](https://doi.org/10.1163/23524588-bja10288).

**Bombyx mori (silkworm) — Shennong Kaiyu-2, Chongqing University,
13 December 2025.** A silkworm pupa/chrysalis flew aboard an 8.3 kg
sealed-ecosystem payload on a Kuaizhou-11 launch and completed full
metamorphosis in orbit — the first time an insect has completed
metamorphosis in space, with the resulting butterfly photographed moving
and flying inside the sealed cabin. The chamber held pressure,
temperature, and humidity within set bounds throughout. This is very
recent (three months before this document) and gives you a strong,
citable "state of the art" to position a stratospheric analog against.
Silkworm is also the one species on this list with a direct cultural and
economic tie to Uzbekistan, historically one of the Silk Road's major
sericulture regions — a genuinely distinctive hook for your introduction
that a generic mealworm study wouldn't have. Source: [AiF — Chinese
scientists conduct a butterfly-hatching experiment in
space](https://aif.ru/society/science/v-kitae-babochka-vylupilas-iz-kokona-na-bortu-kosmicheskogo-modulya).

## 2. Mission ideas, ranked by how buildable they are this season

**A. Comparative mealworm (Tenebrio molitor) survival & development
study — the safest, most buildable option.** Two or more sealed
compartments, each with a set of larvae: one shielded (thicker aluminum
or a UV-blocking window) and one exposed (thin window, full-spectrum
including UVC). Log temperature, humidity, and UV dose per chamber
during flight; assess survival rate, mass change, and time-to-pupation
after landing, against a ground-control group kept in identical chambers
that never fly. This directly extends the Tenebrio literature above from
"weak EM/UVB, on a bench" to "real stratospheric UVC and ionizing
radiation, in flight" — a genuinely novel comparison, not a repeat of
existing work.

**B. Add a radiation-dose correlation.** Same design as A, but add a
simple dosimeter (or a shared one read by both chambers via a
duty-cycled shutter) so you can plot individual/cohort outcome (survival,
mass, time-to-pupation) against *measured* dose rather than assumed dose
from altitude alone. This is what turns "we flew bugs and some lived"
into a quantitative result a paper can actually defend — and it's the
single highest-value addition given what separated the 2025 standings
(experiments that produced a measurable result vs. ones that didn't).

**C. Silkworm (Bombyx mori) cocoon/pupa stratospheric analog.** Fly
silkworm pupae in their cocoons through the stratosphere and assess
post-flight eclosion (emergence) success and timing versus ground
controls — a stratospheric-balloon analog of the December 2025 orbital
result, using a species with real local relevance. Silk moths are
domesticated, non-invasive, legal, and Uzbekistan has existing sericulture
infrastructure to source healthy stock from. This is the highest-novelty,
highest-narrative-value option, and the one most likely to stand out to
judges specifically because it isn't a generic "put bugs in a box"
project — but cocoons are bulkier than mealworm larvae, so check they
actually fit your payload's mass/volume budget early.

**D. Post-flight behavioral assay, on either species.** Add a short
phototaxis or locomotion test (timed movement toward/away from a light
source, or distance traveled in a fixed period) on surviving larvae
immediately after recovery and again after a recovery period, compared
to ground controls. The Tenebrio EM-irradiation literature already
establishes behavior as a measurable, publishable endpoint, and it's
essentially free to add — a phone camera and a stopwatch, no new payload
hardware required.

**E. Multi-generation follow-up (if your timeline allows it).** The
Drosophila studies above tracked effects across generations bred *after*
return to Earth. If your species reproduces fast enough within your
post-competition writing window, tracking F1 offspring of flown vs.
ground-control parents (survival, developmental time, any morphological
anomalies) would be a genuinely strong result — but only commit to this
if you're confident you'll have the weeks needed after the flight to see
it through before your paper is due.

Recommendation for a first build: **A + B** (mealworm, shielded vs.
exposed, with a dosimeter) is the most defensible scope for a 4-week
build-and-fly window — buildable, safe, and it produces a real
quantitative result either way (a null result on survival difference is
still a result, given the equipment measured actual dose). Layer in **D**
essentially for free. Treat **C** as next season's stretch goal, or a
parallel Cosmonautics Project Contest submission if your team has bandwidth,
since that track doesn't require the CubeSat hardware at all.

## 3. Payload chamber & board integration

This is what the Electrical Engineer and Design Engineer roles need to
build to support any of the above.

**Chambers.** Two (or more) small sealed compartments within the
payload bay, each independently vented through a fine mesh (per the NASA
Drosophila Habitat approach — mesh gives gas exchange without losing
containment) and each behind a different window material: one plain
polycarbonate/acrylic window (UV-transmitting, "exposed" arm) and one
UV-blocking window or thicker shielded wall (the "shielded" arm — even a
straightforward aluminum cover with no window at all is a valid shielded
condition if you're not trying to isolate UV specifically from ionizing
radiation). Keep a third, unflown ground-control set of the same chambers
on the bench for a true control.

**Sensors, one set per chamber where budget allows, otherwise shared
and multiplexed:**

| Sensor | Measures | Why |
|---|---|---|
| Temperature + humidity (e.g., a BME280/SHT31-class I2C sensor) | Chamber microclimate | Ties biological outcome to actual experienced conditions, not just "it was cold up there" |
| UV index (e.g., a VEML6075-class sensor) | UVA/UVB (most UV sensors don't reach UVC — say so explicitly in your methods rather than overclaiming) | Differentiates the exposed vs. shielded arms quantitatively |
| Radiation dosimeter (a simple Geiger-tube module, or even a passive film badge read out post-flight if a real-time sensor won't fit your power/mass budget) | Ionizing dose | The single most important addition per idea B above |
| Camera (e.g., an OV2640-class module, time-lapse stills rather than continuous video to save power/storage) | Larva movement/behavior in-flight, chamber integrity | Directly supports mission idea D and gives you flight footage for the defense presentation |
| IMU (likely already on your OBC board) | Shock/vibration at launch and landing | Lets you rule out "died from impact" vs. "died from radiation/cold" as competing explanations — important for a defensible methods section |

**Board-level implications:** route all chamber sensors to the OBC over
I2C (put each chamber's sensors on the same bus with distinct addresses,
or use an I2C multiplexer if two chambers need identically-addressed
parts); log every reading with a timestamp to onboard flash/SD rather
than relying solely on the radio downlink, since biology outcomes are
scored on the ground after recovery, not from live telemetry; keep the
camera on its own power rail with a hard current limit, since image
sensors are usually the single largest peak-current consumer on a payload
like this and you don't want it browning out the OBC. Add this sensor set
to your existing `hardware/satellite-pcb/README.md` subsystem sheet list
as a "Payload Sensors" sheet, and keep the chamber CAD in
`mechanical/cad/` in step with the electrical design — the two need to be
developed together from day one, not integrated at the end.

## 4. Research paper — suggested structure

1. **Title** — name the species and the specific comparison, not just
   "larvae in space" (e.g., "Stratospheric UV and ionizing radiation
   exposure effects on *Tenebrio molitor* survival, development, and
   phototactic behavior: a high-altitude balloon study").
2. **Abstract** — one paragraph: question, method, headline result.
3. **Introduction** — the case for near-space biology as a Mars/space
   analog (cite the HASP/MARSBOx altitude environment numbers), what's
   already known (Drosophila spaceflight results, Tenebrio ground-based
   radiation/EM sensitivity, the December 2025 silkworm metamorphosis
   result if relevant to your chosen species), and the specific gap your
   flight fills.
4. **Hypothesis** — stated as a testable prediction, not a question.
5. **Methods** — species and sourcing, chamber design and materials
   (with the shielded/exposed/ground-control structure), sensor suite and
   sampling rate, flight profile (expected altitude/duration from your
   ground station log), and your outcome measures and how each was
   scored.
6. **Results** — environmental data per chamber (temperature/humidity/UV/
   dose time series) alongside biological outcomes (survival %, mass
   change, time-to-pupation/eclosion, behavioral assay scores), with
   ground-control comparison throughout.
7. **Discussion** — how your result compares to the Drosophila and
   Tenebrio literature above; what a null result would still tell you
   given real measured dose data; honest limitations (single flight, no
   replicate, small sample size, uncontrolled cabin micro-vibration, etc.).
8. **Conclusion** — one paragraph, plus a concrete next-season follow-up
   (this is also good material for the "Researcher" role's mission-concept
   documentation deliverable).
9. **References** — the sources listed in section 1 above, plus whatever
   else you pull in while drafting; keep full citations in
   `docs/research/` as you go so you're not reconstructing them the night
   before the deadline.

## 5. Sources

- [PLOS ONE — Development of *Drosophila melanogaster* under different duration spaceflight](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0166885)
- [NASA — Drosophila Habitat hardware development (PDF)](https://ntrs.nasa.gov/api/citations/20190001070/downloads/20190001070.pdf)
- [NASA — Ballooning for Biologists: Mission Essentials for Flying Life Science Experiments to Near Space (PDF)](https://ntrs.nasa.gov/api/citations/20190025902/downloads/20190025902.pdf?attachment=true)
- [Frontiers in Microbiology — MARSBOx: Fungal and Bacterial Endurance From a Balloon-Flown Analog Mission in the Stratosphere](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2021.601713/full)
- [Neuroscience and Behavioral Physiology — Effects of Weak Electromagnetic Irradiation on Various Types of Behavior in the Mealworm *Tenebrio molitor*](https://link.springer.com/article/10.1007/s11055-010-9335-z)
- [Journal of Insects as Food and Feed — Low intensity UVB irradiation increases expression of the toll pathway in *Tenebrio molitor*](https://doi.org/10.1163/23524588-bja10288)
- [AiF — Chinese scientists conduct a butterfly-hatching (silkworm metamorphosis) experiment aboard Shennong Kaiyu-2](https://aif.ru/society/science/v-kitae-babochka-vylupilas-iz-kokona-na-bortu-kosmicheskogo-modulya)
- [ScienceDirect — Fruit fly *Drosophila melanogaster* as a model organism for space biology research](https://www.sciencedirect.com/science/article/abs/pii/S2214552425001464)
