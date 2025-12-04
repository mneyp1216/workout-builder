"""
Workout Routine Builder - Main Application
A conversational AI that helps users build personalized workout routines.
"""

import os
import sys
from workout_builder import WorkoutRoutineBuilder


def main():
    """Main entry point for the Workout Routine Builder CLI"""

    # Print greeting
    print("=" * 50)
    print("🏋️  WORKOUT ROUTINE BUILDER  🏋️")
    print("=" * 50)
    print("\nWelcome to your personal fitness assistant!")
    print("I'll help you create a custom workout routine.\n")

    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not api_key:
        print("⚠️  ERROR: ANTHROPIC_API_KEY not found in environment variables.")
        print("Please set your API key in the .env file or environment.\n")
        sys.exit(1)

    # Initialize the workout builder
    try:
        bot = WorkoutRoutineBuilder(api_key)
        print("✓ Successfully connected to AI service\n")
    except Exception as e:
        print(f"⚠️  ERROR: Failed to initialize: {e}\n")
        sys.exit(1)

    # Start the conversation loop
    print("Type 'quit' or 'exit' to end the session.\n")
    print("-" * 50)

    # Initial greeting
    print(f"\nBot: {bot.chat('hello')}\n")

    # Conversation loop
    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print("\nBot: Great job today! Remember, consistency is key. See you next time! 💪\n")
                break

            # Get bot response
            response = bot.chat(user_input)
            print(f"\nBot: {response}\n")

        except KeyboardInterrupt:
            print("\n\nBot: Session ended. Keep up the great work! 💪\n")
            break
        except Exception as e:
            print(f"\n⚠️  ERROR: {e}\n")
            print("Let's try that again.\n")


if __name__ == "__main__":
    main()
