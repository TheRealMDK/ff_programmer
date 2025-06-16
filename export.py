import json
import yaml
import pandas as pd


def export_to_json(context, filename="context.json"):
    with open(filename, "w") as f:
        json.dump(context, f, indent=4)


def export_to_yaml(context, filename="context.yaml"):
    with open(filename, "w") as f:
        yaml.dump(context, f, sort_keys=False)


def export_to_excel(context, filename="workout_schedule.xlsx"):
    rows = []

    for day, data in context.items():
        for phase in ["warmup", "wod"]:
            for ex in data[phase]["exercises"]:
                if ex["type"]["name"]:  # Skip placeholders
                    for movement in ex["movements"]:
                        rows.append(
                            {
                                "Day": day.capitalize(),
                                "Phase": phase,
                                "Type": ex["type"]["name"],
                                "Duration": ex["duration"],
                                "Movement": movement["name"],
                                "Amount": movement["amount"],
                                "Unit": movement["si_unit"],
                                "Split": f"{ex['type']['split']['working_time']}/{ex['type']['split']['rest_time']}",
                            }
                        )

    df = pd.DataFrame(rows)
    df.to_excel(filename, index=False)
