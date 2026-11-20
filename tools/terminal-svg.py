#!/usr/bin/env python3
"""Convierte un archivo de texto en una imagen SVG con aspecto de terminal.

Uso:
    python3 tools/terminal-svg.py docs/terminal/lsblk.txt docs/img/terminal/lsblk.svg

Formato del archivo de texto:
    title: Texto de la barra de la ventana     (primera línea, opcional)
    $ comando                                  línea de comando (dibuja el prompt)
    texto normal                               salida del comando
    ! texto                                    línea resaltada en verde (dato bueno / el que buscas)
    ? texto                                    línea resaltada en amarillo (dato para vigilar)
    texto || comentario                        añade un comentario a la derecha
"""
import sys
from html import escape

FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'DejaVu Sans Mono', 'Liberation Mono', monospace"
SIZE = 14          # tamaño de letra
CHAR_W = SIZE * 0.6
LINE_H = 21
PAD_X, PAD_TOP, PAD_BOTTOM, BAR_H = 18, 16, 16, 34

C = {
    "bg": "#1e1e2e", "bar": "#181825", "text": "#cdd6f4", "dim": "#7f849c",
    "prompt": "#a6e3a1", "path": "#89b4fa", "cmd": "#f5e0dc",
    "comment": "#f9e2af", "ok_bg": "#a6e3a1", "warn_bg": "#f9e2af",
}
PROMPT_USER = "fedora"
PROMPT_PATH = "~"


def parse(lines):
    title, rows = "terminal", []
    for raw in lines:
        line = raw.rstrip("\n")
        if line.startswith("title:") and not rows:
            title = line[6:].strip()
            continue
        kind = "out"
        if line.startswith("$ "):
            kind, line = "cmd", line[2:]
        elif line.startswith("! "):
            kind, line = "ok", line[2:]
        elif line.startswith("? "):
            kind, line = "warn", line[2:]
        text, _, comment = line.partition(" || ")
        rows.append((kind, text, comment.strip()))
    return title, rows


def render(title, rows):
    prompt_len = len(f"{PROMPT_USER} {PROMPT_PATH} ❯ ")
    text_cols = max(len(t) + (prompt_len if k == "cmd" else 0) for k, t, _ in rows)
    comment_cols = max((len(c) for _, _, c in rows if c), default=0)
    cols = text_cols + (comment_cols + 4 if comment_cols else 0)
    width = int(PAD_X * 2 + cols * CHAR_W)
    height = BAR_H + PAD_TOP + len(rows) * LINE_H + PAD_BOTTOM
    comment_x = PAD_X + (text_cols + 3) * CHAR_W

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="{width}" height="{height}" rx="10" fill="{C["bg"]}"/>',
        f'<path d="M0 10a10 10 0 0 1 10-10h{width-20}a10 10 0 0 1 10 10v{BAR_H-10}h-{width}z" fill="{C["bar"]}"/>',
    ]
    for i, color in enumerate(("#f38ba8", "#f9e2af", "#a6e3a1")):
        out.append(f'<circle cx="{20 + i*20}" cy="{BAR_H/2}" r="6" fill="{color}"/>')
    out.append(f'<text x="{width/2}" y="{BAR_H/2 + 5}" fill="{C["dim"]}" font-family="{FONT}" font-size="13" text-anchor="middle">{escape(title)}</text>')

    y = BAR_H + PAD_TOP
    for kind, text, comment in rows:
        base = y + LINE_H * 0.72
        if kind in ("ok", "warn"):
            fill = C["ok_bg"] if kind == "ok" else C["warn_bg"]
            out.append(f'<rect x="{PAD_X-6}" y="{y}" width="{text_cols*CHAR_W+12}" height="{LINE_H}" rx="3" fill="{fill}" fill-opacity="0.16"/>')
            out.append(f'<rect x="{PAD_X-6}" y="{y}" width="3" height="{LINE_H}" fill="{fill}"/>')
        t = f'<text x="{PAD_X}" y="{base}" font-family="{FONT}" font-size="{SIZE}" xml:space="preserve">'
        if kind == "cmd":
            t += (f'<tspan fill="{C["prompt"]}">{PROMPT_USER}</tspan><tspan fill="{C["path"]}"> {PROMPT_PATH}</tspan>'
                  f'<tspan fill="{C["prompt"]}"> ❯ </tspan><tspan fill="{C["cmd"]}">{escape(text)}</tspan>')
        else:
            t += f'<tspan fill="{C["text"]}">{escape(text)}</tspan>'
        out.append(t + "</text>")
        if comment:
            out.append(f'<text x="{comment_x}" y="{base}" fill="{C["comment"]}" font-family="{FONT}" font-size="{SIZE}" xml:space="preserve">← {escape(comment)}</text>')
        y += LINE_H
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        svg = render(*parse(f))
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(svg + "\n")
    print(f"Creado {sys.argv[2]}")
