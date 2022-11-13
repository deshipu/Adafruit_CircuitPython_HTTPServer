# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_httpserver.mime_type.MIMEType`
====================================================
* Author(s): Dan Halbert, Michał Pokusa
"""

class MIMEType:
    """Common MIME types.
    From https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
    """

    AAC = "audio/aac"
    ABW = "application/x-abiword"
    ARC = "application/x-freearc"
    AVI = "video/x-msvideo"
    AZW = "application/vnd.amazon.ebook"
    BIN = "application/octet-stream"
    BMP = "image/bmp"
    BZ = "application/x-bzip"
    BZ2 = "application/x-bzip2"
    CSH = "application/x-csh"
    CSS = "text/css"
    CSV = "text/csv"
    DOC = "application/msword"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    EOT = "application/vnd.ms-fontobject"
    EPUB = "application/epub+zip"
    GZ = "application/gzip"
    GIF = "image/gif"
    HTML = "text/html"
    HTM = "text/html"
    ICO = "image/vnd.microsoft.icon"
    ICS = "text/calendar"
    JAR = "application/java-archive"
    JPEG = "image/jpeg"
    JPG = "image/jpeg"
    JS = "text/javascript"
    JSON = "application/json"
    JSONLD = "application/ld+json"
    MID = "audio/midi"
    MIDI = "audio/midi"
    MJS = "text/javascript"
    MP3 = "audio/mpeg"
    CDA = "application/x-cdf"
    MP4 = "video/mp4"
    MPEG = "video/mpeg"
    MPKG = "application/vnd.apple.installer+xml"
    ODP = "application/vnd.oasis.opendocument.presentation"
    ODS = "application/vnd.oasis.opendocument.spreadsheet"
    ODT = "application/vnd.oasis.opendocument.text"
    OGA = "audio/ogg"
    OGV = "video/ogg"
    OGX = "application/ogg"
    OPUS = "audio/opus"
    OTF = "font/otf"
    PNG = "image/png"
    PDF = "application/pdf"
    PHP = "application/x-httpd-php"
    PPT = "application/vnd.ms-powerpoint"
    PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    RAR = "application/vnd.rar"
    RTF = "application/rtf"
    SH = "application/x-sh"
    SVG = "image/svg+xml"
    SWF = "application/x-shockwave-flash"
    TAR = "application/x-tar"
    TIFF = "image/tiff"
    TIF = "image/tiff"
    TS = "video/mp2t"
    TTF = "font/ttf"
    TXT = "text/plain"
    VSD = "application/vnd.visio"
    WAV = "audio/wav"
    WEBA = "audio/webm"
    WEBM = "video/webm"
    WEBP = "image/webp"
    WOFF = "font/woff"
    WOFF2 = "font/woff2"
    XHTML = "application/xhtml+xml"
    XLS = "application/vnd.ms-excel"
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    XML = "application/xml"
    XUL = "application/vnd.mozilla.xul+xml"
    ZIP = "application/zip"
    _7Z = "application/x-7z-compressed"

    @staticmethod
    def from_file_name(filename: str):
        """Return the mime type for the given filename. If not known, return "text/plain"."""
        attr_name = filename.split(".")[-1].upper()

        if attr_name[0].isdigit():
            attr_name = "_" + attr_name

        return getattr(MIMEType, attr_name, MIMEType.TXT)
