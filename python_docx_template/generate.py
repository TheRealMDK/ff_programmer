from docxtpl import DocxTemplate, RichText
from context_data import context_data


def render_exercise_block(exercise):
    lines = []

    # Header
    type_info = exercise.get("type", {})
    header_parts = []

    if type_info.get("value"):
        header_parts.append(type_info["value"])
    if type_info.get("name"):
        header_parts.append(type_info["name"])

    split = type_info.get("split", {})
    if split.get("working_time") or split.get("rest_time"):
        split_str = f"({split.get('working_time', '')}"
        if split.get("rest_time"):
            split_str += f"/{split.get('rest_time')}"
        split_str += ")"
        header_parts.append(split_str)

    if header_parts:
        header = RichText(" ".join(header_parts) + ":\n", bold=True)
        lines.append(header)

    # Movements
    for movement in exercise.get("movements", []):
        if movement.get("name"):
            move_str = f" -> {movement['name']}"
            if movement.get("amount"):
                move_str += f" x{movement['amount']}"
            if movement.get("si_unit"):
                move_str += f"{movement['si_unit']}"
            lines.append(RichText(move_str + "\n"))

            # Apply italics to the amount
            movement_line = RichText(move_str + "\n")

            movement_line.italic = True
    return lines


def preprocess_context(context):
    for day_name, day in context.items():
        day["day_name"] = day_name

        warmup_total = sum(e.get("duration", 0) for e in day["warmup"]["exercises"])
        wod_total = sum(e.get("duration", 0) for e in day["wod"]["exercises"])
        day["warmup"]["total_duration"] = warmup_total
        day["wod"]["total_duration"] = wod_total
        day["total_duration"] = warmup_total + wod_total

        day["warmup"]["rendered_lines"] = []
        for ex in day["warmup"]["exercises"]:
            day["warmup"]["rendered_lines"].extend(render_exercise_block(ex))

        day["wod"]["rendered_lines"] = []
        for ex in day["wod"]["exercises"]:
            day["wod"]["rendered_lines"].extend(render_exercise_block(ex))


# Main execution
doc = DocxTemplate("template.docx")
context = context_data
preprocess_context(context)
doc.render(context)
doc.save("output.docx")
