PYTHON ?= python3
ROM ?= baserom.gba
TARGET ?= ruby_en_rev0

.PHONY: help verify-rom

help:
	@echo "Pocket Monsters Ruby decompilation bootstrap"
	@echo ""
	@echo "Targets:"
	@echo "  make verify-rom ROM=/path/to/local.gba [TARGET=ruby_en_rev0]"
	@echo ""
	@echo "Retail ROM images are never committed to this repository."

verify-rom:
	$(PYTHON) tools/verify_rom.py "$(ROM)" --target "$(TARGET)"
