# 🛠️ Seeed XIAO 3x3 Macropad Firmware

A streamlined, high-performance **3x3 (9-key) diodeless macropad** powered by Python using the KMK Firmware ecosystem. Every mechanical switch wires directly back to an individual GPIO pin on the Seeed Studio XIAO—completely eliminating the need for multiplexing diodes and complex matrix math.

---

## 🔌 Hardware Wiring Guide

Each mechanical switch has two metal pins on the bottom. Wire them according to the rules below:

### 1. The Ground Daisy-Chain (GND)

Connect one leg of **all 9 switches** together in a single, continuous wire loop. Solder the end of this shared loop directly to any pin labeled **GND** on your Seeed XIAO.

### 2. Isolated Signal Lines

Solder the second, independent leg of each switch straight back to its dedicated GPIO terminal pin on the board:

| Physical Row   | Left Switch (`Col 0`) | Center Switch (`Col 1`) | Right Switch (`Col 2`) |
| :------------- | :-------------------: | :---------------------: | :--------------------: |
| **Top Row**    |         `D0`          |          `D1`           |          `D2`          |
| **Middle Row** |         `D3`          |          `D4`           |          `D5`          |
| **Bottom Row** |         `D6`          |          `D7`           |          `D8`          |

---

## 🗂️ Drive File Structure

Before deploying, make sure your project files are organized exactly like this. The `kmk` directory and core configuration scripts must sit flat on the absolute root level:

```text
CIRCUITPY (Your Drive Root)/
├── 📁 kmk/           <-- Core KMK software framework
├── 📄 boot.py         <-- Custom USB behavior and
├── 📄 code.py         <-- Diodeless pin scanner logic
├── 📄 keymap.py       <-- Active 9-key shortcut map
└── 📄 README.md       <-- This documentation file
```

---

## 🚀 Software Installation Setup

Follow these quick sequential steps to flash and launch your new firmware workspace:

### Step 1: Install CircuitPython

1. Hold down the physical **`BOOT`** / **`BOOTSEL`** button on your Seeed XIAO board.

2. Plug the board into your computer using a **USB-C data cable**.
3. An external flash drive will appear on your desktop named `RPI-RP2` or `XIAO-BOOT`.
4. Go to [circuitpython.org/downloads](https://circuitpython.org) and download the correct `.uf2` file for your exact XIAO board variant.
5. Drag and drop that `.uf2` file onto the boot drive. The board will automatically reboot and mount as a permanent flash drive named **`CIRCUITPY`**.

### Step 2: Deploy Your Firmware

1. Open your new **`CIRCUITPY`** drive folder.

2. Select **everything inside** your local `Firmware` folder (`kmk`, `boot.py`, `code.py`, `keymap.py`).
3. Drag and drop them straight into the **`CIRCUITPY`** drive root directory.
4. Safely eject the drive from your operating system, unplug the physical USB cable for 3 seconds, and plug it back in to initialize the fresh macros!

---

## ⌨️ Active Layout Blueprint

Your 9 keys operate in this exact grid layout, optimized natively for Windows/Linux platforms:

| Left Column                     | Center Column                    | Right Column                   |
| :------------------------------ | :------------------------------- | :----------------------------- |
| **📑 Copy**<br>`Pin D0`         | **📋 Paste**<br>`Pin D1`         | **📊 Calculator**<br>`Pin D2`  |
| **🎵 Play / Pause**<br>`Pin D3` | **⏮️ Prev Track**<br>`Pin D4`    | **🔇 Panic Mute**<br>`Pin D5`  |
| **🛠️ Task Manager**<br>`Pin D6` | **✂️ Snipping Tool**<br>`Pin D7` | **🔒 Lock Screen**<br>`Pin D8` |
