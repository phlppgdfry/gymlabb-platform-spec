from demo.contracts import number, text, record, metric


CONFIG = {
    "columns": [
        ["name", "Client"],
        ["status", "Attention"],
        ["value", "Weekly sessions"],
        ["context", "Program"],
    ],
    "title": "GymLabb",
    "heading": "Good coaching starts with attention.",
    "subtitle": "See who needs support, review weekly check-ins, and record the training that moves each client forward.",
    "section": "Coach workspace",
    "list_title": "Your coaching roster",
    "theme": "gym",
    "port": 8113,
    "clock": "Training week · 15–21 June 2026",
}


ACTIONS = frozenset(["workout", "checkin", "review"])


def seed():
    return [
        dict(
            id=str(i + 1),
            name=name,
            program=program,
            inactive=inactive,
            planned=3,
            workouts=[],
            checkin=None,
            reviewed=False,
        )
        for i, (name, program, inactive) in enumerate(
            [
                ("Emma Vermeer", "Strength foundations", 8),
                ("Lucas De Smet", "Progressive strength", 3),
                ("Noor Janssens", "Return to training", 6),
                ("Milan Peeters", "Strength foundations", 1),
                ("Lena Dubois", "Progressive strength", 9),
                ("Adam Willems", "Return to training", 2),
            ]
        )
    ]


def attention(r):
    if r["inactive"] >= 7:
        return "Needs attention"
    if r["checkin"] and not r["reviewed"]:
        return "Review check-in"
    return "On track"


def present(records):
    return [
        r
        | {
            "status": attention(r),
            "value": f"{len(r['workouts'])} / {r['planned']}",
            "context": r["program"],
            "volume": sum(w["sets"] * w["reps"] * w["load"] for w in r["workouts"]),
        }
        for r in sorted(
            records, key=lambda r: (attention(r) != "Needs attention", r["name"])
        )
    ]


def metrics(records):
    completed = sum(len(r["workouts"]) for r in records)
    planned = sum(r["planned"] for r in records)
    return [
        metric("Active clients", len(records), "Synthetic coaching roster"),
        metric("Sessions logged", completed, f"Of {planned} planned this week"),
        metric(
            "Training adherence",
            f"{completed / planned * 100:.0f}%",
            "Completed sessions ÷ planned sessions",
        ),
        metric(
            "Need attention",
            sum(attention(r) == "Needs attention" for r in records),
            "No training activity for 7+ days",
        ),
    ]


def analysis(records):
    return {
        "title": "Make room for the human part.",
        "headline": "Less chasing. More coaching.",
        "description": "Log a squat session with actual sets, reps and load. Submit a weekly check-in, then mark it reviewed. This demo does not provide medical or exercise recommendations.",
        "bars_title": "Weekly session adherence · %",
        "bars": [
            {
                "label": r["name"],
                "value": len(r["workouts"]) / r["planned"] * 100,
                "display": f"{len(r['workouts'])}/{r['planned']}",
            }
            for r in records
        ],
    }


def execute(records, p):
    r = record(records, p)
    if p["action"] == "workout":
        if len(r["workouts"]) >= r["planned"]:
            raise ValueError("All planned sessions are already logged for this week")
        r["workouts"] = [
            *r["workouts"],
            dict(
                exercise="Squat",
                sets=number(p, "sets", 1, 10, True),
                reps=number(p, "reps", 1, 50, True),
                load=number(p, "load", 0, 300),
            ),
        ]
        r["inactive"] = 0
    elif p["action"] == "checkin":
        r["checkin"] = dict(
            sleep=number(p, "sleep", 0, 16),
            energy=number(p, "energy", 1, 5, True),
            note=text(p, "note", 500),
        )
        r["reviewed"] = False
    elif p["action"] == "review":
        if not r["checkin"] or r["reviewed"]:
            raise ValueError("No unreviewed check-in")
        r["reviewed"] = True
    else:
        raise ValueError("Unknown action")
    return r
