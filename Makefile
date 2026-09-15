PYTHON ?= python3
ROM ?= baserom.gba

.PHONY: help inspect-rom verify-rom

help:
	@echo "Pocket Monsters Ruby decompilation"
	@echo ""
	@echo "Targets:"
	@echo "  make inspect-rom ROM=/path/to/local.gba"
	@echo "  make verify-rom ROM=/path/to/local.gba TARGET=<registered-target>"
	@echo ""
	@echo "Target metadata is populated only from direct project analysis."
	@echo "Retail ROM images are never committed to this repository."

inspect-rom:
	$(PYTHON) tools/verify_rom.py "$(ROM)"

verify-rom:
	@test -n "$(TARGET)" || (echo "TARGET is required for verify-rom" && exit 2)
	$(PYTHON) tools/verify_rom.py "$(ROM)" --target "$(TARGET)"
