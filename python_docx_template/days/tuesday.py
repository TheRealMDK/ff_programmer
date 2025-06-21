"""
Notes:
    ==> Whole week full body every day.
    ==> Anterior Push focused day (chest).
"""

day_data = {
    "warmup": {
        "exercises": [
            {
                "type": {
                    "name": "Tabata",
                },
                "movements": [
                    {
                        "name": "Airbike",
                    },
                    {
                        "name": "Battle rope",
                    },
                ],
                "duration": 5,
            },
            {
                "type": {
                    "name": "Tabata",
                },
                "movements": [
                    {
                        "name": "Floor plate press",
                    },
                    {
                        "name": "KB Farmer carry static march",
                    },
                ],
                "duration": 5,
            },
        ]
    },
    "wod": {
        "exercises": [
            {
                "type": {
                    "name": "AMRAP",
                    "value": "35min",
                },
                "movements": [
                    {
                        "name": "Airbike",
                        "amount": 20,
                        "si_unit": "cal",
                    },
                    {
                        "name": "Sandbag/Slamball carry",
                        "amount": 40,
                        "si_unit": "m",
                    },
                    {
                        "name": "DB Chest press",
                        "amount": 20,
                        "si_unit": "p/s",
                    },
                    {
                        "name": "Battle rope",
                        "amount": 40,
                    },
                    {
                        "name": "Abmat crunches",
                        "amount": 20,
                    },
                ],
                "duration": 35,
            },
        ]
    },
}
