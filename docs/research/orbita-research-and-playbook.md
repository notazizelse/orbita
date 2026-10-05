# Orbita International Space Tournament — Research & Project Playbook

Compiled 10 September 2026. This is a working reference, not an official
document — always cross-check against the current Regulations PDF and
organizer communications, since rules and dates get revised.

## 1. What Orbita is

"Orbita" (Russian: «Орбита») is an international space-education tournament
for school and university students, run by the Russian engineering company
**Obrazovaniye Budushchego** ("Education of the Future") together with the
**Center for Engineering, Space, and Natural Science Education**, with
support from **Roscosmos**, the Presidential Grants Foundation, the
Skolkovo Foundation, NTI, and a network of national committees and
planetariums in participating countries.

It brings together teams from Russia, Uzbekistan, Kazakhstan, Kyrgyzstan,
Belarus, Armenia, India, the UAE, Saudi Arabia and Malaysia (the exact
country list shifts slightly year to year) for two parallel competitions
plus an education forum:

- **Satellite Construction Competition** — teams build a CubeSat 3U
  satellite around a supplied kit, integrate a self-designed payload, and
  fly it on a high-altitude balloon to the stratosphere.
- **Cosmonautics Project Contest** — a broader space-engineering project
  competition judged on a written summary, a slide deck, a physical
  model/prototype, and a live defense — doesn't require the CubeSat kit.
- **International Space Education Forum** — talks, museum visits, and
  meetings with cosmonauts and agency representatives, run alongside the
  finals.

Your `orbita` folder is set up for the Satellite Construction Competition,
since that's the one with a real KiCad-designed PCB in it, but the
`presentations/` and `project-management/` folders work for the Project
Contest too.

## 2. How the competition has run in past seasons

**2024 season.** Finals held 27 May – 1 June 2024. Four teams (Russia,
Kazakhstan, Kyrgyzstan, Uzbekistan), 25 participants aged 15–19, working
with CubeSat 3U satellites from the Introsat constructor kit, flown to
altitudes up to 24 km. Structure: satellite-building competition + a
training course for mentors + the education forum.

**2025 season.** Finals held 19–25 August 2025 in Moscow (venue "KAIT №20")
and Korolyov (the "Kvantorium" technology park). Teams from Russia,
Uzbekistan, India and the UAE. All built CubeSats around the IntroSat 3U
kit and flew scientific payloads to roughly 20 km. Every satellite
survived and returned telemetry during flight, but not every onboard
experiment produced usable results — and that gap between "the hardware
worked" and "the experiment worked" is explicitly what separated the
standings, decided in expert defense sessions at the Moscow Museum of
Cosmonautics. **Team Uzbekistan won the satellite-building competition.**
The Cosmonautics Project Contest had three winners (two from India, one
from Russia). The forum included visits to RKK Energia and meetings with
cosmonauts Yuri Usachyov and Valery Tokarev, framed around STEM
cooperation across BRICS and EAEU countries.

**2026 season (current).** National selection phases run June 1 –
September 10/15, 2026. IntroSat 3U kits ship to finalist teams
10–20 September 2026 (i.e., right now, if your team has qualified).
Preparatory development runs through 26 October 2026. Finals run
26 October – 1 November 2026, with the forum on 31 October, in the
Korolyov/Moscow area again.

**The pattern to take from this:** the kit and the stratospheric flight
are constant every year; what changes is the specific payload/mission
theme, the judging weight given to "did the experiment produce a result"
vs. "did the satellite survive," and the exact finalist country list. Build
for reliability first — a satellite that transmits clean telemetry the
whole flight beats a more ambitious payload that goes silent halfway up.

## 3. Technical requirements (2026 regulations)

**Platform.** A 3U CubeSat structure from the IntroSat educational kit,
supplied free to finalists (arrives without payload — you design and
integrate that part yourselves).

**Onboard computer.** STM32-family microcontroller, programmed via Arduino
IDE (or STM32CubeIDE/PlatformIO if your team wants finer control).
Interfaces called out explicitly: UART, I2C, SPI.

**Communications.** A radio module on the satellite talking to a ground
station you build/operate. Firmware is C/C++; ground-station-side tooling
is expected in Python. You are responsible for both ends of the link.

**Payload.** A custom experimental module of your own design, mechanically
integrated into the 3U structure — this is where your project's science
or engineering question lives. 3D CAD skills (for fasteners and
custom parts) and access to 3D printing or laser cutting are called out as
valuable.

**Environment.** Stratospheric balloon flight to ~20–24 km. That's roughly
-50 to -60°C ambient air temperature, down to a few percent of sea-level
atmospheric pressure, direct UV exposure, and a violent shock/vibration
profile at launch and especially at parachute deployment and landing.
Micro-gravity is only approximated briefly near apogee — this is not a
vacuum/orbital thermal test, but it's a genuinely harsh environment for a
board that was only bench-tested at room temperature.

**Team structure.** Exactly 4 students (12–18, one university student up
to 21 allowed) filling four defined roles, plus one non-participating
adult mentor:

- **Design Engineer** — mechanical/structural integration, CAD, payload-to-structure fit
- **Electrical Engineer** — PCB design, power system, firmware bring-up
- **Radio Technician** — RF link, ground station hardware and software
- **Researcher** — mission concept, documentation, data analysis, the written/verbal defense

**Deliverables.** Mission concept documentation, a payload prototype, the
integrated CubeSat, ground- and flight-test results, and a project defense
presentation. (The Cosmonautics Project Contest instead wants a summary
form, a ≤14-slide PDF deck, a physical model, and a 7-minute presentation
+ 3-minute Q&A.)

**What isn't published yet.** The organizers explicitly withhold the exact
judging rubric and on-site conduct rules until the first day of finals —
budget review time in your schedule for absorbing last-minute criteria
rather than assuming last year's weighting still applies.

Source: [Orbita tournament overview](https://spaceeducation.info/en/orbita/),
[Regulations PDF](https://spaceeducation.info/wp-content/uploads/2026/08/Regulations-of-the-International-Tournament-Orbita-3.pdf).

## 4. The ground station, explained

"Ground station" here means the equipment and software on the ground that
talks to your satellite during the stratospheric flight — not a
professional S-band tracking dish, but the same concept scaled to an
amateur/educational RF link. Four things it has to do:

**1. Receive telemetry.** Your satellite transmits sensor data,
housekeeping (battery voltage, MCU temperature, uptime) and status
periodically over the radio link. The ground station's radio module
receives these packets; your ground software parses and logs them, and
ideally displays them live so your team can watch the flight in real
time — battery voltage trending down is exactly the kind of thing you
want visible on a live dashboard, not buried in a log file you read after
landing.

**2. Send commands (uplink), if your design includes it.** Not all
educational CubeSats implement a command uplink — many are telemetry-only
to keep the design and the regulatory story simple. If you do add
commands (e.g., "switch payload mode," "request a specific sensor
reading"), you need a defined command packet format, an acknowledgment
scheme, and a plan for what the satellite does if it never hears from the
ground (it should default to a safe autonomous behavior, not wait forever
for an instruction that a dropped link will never deliver).

**3. Maintain the link despite motion.** A stratospheric balloon drifts
with the wind and can end up many kilometers from the launch site,
climbing and later descending fast under parachute. Link margin (see
below) has to hold across that whole geometry change, and your antenna
needs a wide enough beamwidth (or active tracking) to stay pointed at a
moving target — a balloon payload is not a fixed target you can aim at once
and forget.

**4. Record everything, unconditionally.** Whatever else happens, the
ground station should log every received packet, raw and decoded, with a
timestamp, to disk. This is your only record of the flight for the
post-flight analysis the judges want, and it's your best debugging tool
if telemetry gets weird mid-flight.

**Typical hardware building blocks** for a station like this: a radio
module or SDR (software-defined radio) receiver matched in frequency and
protocol to whatever module you put on the satellite (a sub-GHz module
such as a 433 MHz LoRa transceiver is a very common choice for this class
of project, because of its long range at low power and easy
availability — confirm the actual frequency/module against your kit
documentation once it arrives, since the IntroSat kit's exact radio choice
wasn't published on the sources checked for this document); a
directional or omnidirectional antenna appropriate to that band; and
either a dedicated ground-station PCB (interfacing the radio module to a
laptop) or an off-the-shelf USB/serial radio dongle. **Software**: a
serial/USB link into a laptop running your Python receiver script, which
parses packets against your defined format and writes them to a log file
and a live display (even a simple scrolling terminal or CSV-tailing
dashboard is enormously more useful mid-flight than nothing).

**Link budget, in plain terms.** Before you commit to a frequency, module,
and antenna, work out whether the signal will actually be strong enough to
receive at the expected range: transmit power out of the satellite's radio,
minus losses (cable, connector, and — critically — the free-space loss
over the distance to the balloon at altitude), plus your ground antenna's
gain, needs to clear the receiver's sensitivity floor with margin (aim for
at least 10 dB of margin, more if you can get it, since a marginal link
that works on the bench will drop packets the moment the balloon is
20 km away with terrain or a marginal antenna angle in between). This is
one calculation worth doing on paper (or in a spreadsheet in
`ground-station/rf-design/`) before you solder anything — it decides
whether "20 km at altitude" is even achievable with your chosen module and
antenna, and it's a very natural thing for the Radio Technician role to
own and later present in the defense.

## 5. KiCad workflow — best practices for this project

You're building at least two related KiCad projects (`satellite-pcb` and
optionally `ground-station-pcb`), on a team, under a hard deadline, for a
board that has to survive a real flight. A few habits pay for themselves:

**Structure the schematic hierarchically.** One top sheet with
sub-sheets for Power, OBC, Communications, and Payload Interface, rather
than one flat schematic. It matches how the team's roles divide the work
(Electrical Engineer on Power/OBC, Radio Technician reviewing
Communications) and makes the board much easier to review with mentors.

**Use net classes and design rules that match reality**, not KiCad's
defaults: minimum trace width and clearance your fab house can actually
achieve, and a separate (wider) net class for battery/power traces. Set
these once in the project and let the DRC (Design Rule Check) enforce
them, rather than eyeballing trace widths.

**Keep the board profile locked to the IntroSat 3U mounting pattern
from day one.** Get the mechanical outline and mounting hole positions
from the kit documentation (or measure the physical kit once it arrives)
and set them as the PCB edge-cuts layer before you start placing
components, not after — that's the single most common cause of "the board
doesn't fit" late in a schedule like this one.

**Version control the KiCad project as text**, which modern KiCad (7/8)
supports natively — `.kicad_sch`, `.kicad_pcb`, and `.kicad_pro` are all
plain text and diff reasonably well in git. Commit after every meaningful
schematic or layout change, with a message that says what changed
electrically (not just "wip"). The `.gitignore` already in this folder
excludes KiCad's backup and autosave files so they don't clutter history.

**Run ERC and DRC before every "this is a checkpoint" moment** —
before ordering fab, before asking a mentor to review, before a team
demo. Zero warnings you can't explain is the bar, not zero errors.

**Design for the flight environment, not just the bench.** At -50 to
-60°C, some components (electrolytic capacitors especially, some battery
chemistries) behave badly or fall outside their rated range — check
datasheet operating temperature ranges when selecting parts, not just
their typical/room-temperature specs. Secure connectors mechanically
(friction alone isn't enough under launch/landing shock) and consider
strain relief on any wire leaving the board.

**Order fab and assembly with real margin.** Panelize your first fab run
if budget allows, so a soldering mistake or ESD failure on one board
doesn't become a schedule crisis. Standard fab houses commonly run
1–2 weeks; build that into `project-management/timeline.md` working
backward from the 10–20 September kit-arrival window (2026 season) or
your own season's finals date.

**Keep a shared parts library from the start** (`hardware/shared-libraries/`)
rather than letting `satellite-pcb` and `ground-station-pcb` each
accumulate their own copies of the same connector footprint — footprint
drift between two "identical" custom symbols is a very avoidable source
of a board that doesn't fit its connector.

## 6. Task / project ideas, by role

**For the Electrical Engineer / PCB design:**
- Design the power subsystem: battery protection (over-discharge, over-current), a regulator sized for worst-case peak current (radio TX draws far more than idle), and a simple power budget spreadsheet (mAh needed vs. mAh available across expected flight duration).
- Bring up the STM32 OBC on a breadboard/dev board first — validate your firmware architecture before committing it to a custom PCB you can't easily rework mid-competition.
- Build a test harness board (or just test points) so the team can check power rails and MCU status without a full disassembly.
- Do a thermal survival review of the BOM: flag every part whose datasheet operating range doesn't comfortably cover -60°C to the expected max internal temperature.

**For the Radio Technician / ground station:**
- Work out the link budget (section 4) before finalizing frequency and antenna choice.
- Build and bench-test the ground station receiver chain against a satellite-side radio on the actual chosen frequency, at increasing simulated distance/attenuation, to find your real-world range — don't trust the module's marketing-spec range number.
- Define the packet format (a simple, robust framing with a checksum/CRC) and write both the satellite-side encoder and ground-side decoder from the same shared spec so they can't drift apart.
- Build a live telemetry dashboard (even a terminal-based one) that highlights out-of-range values (battery voltage, temperature) rather than a wall of raw numbers.
- Plan and rehearse the physical ground-station setup: antenna assembly time, laptop battery life, what happens if the balloon drifts further than expected.

**For the Design Engineer / mechanical:**
- CAD the payload's mechanical interface to the 3U structure early, in parallel with PCB design, so electrical and mechanical don't discover a conflict during final integration.
- Design for tool-less or minimal-tool assembly/disassembly, since you'll likely open the satellite multiple times for testing and last-minute fixes.
- Prototype in 3D-printed plastic before committing to a final material, and mechanically shock-test any printed bracket before flight (a drop test is a cheap proxy for launch/landing shock).
- Plan cable routing and strain relief inside the structure before the final assembly pass — this is a common last-minute scramble.

**For the Researcher / mission design:**
- Pick a payload experiment with a clearly falsifiable question ("does X measurably change with altitude/temperature") rather than an open-ended demo — that maps directly onto "did the experiment produce a result," which past seasons show is what actually separates standings.
- Draft the mission concept document and success criteria before hardware design finalizes, so the team is building toward an agreed goal.
- Own the post-flight data analysis pipeline (even a simple one) so flight data becomes a defensible result, not just a CSV nobody has time to process before the defense.
- Prepare the defense narrative in parallel with hardware work, not the week before finals — reserve the last week for rehearsal, not first-draft writing.

**Team-wide / shared tasks:**
- A full integration test on the bench that simulates the mission timeline end-to-end (power-on, boot, telemetry stream, payload activation, landing/power-down) before the actual flight.
- A pre-flight checklist (`testing/stratospheric-launch/`) covering battery charge state, antenna connections torqued/seated, SD card or logging storage cleared, structure fasteners checked.
- A risk register (`project-management/risk-register.md`) — kit shipping delay, radio range shorter than hoped, a part going out of stock, a team member unavailable near the deadline — with a mitigation for each.

## 7. Sources

- [International Space Tournament "Orbita" — official overview](https://spaceeducation.info/en/orbita/)
- [Regulations of the International Tournament Orbita (PDF)](https://spaceeducation.info/wp-content/uploads/2026/08/Regulations-of-the-International-Tournament-Orbita-3.pdf)
- [Orbita 2025 finals recap — Space-π](https://spacepi.space/news/final-orbita-2025/)
- [Orbita 2025 season recap — cikeno.ru](https://cikeno.ru/tournament-orbita-2025/)
- [Orbita 2024 finals announcement — Дворец Молодёжи](https://dm-centre.ru/novosti/kvantorium/mezhdunarodnyj-turnir-orbita/)
- [Orbita.Challenge online platform](https://introsat.ru/orbita)
- [IntroSat educational kits catalog](https://introsat.ru/en/space-education-kits-all)
