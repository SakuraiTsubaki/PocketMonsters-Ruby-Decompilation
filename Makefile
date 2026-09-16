PYTHON ?= python3
ROM ?= baserom.gba
MGBA ?= $(shell command -v mgba-qt 2>/dev/null || command -v mgba 2>/dev/null || printf '%s' .local/decompilation/bin/mgba)

.PHONY: help inspect-rom verify-rom setup-tools check-tools run-rom debug-rom

help:
	@echo "Pocket Monsters Ruby decompilation"
	@echo ""
	@echo "Targets:"
	@echo "  make setup-tools"
	@echo "  make check-tools"
	@echo "  make inspect-rom ROM=/path/to/local.gba"
	@echo "  make verify-rom ROM=/path/to/local.gba TARGET=<registered-target>"
	@echo "  make run-rom ROM=/path/to/local.gba"
	@echo "  make debug-rom ROM=/path/to/local.gba"
	@echo ""
	@echo "Target metadata is populated only from direct project analysis."
	@echo "Retail ROM images are never committed to this repository."

setup-tools:
	bash tools/setup_decompilation_env.sh

check-tools:
	$(PYTHON) tools/check_decompilation_env.py

inspect-rom:
	$(PYTHON) tools/verify_rom.py "$(ROM)"

verify-rom:
	@test -n "$(TARGET)" || (echo "TARGET is required for verify-rom" && exit 2)
	$(PYTHON) tools/verify_rom.py "$(ROM)" --target "$(TARGET)"

run-rom:
	@test -f "$(ROM)" || (echo "ROM not found: $(ROM)" && exit 2)
	@test -x "$(MGBA)" || command -v "$(MGBA)" >/dev/null 2>&1 || (echo "mGBA not found; run make setup-tools" && exit 2)
	"$(MGBA)" "$(ROM)"

debug-rom:
	@test -f "$(ROM)" || (echo "ROM not found: $(ROM)" && exit 2)
	@test -x "$(MGBA)" || command -v "$(MGBA)" >/dev/null 2>&1 || (echo "mGBA not found; run make setup-tools" && exit 2)
	"$(MGBA)" -d "$(ROM)"
