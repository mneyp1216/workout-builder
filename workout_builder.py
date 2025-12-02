import anthropic
import json
import os
from datetime import datetime

class WorkoutRoutineBuilder:
    def __init__(self, api_key):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.conversation_history = []
        self.user_level = None
        self.user_time = None
        self.current_routine = None
        self.workout_count = self.load_workout_count()
        
        # Hardcoded workout library
        self.exercises = {
            'jumping_jacks': {'name': 'Jumping Jacks', 'duration': '2 minutes', 'level': 'beginner'},
            'bodyweight_squats': {'name': 'Bodyweight Squats', 'reps': '10 reps', 'level': 'beginner'},
            'modified_pushups': {'name': 'Push-ups (modified)', 'reps': '5 reps', 'level': 'beginner'},
            'plank': {'name': 'Plank', 'duration': '30 seconds', 'level': 'beginner'},
            'lunges': {'name': 'Lunges', 'reps': '10 reps per leg', 'level': 'beginner'},
            'mountain_climbers': {'name': 'Mountain Climbers', 'duration': '1 minute', 'level': 'beginner'},
            'burpees': {'name': 'Burpees', 'reps': '8 reps', 'level': 'intermediate'},
            'regular_pushups': {'name': 'Push-ups (regular)', 'reps': '15 reps', 'level': 'intermediate'},
            'jump_squats': {'name': 'Jump Squats', 'reps': '12 reps', 'level': 'intermediate'},
            'plank_60': {'name': 'Plank', 'duration': '60 seconds', 'level': 'intermediate'},
            'high_knees': {'name': 'High Knees', 'duration': '2 minutes', 'level': 'intermediate'},
        }
        
        # Pre-built routines
        self.routines = {
            ('beginner', 15): [
                'jumping_jacks', 'bodyweight_squats', 'modified_pushups', 'plank'
            ],
            ('beginner', 30): [
                'jumping_jacks', 'bodyweight_squats', 'modified_pushups', 
                'plank', 'lunges', 'mountain_climbers'
            ],
            ('intermediate', 30): [
                'high_knees', 'jump_squats', 'regular_pushups', 
                'burpees', 'plank_60'
            ],
        }
    
    def load_workout_count(self):
        """Load workout count from file"""
        if os.path.exists('workout_count.txt'):
            with open('workout_count.txt', 'r') as f:
                return int(f.read().strip())
        return 0
    
    def save_workout_count(self):
        """Save workout count to file"""
        with open('workout_count.txt', 'w') as f:
            f.write(str(self.workout_count))
    
    def increment_workout_count(self):
        """Increment and save workout count"""
        self.workout_count += 1
        self.save_workout_count()
    
    def get_routine(self, level, time):
        """Get the appropriate routine based on level and time"""
        # Find closest matching time
        if time <= 15:
            target_time = 15
        elif time <= 30:
            target_time = 30
        else:
            target_time = 30  # Cap at 30 for this example
        
        # Get routine or default to beginner 15
        routine_key = (level, target_time)
        if routine_key not in self.routines:
            routine_key = ('beginner', 15)
        
        return self.routines[routine_key]
    
    def format_routine(self, exercise_keys):
        """Format routine for display"""
        routine_text = ""
        for i, key in enumerate(exercise_keys, 1):
            ex = self.exercises[key]
            detail = ex.get('reps') or ex.get('duration')
            routine_text += f"{i}. {ex['name']} - {detail}\n"
        
        # Add repeat instruction
        if self.user_time and self.user_time >= 20:
            routine_text += "\nRepeat 2x for a complete workout!"
        
        return routine_text
    
    def classify_intent(self, user_message):
        """Classify user intent using simple rules"""
        msg_lower = user_message.lower()
        
        # Check for completion
        if any(word in msg_lower for word in ['done', 'finished', 'completed', 'did it']):
            return 'log_completion'
        
        # Check for explanation request
        if any(word in msg_lower for word in ['how', 'explain', 'what is', 'show me']):
            return 'explain_exercise'
        
        # Check for fitness level
        if any(word in msg_lower for word in ['beginner', 'intermediate', 'advanced']):
            return 'set_level'
        
        # Check for time
        if any(word in msg_lower for word in ['minute', 'min', 'time']) or msg_lower.isdigit():
            return 'get_routine'
        
        return 'general'
    
    def handle_set_level(self, user_message):
        """Handle fitness level setting"""
        msg_lower = user_message.lower()
        if 'beginner' in msg_lower:
            self.user_level = 'beginner'
            return "Great! How much time do you have today? (15, 30, or 45 minutes)"
        elif 'intermediate' in msg_lower:
            self.user_level = 'intermediate'
            return "Awesome! How much time do you have today? (15, 30, or 45 minutes)"
        else:
            return "I didn't catch that. Are you a beginner or intermediate exerciser?"
    
    def handle_get_routine(self, user_message):
        """Handle routine generation"""
        # Extract time from message
        import re
        numbers = re.findall(r'\d+', user_message)
        
        if numbers:
            self.user_time = int(numbers[0])
        else:
            return "How many minutes do you have? (e.g., 15, 30, or 45)"
        
        if not self.user_level:
            return "First, let me know: are you a beginner or intermediate exerciser?"
        
        # Generate routine
        exercise_keys = self.get_routine(self.user_level, self.user_time)
        self.current_routine = exercise_keys
        routine_text = self.format_routine(exercise_keys)
        
        return f"Perfect! Here's your {self.user_time}-minute {self.user_level} workout:\n\n{routine_text}\n\nWant me to explain any exercise? Just ask!"
    
    def handle_explain_exercise(self, user_message):
        """Use AI to explain an exercise"""
        # Build prompt for AI
        prompt = f"""The user asked: "{user_message}"

Please explain the exercise they're asking about in a clear, beginner-friendly way. 
Include:
- Starting position
- Step-by-step instructions
- Common mistakes to avoid
- One helpful tip

Keep it concise (3-4 sentences max) and encouraging."""
        
        # Call Anthropic API
        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=300,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.content[0].text
    
    def handle_log_completion(self):
        """Log workout completion"""
        self.increment_workout_count()
        
        messages = [
            f"Awesome! That's workout #{self.workout_count} this week. Keep going! 💪",
            f"Amazing work! You've completed {self.workout_count} workouts. You're crushing it! 🔥",
            f"Yes! Workout #{self.workout_count} in the books! Consistency is key! 🎯",
        ]
        
        # Rotate through messages
        return messages[(self.workout_count - 1) % len(messages)]
    
    def chat(self, user_message):
        """Main chat function"""
        # Classify intent
        intent = self.classify_intent(user_message)
        
        # Route to appropriate handler
        if intent == 'set_level':
            response = self.handle_set_level(user_message)
        elif intent == 'get_routine':
            response = self.handle_get_routine(user_message)
        elif intent == 'explain_exercise':
            response = self.handle_explain_exercise(user_message)
        elif intent == 'log_completion':
            response = self.handle_log_completion()
        else:
            # General conversation - could use AI here too
            if not self.user_level:
                response = "Welcome! Are you a beginner or intermediate exerciser?"
            elif not self.user_time:
                response = "How much time do you have today? (15, 30, or 45 minutes)"
            else:
                response = "I'm here to help! You can ask me to explain exercises or let me know when you're done!"
        
        return response


# Example usage and demo
def main():
    # Initialize with your API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    bot = WorkoutRoutineBuilder(api_key)
    
    print("=== Workout Routine Builder Demo ===\n")
    
    # Simulate conversation
    conversations = [
        "Hi there!",
        "I'm a beginner",
        "I have 20 minutes",
        "How do I do a plank?",
        "What about jumping jacks?",
        "Done!"
    ]
    
    for user_msg in conversations:
        print(f"User: {user_msg}")
        response = bot.chat(user_msg)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()