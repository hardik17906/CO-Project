# RISC-V Assembler and Simulator

A team-built educational assembler and simulator for a subset of 32-bit RISC-V instructions. The assembler translates text instructions into 32-bit machine code; the simulator executes machine-code input and writes register and memory traces.

The repository history credits contributions from [Hardik](https://github.com/hardik17906), [Harsh](https://github.com/Harsh060911), [Deepesh](https://github.com/deepesh336), and [Bhavya](https://github.com/bhvy1). This project is presented as team work.

## Run a small example

Python 3 is the only runtime dependency for the assembler and simulator. From the repository root:

```bash
python Simple_Assembler.py tests/assembly/simpleBin/simple_1.txt assembled.bin
python Simple_simulator.py assembled.bin trace.txt
```

The first command writes binary instructions. The second writes a step-by-step execution trace. Each script expects an input path and an output path.

## Layout

- [`Simple_Assembler.py`](Simple_Assembler.py): instruction parsing and encoding.
- [`Simple_simulator.py`](Simple_simulator.py): instruction execution and trace generation.
- [`tests/`](tests/): assembly cases, expected binaries, and simulator traces.
- [`src/main.py`](src/main.py): provided grading harness. Use `python src/main.py --windows --verbose` on Windows or `python src/main.py --linux --verbose` on Linux to run it.

The implementation follows the course project's supported instruction subset and is not a complete RISC-V toolchain.
