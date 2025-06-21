"""
Notes:
    ==> Whole week full body every day.
    ==> Active rest day i.e. Hyrox.
"""

day_data = {
    "warmup": {
        "exercises": [
            {
                "type": {
                    "name": "EMOM",
                    "value": "9min",
                    "split": {
                        "working_time": "40",
                        "rest_time": "20",
                    },
                },
                "movements": [
                    {
                        "name": "Ski",
                        "amount": 1,
                        "si_unit": "min",
                    },
                    {
                        "name": "Wall balls",
                        "amount": 10,
                    },
                    {
                        "name": "KB swing",
                        "amount": 10,
                    },
                ],
                "duration": 9,
            },
        ]
    },
    "wod": {
        "exercises": [
            {
                "type": {
                    "name": "For time",
                },
                "movements": [
                    {
                        "name": "Run",
                        "amount": 400,
                        "si_unit": "m",
                    },
                    {
                        "name": "Ski",
                        "amount": 750,
                        "si_unit": "m",
                    },
                    {
                        "name": "Wall balls",
                        "amount": 50,
                    },
                    {
                        "name": "Bike erg",
                        "amount": 750,
                        "si_unit": "m",
                    },
                    {
                        "name": "KB swing",
                        "amount": 50,
                    },
                    {
                        "name": "Row",
                        "amount": 750,
                        "si_unit": "m",
                    },
                    {
                        "name": "Run",
                        "amount": 400,
                        "si_unit": "m",
                    },
                ],
                "duration": 36,
            },
            {
                "type": {
                    "name": "",
                    "value": "**35min cap**",
                },
                "duration": 0,
            },
        ]
    },
}
