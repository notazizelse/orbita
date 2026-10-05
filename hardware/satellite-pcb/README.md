# Satellite PCB — KiCad Project

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
