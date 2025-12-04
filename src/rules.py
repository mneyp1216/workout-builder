"""
Decision rules for the Workout Routine Builder
Contains simple logic for fitness level and time-based workout selection.
"""


def determine_workout_duration(user_time_minutes):
    """
    Determine the appropriate workout duration category based on user's available time.

    Args:
        user_time_minutes (int): User's available time in minutes

    Returns:
        int: Standardized workout duration (15, 30, or 45 minutes)

    Examples:
        >>> determine_workout_duration(10)
        15
        >>> determine_workout_duration(25)
        30
        >>> determine_workout_duration(50)
        45
    """
    # Safe default for invalid input
    if not isinstance(user_time_minutes, (int, float)) or user_time_minutes < 0:
        return 15  # Safe default: shortest workout

    # Decision rule with safe default
    if user_time_minutes <= 15:
        return 15
    elif user_time_minutes <= 30:
        return 30
    elif user_time_minutes <= 45:
        return 45
    else:
        return 45  # Cap at maximum supported duration


def validate_fitness_level(level):
    """
    Validate and normalize fitness level input.

    Args:
        level (str): User's fitness level input

    Returns:
        str: Normalized fitness level ('beginner' or 'intermediate')

    Examples:
        >>> validate_fitness_level('Beginner')
        'beginner'
        >>> validate_fitness_level('INTERMEDIATE')
        'intermediate'
        >>> validate_fitness_level('advanced')
        'intermediate'
        >>> validate_fitness_level('invalid')
        'beginner'
    """
    # Safe default for invalid input
    if not isinstance(level, str):
        return 'beginner'  # Safe default: beginner level

    level_lower = level.lower().strip()

    # Decision rule with safe default
    if 'beginner' in level_lower:
        return 'beginner'
    elif 'intermediate' in level_lower or 'advanced' in level_lower:
        return 'intermediate'
    else:
        return 'beginner'  # Safe default for unrecognized input


def should_include_warmup(workout_duration):
    """
    Determine if a warmup should be included based on workout duration.

    Args:
        workout_duration (int): Duration of the workout in minutes

    Returns:
        bool: True if warmup should be included, False otherwise

    Examples:
        >>> should_include_warmup(15)
        False
        >>> should_include_warmup(30)
        True
        >>> should_include_warmup(45)
        True
    """
    # Safe default for invalid input
    if not isinstance(workout_duration, (int, float)) or workout_duration < 0:
        return False  # Safe default: no warmup for invalid input

    # Decision rule: include warmup for workouts 20 minutes or longer
    return workout_duration >= 20


def calculate_exercise_count(fitness_level, duration):
    """
    Calculate the appropriate number of exercises for a workout.

    Args:
        fitness_level (str): User's fitness level ('beginner' or 'intermediate')
        duration (int): Workout duration in minutes

    Returns:
        int: Number of exercises to include in the workout

    Examples:
        >>> calculate_exercise_count('beginner', 15)
        4
        >>> calculate_exercise_count('beginner', 30)
        6
        >>> calculate_exercise_count('intermediate', 30)
        5
    """
    # Safe defaults
    level = validate_fitness_level(fitness_level)
    time = determine_workout_duration(duration)

    # Decision rules based on level and time
    if level == 'beginner':
        if time == 15:
            return 4
        elif time == 30:
            return 6
        else:  # 45 minutes
            return 8
    else:  # intermediate
        if time == 15:
            return 4
        elif time == 30:
            return 5
        else:  # 45 minutes
            return 7
