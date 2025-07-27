import os
import json
from app.extractor import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            output_json = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
            print(f"Processing {filename}...")
            result = extract_outline(pdf_path)
            with open(output_json, "w") as f:
                json.dump(result, f, indent=2)
            print(f"Saved: {output_json}")

if __name__ == "__main__":
    main()
