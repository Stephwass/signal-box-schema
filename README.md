Signal Box is a JSON schema for recording qualitative reasoning and reflection data.
It supports metrics, affective tags, and symbolic glyphs representing cognitive functions.

## Files
- `signal_box_reference.json` — master schema and glyph lexicon
- `examples/example_frame.json` — sample frame
- `signal_box.py` — small helper to create and save frames
- `LICENSE` — MIT license

## Quick usage (Python)
```python
import json
with open("signal_box_reference.json", encoding="utf-8") as f:
    schema = json.load(f)
print(schema["glyph_lexicon"]["⚡"])

## License

This project is licensed under the Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0) License.  
You may use, modify, and share it for **personal or research purposes only**, not for commercial use.

See the [LICENSE](LICENSE) file for details.
