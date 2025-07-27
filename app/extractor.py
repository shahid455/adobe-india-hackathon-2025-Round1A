import fitz  # PyMuPDF
import os
import json
from collections import defaultdict

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    font_stats = defaultdict(list)
    headings = []

    title = ""
    max_font = 0

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text or len(text) < 2:
                        continue
                    size = span["size"]
                    font_stats[size].append(text)

                    if page_num == 1 and size > max_font:
                        max_font = size
                        title = text

                    headings.append({
                        "text": text,
                        "size": size,
                        "bold": span.get("flags", 0) & 2,
                        "page": page_num
                    })

    sizes = sorted(font_stats.keys(), reverse=True)
    h1_size = sizes[0] if len(sizes) > 0 else 0
    h2_size = sizes[1] if len(sizes) > 1 else h1_size
    h3_size = sizes[2] if len(sizes) > 2 else h2_size

    outline = []
    for h in headings:
        if h["size"] == h1_size:
            level = "H1"
        elif h["size"] == h2_size:
            level = "H2"
        elif h["size"] == h3_size:
            level = "H3"
        else:
            continue
        outline.append({
            "level": level,
            "text": h["text"],
            "page": h["page"]
        })

    result = {
        "title": title,
        "outline": outline
    }
    return result
