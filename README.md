# 🧠 Adobe India Hackathon 2025 – Round 1A: PDF Outline Extractor

## 📝 Overview

This repository contains my solution for **Round 1A** of the Adobe India Hackathon 2025. The challenge involves building a PDF processing system that extracts structured text data and generates corresponding JSON outputs. The implementation is fully containerized with Docker and meets all the technical constraints defined in the challenge.

---

## 📂 Project Structure
```
📁 adobe_challenge
├── 📁 input # Folder containing input PDF files
├── 📁 output # Folder where extracted JSON files will be saved
├── 📄 Dockerfile # Dockerfile to build the containerized environment
├── 📄 main.py # Main script that processes all PDF files in the input folder
├── 📄 outline_extractor.py# Helper module to extract outlines and text
```
### Build Command
```bash
docker build --platform linux/amd64 -t <reponame.someidentifier> .
```

### Run Command
```bash
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output/repoidentifier/:/app/output --network none <reponame.someidentifier>
```

### Critical Constraints
- **Execution Time**: ≤ 10 seconds for a 50-page PDF
- **Model Size**: ≤ 200MB (if using ML models)
- **Network**: No internet access allowed during runtime execution
- **Runtime**: Must run on CPU (amd64) with 8 CPUs and 16 GB RAM
- **Architecture**: Must work on AMD64, not ARM-specific

### Key Requirements
- **Automatic Processing**: Process all PDFs from `/app/input` directory
- **Output Format**: Generate `filename.json` for each `filename.pdf`
- **Input Directory**: Read-only access only
- **Open Source**: All libraries, models, and tools must be open source
- **Cross-Platform**: Test on both simple and complex PDFs


## Implementation

---

## 🧠 Solution Highlights

- Automatically processes all PDFs placed in `/app/input`
- Extracts headings and font structure from PDFs
- Generates a clean, structured JSON for each file
- Respects read-only access to input, and produces output into mounted `/app/output`

---

## 🚀 Getting Started

> Make sure you have Docker installed and running on your system.

### 🔧 Build the Docker Image

```bash
docker build --platform linux/amd64 -t adobe_outline_extractor:round1a .
```
### Processing Script
```
def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process all PDF files in input directory
    for pdf_file in input_dir.glob("*.pdf"):
        print(f"Processing {pdf_file.name}...")
        
        # Extract structured data using helper
        result = extract_outline(pdf_file)

        # Save JSON output with the same base name
        output_file = output_dir / f"{pdf_file.stem}.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2)
        
        print(f"Saved: {output_file}")
```
### Sample Docker Configuration
```dockerfile
docker run --rm ^
  -v "${PWD}\input:/app/input" ^
  -v "${PWD}\output:/app/output" ^
  --network none ^
  adobe_outline_extractor:round1a
```

## Output Format

### Required JSON Structure
Each PDF is analyzed for font size and hierarchy, and the resulting structure includes:
```
[
  {
    "text": "Section Heading",
    "size": 16.0,
    "bold": true,
    "font": "Times-Roman"
  },
  ...
]
```


## Implementation Guidelines

### Performance Considerations
- **Memory Management**: Efficient handling of large PDFs
- **Processing Speed**: Optimize for sub-10-second execution
- **Resource Usage**: Stay within 16GB RAM constraint
- **CPU Utilization**: Efficient use of 8 CPU cores

### 🧪 Testing Strategy
I tested the solution using:
- 📄 Simple 1–2 page PDFs
- 📑 Larger documents with 50+ pages
- 🧾 PDFs with multi-column, table-based layouts

## Testing Solution

### Local Testing
```bash
# Build the Docker image
docker build --platform linux/amd64 -t adobe_outline_extractor:round1a .

# Test with sample data
docker run --platform linux/amd64 -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output adobe_outline_extractor:round1a
```

### Validation Checklist
- ✅ All PDFs in input directory are processed
- ✅ JSON output files are generated for each PDF
- ✅ Output format matches required structure
- ✅ **Output conforms to schema** in `sample_dataset/schema/output_schema.json`
- ✅ Processing completes within 10 seconds for 50-page PDFs
- ✅ Solution works without internet access
- ✅ Memory usage stays within 16GB limit
- ✅ Compatible with AMD64 architecture

---
### 🧰 Dependencies
See requirements.txt:
```bash
PyMuPDF==1.22.3
```
Install manually (if not using Docker):
```bash
pip install -r requirements.txt
```
### 🧑‍💻 Author
- Shahidul Hasan
- Deepta Chakravarty
