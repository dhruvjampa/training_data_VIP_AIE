#Converts lecture_notes into structured JSON format (stored in lecture_notes_json)

import fitz
import json
from pathlib import Path


def extract_title_and_content(text):
    """
    Splits slide text so that:
    - First line = title
    - Remaining lines = content
    """
    lines = text.split("\n")

    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    if not lines:
        return "", ""

    title = lines[0]
    content = "\n".join(lines[1:]) if len(lines) > 1 else ""

    return title, content


def pdf_to_structured_json(pdf_path, output_json_path, course_name="ECE 20875"):
    """
    Convert a single PDF into structured lecture JSON format.
    """
    doc = fitz.open(pdf_path)

    slides = []

    lecture_title = pdf_path.stem  # Default lecture title = file name

    for slide_index, slide in enumerate(doc):

        raw_text = slide.get_text().strip()
        title, content = extract_title_and_content(raw_text)

        slide_data = {
            "slide_number": slide_index + 1,
            "title": title,
            "content": content
        }

        slides.append(slide_data)

    output_data = {
        "document_type": "lecture_slides",
        "course": course_name,
        "lecture_title": lecture_title,
        "source_file": pdf_path.name,
        "slides": slides
    }

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)

    print(f"Saved: {output_json_path}")


def process_folder(input_folder, output_folder):
    """
    Process every PDF in input_folder.
    Create a structured JSON file for each PDF.
    Save all outputs into output_folder.
    """

    input_path = Path(input_folder)
    output_path = Path(output_folder)

    output_path.mkdir(exist_ok=True)

    for pdf_file in input_path.glob("*.pdf"):

        output_file = output_path / f"{pdf_file.stem}.json"

        pdf_to_structured_json(pdf_file, output_file)


# ---- Run Script ----
if __name__ == "__main__":

    process_folder(
        input_folder= Path("inputs") / "lecture_notes",
        output_folder= Path("outputs") / "lecture_notes_json"
    )