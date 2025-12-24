# exercise_app/rules/exercise_rules.py

import json
import os

"""
Orthopedic condition profiles.
Each profile defines how a medical condition constrains
safe orthopedic exercise recommendations.
"""

ORTHOPEDIC_PROFILES = {
    "hypertension": {
        "allowed_movements": ["seated", "walking"],
        "max_joint_load": "very_low",
        "pace": "slow_steady",
        "progression": "increase_time",
        "note": "Avoid sudden pace or intensity changes"
    },

    "diabetes": {
        "allowed_movements": ["walking", "standing_supported"],
        "max_joint_load": "low",
        "pace": "steady",
        "progression": "increase_time",
        "note": "Maintain rhythm and avoid fatigue"
    },

    "pre-diabetes": {
        "allowed_movements": ["walking", "standing_supported"],
        "max_joint_load": "low",
        "pace": "steady",
        "progression": "increase_time",
        "note": "Gradual progression is recommended"
    },

    "pcos": {
        "allowed_movements": ["walking", "mobility"],
        "max_joint_load": "low",
        "pace": "steady",
        "progression": "increase_time",
        "note": "Consistency is more important than intensity"
    },

    "thyroid-hyper": {
        "allowed_movements": ["seated", "walking"],
        "max_joint_load": "very_low",
        "pace": "slow",
        "progression": "increase_time",
        "note": "Avoid overexertion"
    },

    "thyroid-hypo": {
        "allowed_movements": ["seated", "walking"],
        "max_joint_load": "low",
        "pace": "slow_steady",
        "progression": "increase_time",
        "note": "Start slow and progress gradually"
    },

    "none": {
        "allowed_movements": ["seated", "walking", "standing_supported"],
        "max_joint_load": "low",
        "pace": "steady",
        "progression": "increase_time",
        "note": "General orthopedic beginner plan"
    }
}

def combine_orthopedic_profiles(conditions):
    """
    Combine multiple orthopedic condition profiles into
    one final safe constraint set.
    """

    # Default to 'none' if no condition is provided
    if not conditions:
        conditions = ["none"]

    # Filter valid conditions only
    profiles = [
        ORTHOPEDIC_PROFILES[c]
        for c in conditions
        if c in ORTHOPEDIC_PROFILES
    ]

    # Start with the first profile
    combined = profiles[0].copy()

    for profile in profiles[1:]:
        # Allowed movements: intersection
        combined["allowed_movements"] = list(
            set(combined["allowed_movements"]) &
            set(profile["allowed_movements"])
        )

        # Joint load: choose the strictest
        if profile["max_joint_load"] == "very_low":
            combined["max_joint_load"] = "very_low"

        # Pace: choose slowest
        pace_priority = ["slow", "slow_steady", "steady"]
        combined["pace"] = min(
            combined["pace"],
            profile["pace"],
            key=lambda p: pace_priority.index(p)
        )

        # Progression remains conservative
        combined["progression"] = "increase_time"

    return combined


def select_top_3_exercises(combined_profile):
    """
    Select exactly 3 orthopedic exercises
    with maximum movement diversity while
    respecting all safety constraints.
    """

    import json
    import os

    # Load exercise database
    data_path = os.path.join(
        os.path.dirname(__file__),
        "..", "data", "exercises.json"
    )
    with open(data_path, "r") as f:
        exercises = json.load(f)

    # Step 1: Filter exercises by safety rules
    safe_exercises = [
        ex for ex in exercises
        if ex["movement_type"] in combined_profile["allowed_movements"]
        and (
            combined_profile["max_joint_load"] == "low"
            or ex["joint_load"] == "very_low"
        )
    ]

    # Step 2: Group exercises by movement type
    grouped = {
        "seated": [],
        "standing_supported": [],
        "walking": []
    }

    for ex in safe_exercises:
        grouped[ex["movement_type"]].append(ex)

    # Step 3: Pick exercises with diversity
    selected = []

    for movement in ["seated", "standing_supported", "walking"]:
        if grouped[movement]:
            selected.append(grouped[movement][0])
        if len(selected) == 3:
            break

    # Step 4: Fill remaining slots if needed
    if len(selected) < 3:
        for ex in safe_exercises:
            if ex not in selected:
                selected.append(ex)
            if len(selected) == 3:
                break

    return selected
