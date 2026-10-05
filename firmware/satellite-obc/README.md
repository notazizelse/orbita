# Satellite Flight Software (STM32)

Onboard computer firmware. STM32 + Arduino IDE is the path of least
resistance for the competition; STM32CubeIDE/PlatformIO with HAL/LL
gives you more control (interrupts, low-power modes, DMA) if you have
time to invest. Structure suggestion:

- `src/` — application code
- `lib/` — drivers for sensors/radio not provided by the framework
- `test/` — unit tests / hardware-in-the-loop test scripts
- `platformio.ini` or `.ioc` (CubeMX project file) at this folder's root
