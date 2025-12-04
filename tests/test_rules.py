"""
Unit tests for workout decision rules.
Tests the core logic in rules.py to ensure correct behavior.
"""

import sys
import os

# Add src directory to path so we can import rules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from rules import (
    determine_workout_duration,
    validate_fitness_level,
    should_include_warmup,
    calculate_exercise_count
)


def test_determine_workout_duration():
    """Test that workout duration is correctly categorized"""
    # Test basic categorization
    assert determine_workout_duration(10) == 15
    assert determine_workout_duration(15) == 15
    assert determine_workout_duration(20) == 30
    assert determine_workout_duration(30) == 30
    assert determine_workout_duration(40) == 45
    assert determine_workout_duration(45) == 45
    assert determine_workout_duration(60) == 45  # Caps at 45

    # Test safe defaults
    assert determine_workout_duration(-5) == 15  # Negative time
    assert determine_workout_duration(0) == 15  # Zero time

    print("✓ test_determine_workout_duration passed")


def test_validate_fitness_level():
    """Test that fitness level is correctly validated and normalized"""
    # Test valid inputs
    assert validate_fitness_level('beginner') == 'beginner'
    assert validate_fitness_level('Beginner') == 'beginner'
    assert validate_fitness_level('BEGINNER') == 'beginner'
    assert validate_fitness_level('intermediate') == 'intermediate'
    assert validate_fitness_level('Intermediate') == 'intermediate'
    assert validate_fitness_level('advanced') == 'intermediate'

    # Test safe defaults
    assert validate_fitness_level('invalid') == 'beginner'
    assert validate_fitness_level('') == 'beginner'
    assert validate_fitness_level(None) == 'beginner'

    print("✓ test_validate_fitness_level passed")


# Run tests if this file is executed directly
if __name__ == "__main__":
    print("\nRunning tests for rules.py...\n")

    try:
        test_determine_workout_duration()
        test_validate_fitness_level()

        print("\n" + "=" * 50)
        print("ALL TESTS PASSED! ✓")
        print("=" * 50 + "\n")

    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ ERROR: {e}\n")
        sys.exit(1)
