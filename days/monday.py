"""
Notes:
    ==> Whole week full body every day.
    ==> Posterior leg focused day.
"""

day_data = {
    "warmup": {
        "exercises": [
            {
                "type": {
                    "name": "3 Rounds of",
                },
                "movements": [
                    {
                        "name": "DB glute bridge static hold (I.C.W)",
                        "amount": 30,
                        "si_unit": "sec",
                    },
                    {"name": "Single kb deadlift (I.C.W)", "amount": 10, "si_unit": ""},
                    {
                        "name": "Kneeling db shoulder press (I.C.W)",
                        "amount": 10,
                        "si_unit": "p/s",
                    },
                ],
                "duration": 12,
            },
        ]
    },
    "wod": {
        "exercises": [
            {
                "type": {
                    "name": "For time",
                },
                "duration": 35,
            },
            {
                "type": {
                    "name": "35 min Cap",
                },
            },
            {
                "type": {
                    "name": "",
                    "value": "",
                    "split": {
                        "working_time": 40,
                        "rest_time": 20,
                    },
                },
                "movements": [
                    {"name": "", "amount": 0, "si_unit": ""},
                    {"name": "", "amount": 0, "si_unit": ""},
                    {"name": "", "amount": 0, "si_unit": ""},
                ],
                "duration": 0,
            },
        ]
    },
}
