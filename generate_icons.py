#!/usr/bin/env python3
"""Generate simple PWA icons for VibeGene."""
import struct, zlib, os

def png(size):
    """Create a minimal valid PNG with the VG hex design."""
    w = h = size
    # Background color #0a0f1e, hex accent #4ade80
    bg = (10, 15, 30)
    fg = (74, 222, 128)

    rows = []
    for y in range(h):
        row = [0]  # filter byte
        for x in range(w):
            # Normalize coords to -1..1
            nx = (x / w - 0.5) * 2
            ny = (y / h - 0.5) * 2
            # Draw hexagon border
            q = abs(nx)
            r = abs(ny)
            in_hex = (q * 0.866 + r * 0.5 < 0.82) and (r < 0.82)
            on_border = in_hex and not ((q * 0.866 + r * 0.5 < 0.72) and (r < 0.72))
            # Simple "VG" area — just color the center
            in_center = abs(nx) < 0.35 and abs(ny) < 0.3
            if on_border or in_center:
                row += list(fg)
            else:
                row += list(bg)
        rows.append(bytes(row))

    def chunk(name, data):
        c = zlib.crc32(name + data) & 0xffffffff
        return struct.pack('>I', len(data)) + name + data + struct.pack('>I', c)

    ihdr_data = struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)
    raw = b''.join(rows)
    idat_data = zlib.compress(raw)

    return (
        b'\x89PNG\r\n\x1a\n' +
        chunk(b'IHDR', ihdr_data) +
        chunk(b'IDAT', idat_data) +
        chunk(b'IEND', b'')
    )

os.makedirs('public/icons', exist_ok=True)
for size in [192, 512]:
    with open(f'public/icons/icon-{size}.png', 'wb') as f:
        f.write(png(size))
    print(f'Created public/icons/icon-{size}.png')
