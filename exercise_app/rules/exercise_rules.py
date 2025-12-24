# exercise_app/rules/exercise_rules.py

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
