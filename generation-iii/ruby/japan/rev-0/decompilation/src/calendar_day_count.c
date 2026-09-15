/* Initial semantic reconstruction from project-supplied Pokemon Ruby ROMs.
 * Canonical target: jp-r0. Names are descriptive placeholders until caller
 * tracing or symbols establish authoritative names. Not compiler-matched yet.
 */
#include <stdbool.h>
#include <stdint.h>

typedef uint8_t u8;
typedef uint16_t u16;

static const uint32_t sDaysInMonth[12] = {
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31,
};

/* Observed at jp-r0 ROM offset 0x00006754. */
static bool IsLeapYearIndex(u8 year)
{
    if ((year & 3) != 0)
        return false;
    if ((year % 100) != 0)
        return true;
    return (year % 400) == 0;
}

/* Observed at jp-r0 ROM offset 0x0000678C. */
u16 CalendarDayCount_JpRev0(u8 year, u8 month, u8 day)
{
    u16 total = 0;
    int y = (int)year - 1;

    /* Older supplied builds: BLE/BGT => y > 0. */
    while (y > 0) {
        total = (u16)(total + 365);
        if (IsLeapYearIndex((u8)y))
            total = (u16)(total + 1);
        y--;
    }

    if (month > 1) {
        unsigned remaining = (unsigned)month - 1;
        const uint32_t *days = sDaysInMonth;
        while (remaining != 0) {
            total = (u16)(total + *days++);
            remaining--;
        }
    }

    if (month > 2 && IsLeapYearIndex(year))
        total = (u16)(total + 1);

    return (u16)(total + day);
}

/* Semantic form of the later BLT/BGE correction. */
u16 CalendarDayCount_FixedBoundary(u8 year, u8 month, u8 day)
{
    u16 total = 0;
    int y = (int)year - 1;

    while (y >= 0) {
        total = (u16)(total + 365);
        if (IsLeapYearIndex((u8)y))
            total = (u16)(total + 1);
        y--;
    }

    if (month > 1) {
        unsigned remaining = (unsigned)month - 1;
        const uint32_t *days = sDaysInMonth;
        while (remaining != 0) {
            total = (u16)(total + *days++);
            remaining--;
        }
    }

    if (month > 2 && IsLeapYearIndex(year))
        total = (u16)(total + 1);

    return (u16)(total + day);
}
