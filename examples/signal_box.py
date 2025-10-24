"""
signal_box.py – helper functions for the Signal Box reflection schema
"""

import json
from datetime import datetime

def new_frame(input_text, output_text, glyphs, metrics, affective_tags):
    """Create a new Signal Box reflection frame."""
    return {
        "schema_version": "1.0",
        "session_id": "auto",
        "timestamp": datetime.utcnow().isoformat(),
        "input_text": input_text,
        "output_text": output_text,
        "metrics": metrics,
        "affective_tags": affective_tags,
        "glyph_sequence": glyphs,
        "resonance_flag": max(affective_tags.get("resonance", 0), 0.5) > 0.8
    }

def save_frame(frame, path="frame.json"):
    """Save a reflection frame as a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(frame, f, indent=2, ensure_ascii=False)

def load_frame(path):
    """Load a reflection frame from disk."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
