"""
consts.py

Contains configuration settings which should not need to be changed.
These values cannot be modified with a configuration json.

If any of these settings do need to be changed, the change will
probably need to be made permanent, by changing this file.

CONSTANTS:
    IMAGE_TYPES: A tuple of known supported image types

    SOUND_TYPES: A tuple of known supported sound types

    BLANK_SVG_HASHES: A tuple of md5exts which are blanks svg images.
        Some svg converters (cairosvg) don't work with these svgs, so
        the FALLBACK_IMAGE is used rather than attempting conversion.

    FALLBACK_IMAGE: The binary data of a blank png image.
"""

IMAGE_TYPES = ('png', 'svg', 'jpg', 'jpeg', 'bmp')
SOUND_TYPES = ('wav', 'mp3')

BLANK_SVG_HASHES = (
    '3339a2953a3bf62bb80e54ff575dbced.svg',

    # TODO Verify these are actually blank (pokemon4.sb3)
    '14e46ec3e2ba471c2adfe8f119052307.svg',
    '09f60d713153e3d836152b1db500afd1.svg',
    '5adf038af4cd6319154b5601237092fa.svg',
    '9af27a7ad39ec41b7cbfda3622d08a1a.svg'
)
FALLBACK_IMAGE = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
    b"\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\x0bIDAT\x18Wc`\x00"
    b"\x02\x00\x00\x05\x00\x01\xaa\xd5\xc8Q\x00\x00\x00\x00IEND\xaeB`\x82"
)
