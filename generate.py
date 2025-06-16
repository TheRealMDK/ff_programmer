import argparse
from docxtpl import DocxTemplate
from context_data import context_data
from export import export_to_json, export_to_yaml, export_to_excel

# Set up argument parser
parser = argparse.ArgumentParser(
    description="Generate weekly workout plan and optionally export it."
)
parser.add_argument(
    "-e",
    "--export",
    choices=["json", "yaml", "excel"],
    help="Export context to the specified format",
)

parser.add_argument(
    "-o",
    "--output",
    type=str,
    help="Specify output file name (without extension)",
)

args = parser.parse_args()

# Load your Word template
doc = DocxTemplate("template.docx")

# Define your data
context = context_data

for day in context:
    warmup_total = sum(
        e.get("duration", 0) for e in context[day]["warmup"]["exercises"]
    )
    context[day]["warmup"]["total_duration"] = warmup_total

    wod_total = sum(e.get("duration", 0) for e in context[day]["wod"]["exercises"])
    context[day]["wod"]["total_duration"] = wod_total


# Render the document with data
doc.render(context)

# Save the result
if args.output:
    outputFileName = f"{input('provide output file name without extension:\n-> ')}.docx"
else:
    outputFileName = "wip.docx"

doc.save(outputFileName)

# Export if flag is provided
if args.export == "json":
    export_to_json(context)
elif args.export == "yaml":
    export_to_yaml(context)
elif args.export == "excel":
    export_to_excel(context)
