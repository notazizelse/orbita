# Ground Station Software

Code that talks to the radio module on the ground side: receiving
telemetry, sending commands, logging. Python is a good fit here (the
regulations call out Python specifically for the radio/ground-station
side). Structure suggestion:

- `src/` — telemetry receiver, command sender, decoder
- `protocol/` — packet format definitions shared conceptually with the
  satellite firmware (keep both sides' packet structs in sync!)
- `logs/` — raw telemetry logs from tests and the actual flight (gitignored, see root .gitignore)
