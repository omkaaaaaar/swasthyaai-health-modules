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
