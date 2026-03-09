#Converts homework into structured JSON format (stored in homework_json)

import re
import json
import fitz
from pathlib import Path

def extract_pdf_lines(pdf_path):
    """Extract text from a PDF and return it as a list of lines."""
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text.splitlines()


def parse_lines_to_structure(lines, filename, class_name="UNKNOWN_CLASS"):
    # Extract homework number from filename like HW7_README.md
    match = re.search(r"HW(\d+)", filename)
    homework_number = int(match.group(1)) if match else None

    data = {
        "class": class_name,
        "homework_number": homework_number,
        "sections": {}
    }

    section_stack = []

    for line in lines:
        header_match = re.match(r"(#+)\s+(.*)", line)

        if header_match:
            level = len(header_match.group(1))
            title = header_match.group(2).strip().lower()

            # Move up the hierarchy if necessary
            while section_stack and section_stack[-1][0] >= level:
                section_stack.pop()

            if not section_stack:
                data["sections"][title] = {"content": "", "subsections": {}}
                section_stack.append((level, title))
            else:
                parent = data["sections"]

                # Traverse down hierarchy correctly
                for i, (_, name) in enumerate(section_stack):
                    if i == 0:
                        parent = parent[name]
                    else:
                        parent = parent["subsections"][name]

                parent["subsections"][title] = {"content": "", "subsections": {}}
                section_stack.append((level, title))

        else:
            if section_stack:
                parent = data["sections"]

                for i, (_, name) in enumerate(section_stack):
                    if i == 0:
                        parent = parent[name]
                    else:
                        parent = parent["subsections"][name]

                parent["content"] += line + "\n"

    # Remove empty subsections
    def clean_empty_sections(section):
        if "subsections" in section:
            if not section["subsections"]:
                del section["subsections"]
            else:
                for sub in list(section["subsections"].keys()):
                    clean_empty_sections(section["subsections"][sub])

    for sec in data["sections"].values():
        clean_empty_sections(sec)

    return data


def parse_markdown_file(md_path, class_name):
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return parse_lines_to_structure(lines, md_path.name, class_name)


def parse_pdf_file(pdf_path, class_name):
    lines = extract_pdf_lines(pdf_path)
    return parse_lines_to_structure(lines, pdf_path.name, class_name)


def process_folder(input_folder, output_folder, class_name="ECE 20875"):
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(exist_ok=True)

    for file in input_path.glob("*"):
        if file.suffix.lower() == ".md":
            structured_data = parse_markdown_file(file, class_name)

        elif file.suffix.lower() == ".pdf":
            structured_data = parse_pdf_file(file, class_name)

        else:
            continue

        output_file = output_path / f"{file.stem}.json"

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(structured_data, f, indent=4, ensure_ascii=False)

        print(f"Saved: {output_file}")


# ---- Run Script ----
if __name__ == "__main__":

    folder = Path("homework") / "S20 HW READMEs"

    process_folder(
        input_folder= Path ("inputs") / folder,
        output_folder= Path("outputs") / "homework_json",
        class_name="ECE 20875"
    )