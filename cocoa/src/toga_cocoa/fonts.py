from pathlib import Path

from toga.fonts import (
    _REGISTERED_FONT_CACHE,
    BOLD,
    CURSIVE,
    FANTASY,
    ITALIC,
    MESSAGE,
    MONOSPACE,
    NORMAL,
    OBLIQUE,
    SANS_SERIF,
    SERIF,
    SMALL_CAPS,
    SYSTEM,
    SYSTEM_DEFAULT_FONT_SIZE,
    SYSTEM_DEFAULT_FONTS,
)
from toga_cocoa.libs import (
    NSURL,
    NSFont,
    NSFontManager,
    NSFontMask,
)
from toga_cocoa.libs.core_text import core_text, kCTFontManagerScopeProcess

_FONT_CACHE = {}
_POSTSCRIPT_NAMES = {
    SERIF: "Times-Roman",
    SANS_SERIF: "Helvetica",
    CURSIVE: "Apple Chancery",
    FANTASY: "Papyrus",
    MONOSPACE: "Courier New",
}


class Font:
    def __init__(self, interface):
        self.interface = interface
        try:
            font = _FONT_CACHE[self.interface]
        except KeyError:
            font = None
            family = self.interface.family
            font_key = self.interface._registered_font_key(
                family,
                weight=self.interface.weight,
                style=self.interface.style,
                variant=self.interface.variant,
            )

            # Font isn't a built-in system font, has been registered, but hasn't
            # been loaded previously.
            # FIXME this doesn't handle when there are multiple fonts in a file,
            # or multiple font registrations for a single file.
            if (
                self.interface.family not in SYSTEM_DEFAULT_FONTS
                and font_key in _REGISTERED_FONT_CACHE
                and self.interface.family not in _POSTSCRIPT_NAMES
            ):
                font_path = _REGISTERED_FONT_CACHE[font_key]
                if Path(font_path).is_file():
                    font_url = NSURL.fileURLWithPath(font_path)
                    success = core_text.CTFontManagerRegisterFontsForURL(
                        font_url, kCTFontManagerScopeProcess, None
                    )
                    if success:
                        # FIXME - this naming needs to be dynamically determined from the font,
                        # rather than hard-coded
                        _POSTSCRIPT_NAMES[self.interface.family] = {
                            "awesome-free-solid": "Font Awesome 5 Free",
                            "Endor": "ENDOR",
                        }.get(self.interface.family, self.interface.family)
                    else:
                        print(f"Font '{self.interface}' could not be loaded")
                else:
                    raise ValueError(f"Font file {font_path} could not be found")

            if self.interface.size == SYSTEM_DEFAULT_FONT_SIZE:
                font_size = NSFont.systemFontSize
            else:
                # A "point" in Apple APIs is equivalent to a CSS pixel, but the Toga
                # public API works in CSS points, which are slightly larger
                # (https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Explained/Explained.html).
                font_size = self.interface.size * 96 / 72

            # Construct the NSFont
            if self.interface.family == SYSTEM:
                font = NSFont.systemFontOfSize(font_size)
            elif family == MESSAGE:
                font = NSFont.messageFontOfSize(font_size)
            else:
                try:
                    font = NSFont.fontWithName(
                        _POSTSCRIPT_NAMES[family], size=font_size
                    )
                except KeyError:
                    print(
                        f"Unknown font '{self.interface}'; "
                        "using system font as a fallback"
                    )
                    font = NSFont.systemFontOfSize(font_size)

            # Convert the base font definition into a font with all the desired traits.
            attributes_mask = 0
            if self.interface.weight == BOLD:
                attributes_mask |= NSFontMask.Bold.value
            if self.interface.style in {ITALIC, OBLIQUE}:
                # Oblique is the fallback for Italic.
                attributes_mask |= NSFontMask.Italic.value
            if self.interface.variant == SMALL_CAPS:
                attributes_mask |= NSFontMask.SmallCaps.value

            if attributes_mask:
                attributed_font = NSFontManager.sharedFontManager.convertFont(
                    font, toHaveTrait=attributes_mask
                )
                # print(font, attributed_font)
            else:
                attributed_font = font

            full_name = "{family}{weight}{style}".format(
                family=family,
                weight=(" " + self.interface.weight.title())
                if self.interface.weight is not NORMAL
                else "",
                style=(" " + self.interface.style.title())
                if self.interface.style is not NORMAL
                else "",
            )

            if attributed_font is None:
                print(
                    "Unable to load font: {}pt {}".format(
                        self.interface.size, full_name
                    )
                )
            else:
                font = attributed_font

            _FONT_CACHE[self.interface] = font.retain()

        self.native = font
