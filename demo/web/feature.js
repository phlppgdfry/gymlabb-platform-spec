export function inspect(r) {
  return {
    fields: [
      ["Training plan", r.program],
      ["Last training activity", `${r.inactive} days ago`],
      [
        "Squat volume this week",
        `${r.volume.toLocaleString()} kg · sets × reps × load`,
      ],
      [
        "Weekly check-in",
        r.checkin
          ? `${r.checkin.sleep} h sleep · energy ${r.checkin.energy}/5`
          : "Not submitted",
      ],
      ...(r.checkin
        ? [
            ["Client note", r.checkin.note],
            ["Coach review", r.reviewed ? "Reviewed" : "Awaiting review"],
          ]
        : []),
    ],
    forms: [
      ...(r.workouts.length < r.planned
        ? [
            {
              title: "Log a squat session",
              help: "One entry records the same reps and load for each set. No session is pre-filled as completed.",
              action: "workout",
              button: "Save training session",
              fields: [
                {
                  key: "sets",
                  label: "Sets",
                  type: "number",
                  min: 1,
                  max: 10,
                  value: 3,
                },
                {
                  key: "reps",
                  label: "Reps per set",
                  type: "number",
                  min: 1,
                  max: 50,
                  value: 8,
                },
                {
                  key: "load",
                  label: "Load · kg",
                  type: "number",
                  min: 0,
                  max: 300,
                  step: 0.5,
                  value: 40,
                },
              ],
            },
          ]
        : []),
      {
        title: "Weekly check-in",
        help: "Replace this week’s check-in. A new check-in always requires coach review.",
        action: "checkin",
        button: "Submit check-in",
        fields: [
          {
            key: "sleep",
            label: "Average sleep · hours",
            type: "number",
            min: 0,
            max: 16,
            step: 0.5,
            value: r.checkin?.sleep ?? 7,
          },
          {
            key: "energy",
            label: "Energy · 1 low, 5 high",
            type: "number",
            min: 1,
            max: 5,
            value: r.checkin?.energy ?? 3,
          },
          {
            key: "note",
            label: "Note for your coach",
            type: "textarea",
            maxLength: 500,
            value: r.checkin?.note ?? "",
          },
        ],
      },
      ...(r.checkin && !r.reviewed
        ? [
            {
              title: "Coach review",
              action: "review",
              button: "Mark check-in reviewed",
              fields: [],
            },
          ]
        : []),
    ],
    note: "A single local workspace demonstrates both client and coach actions. Only use fictional training and wellbeing data.",
  };
}
