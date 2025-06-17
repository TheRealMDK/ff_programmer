"""
Notes:
    ==> Whole week full body every day.
    ==> Posterior leg focused day.
    ==> Target shoulders for push.
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
                    {"name": "Single KB deadlift (I.C.W)", "amount": 10, "si_unit": ""},
                    {
                        "name": "Kneeling DB shoulder press (I.C.W)",
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
                    "name": "E12MOM",
                    "value": "34min",
                    "split": {
                        "working_time": "10min",
                        "rest_time": "2min",
                    },
                },
                "duration": 34,
            },
            {
                "type": {
                    "name": "For the first 10 minutes",
                },
                "duration": 0,
            },
            {
                "type": {
                    "name": "AMRAP",
                    "value": "10min",
                },
                "movements": [
                    {
                        "name": "Rocket bag back squats",
                        "amount": 20,
                    },
                    {
                        "name": "Push-ups/Ladies push-ups",
                        "amount": 10,
                    },
                    {
                        "name": "Alt KB high pull",
                        "amount": 20,
                    },
                ],
                "duration": 0,
            },
            {
                "type": {
                    "name": "",
                    "value": "**2min rest**",
                },
                "duration": 0,
            },
            {
                "type": {
                    "name": "For the second 10 minutes",
                },
                "duration": 0,
            },
            {
                "type": {
                    "name": "AMRAP",
                    "value": "10min",
                },
                "movements": [
                    {
                        "name": "Slam ball throws",
                        "amount": 20,
                    },
                    {
                        "name": "ALT DB bicep curls",
                        "amount": 30,
                    },
                    {
                        "name": "Bike erg",
                        "amount": 12,
                        "si_unit": "cals",
                    },
                ],
                "duration": 0,
            },
            {
                "type": {
                    "name": "",
                    "value": "**2min rest**",
                },
                "duration": 0,
            },
            {
                "type": {
                    "name": "For the last 10 minutes",
                },
                "duration": 0,
            },
            {
                "type": {
                    "name": "AMRAP",
                    "value": "10min",
                },
                "movements": [
                    {
                        "name": "Single KB deadlift",
                        "amount": 20,
                    },
                    {
                        "name": "Plate calve raises",
                        "amount": 40,
                    },
                    {
                        "name": "Rolling DB tricep extensions",
                        "amount": 12,
                        "si_unit": "cals",
                    },
                ],
                "duration": 0,
            },
        ]
    },
}
