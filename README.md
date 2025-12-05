# Workout Routine Builder

A conversational AI-powered workout assistant that helps beginners and intermediate fitness enthusiasts build personalized workout routines.

## Team Members

- Miguel Pena - [@mneyp1216](https://github.com/mneyp1216)
- Team Member 2 - [@github-handle-2](https://github.com/github-handle-2)
- Team Member 3 - [@github-handle-3](https://github.com/github-handle-3)
- Team Member 4 - [@github-handle-4](https://github.com/github-handle-4)

## Purpose

This project addresses a common challenge faced by fitness beginners: not knowing where to start with exercise. Our conversational AI helps users by:

- Creating personalized workout routines based on fitness level and available time
- Providing clear explanations of exercises using AI
- Tracking workout completion to encourage consistency
- Offering beginner-friendly guidance in plain language

## Features

- **Fitness Level Assessment**: Tailors workouts to beginner or intermediate levels
- **Time-Based Routines**: Generates 15, 30, or 45-minute workout plans
- **Exercise Library**: 10-15 fundamental exercises with proper instructions
- **AI-Powered Explanations**: Detailed exercise guidance using AI API
- **Workout Tracking**: Counts completed workouts to motivate users
- **Intent-Based Conversation**: Natural language interaction for easy use

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- An API key from OpenAI, Anthropic, or similar AI service

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-org/workout-builder.git
cd workout-builder
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your environment:
```bash
cp .env.sample .env
```

4. Add your AI API key to the `.env` file:
```
API_KEY=your-api-key-here
```

## Usage

### Running the Application

Start the workout builder CLI:

```bash
python src/app.py
```

### Example Conversation

```
Bot: Welcome! Are you a beginner or intermediate exerciser?
User: Beginner

Bot: How much time do you have today?
User: 20 minutes

Bot: Perfect! Here's your 20-minute beginner workout:
     1. Jumping Jacks - 2 minutes
     2. Bodyweight Squats - 10 reps
     3. Push-ups (modified) - 5 reps
     4. Plank - 30 seconds
     5. Repeat 2x
     Want me to explain any exercise?

User: How do I do a plank?
Bot: [AI-generated explanation of proper plank form]

User: Done!
Bot: Awesome! That's workout #3 this week. Keep going!
```

### Available Commands

- Set your fitness level (beginner/intermediate)
- Specify available workout time
- Request a workout routine
- Ask for exercise explanations
- Log workout completion

## Project Structure

```
workout-builder/
├── src/
│   ├── app.py              # Main application entry point
│   ├── rules.py            # Decision rules and workout logic
│   └── exercises.py        # Exercise library
├── tests/
│   └── test_rules.py       # Unit tests
├── .env.sample             # Environment variable template
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Responsible AI Use

This project uses AI technology to provide exercise explanations and guidance. We are committed to responsible AI practices:

### Our Commitments

1. **Accuracy & Safety**: AI-generated exercise advice is reviewed for safety and accuracy. We prioritize beginner-friendly modifications and proper form guidance.

2. **Transparency**: Users are informed when they're receiving AI-generated content. All exercise explanations clearly indicate they come from an AI assistant.

3. **Data Privacy**: User workout data is stored locally on their device. No personal fitness information is shared with third parties or used for AI training.

4. **Limitations Awareness**: We acknowledge that AI-generated fitness advice should not replace professional medical or fitness guidance. Users with health concerns should consult healthcare providers before starting any exercise program.

5. **Bias Mitigation**: We strive to provide inclusive fitness guidance that considers various fitness levels, abilities, and backgrounds. Exercise modifications are offered to accommodate different needs.

6. **Human Oversight**: AI-generated content is designed to supplement, not replace, evidence-based fitness principles. Our exercise library is curated by the development team.

### User Responsibilities

- Consult a healthcare provider before starting any new exercise program
- Listen to your body and stop if you experience pain or discomfort
- Verify AI-generated exercise advice with reliable fitness resources when uncertain
- Report any concerning or unsafe AI-generated content to the development team

### Reporting Issues

If you encounter inappropriate, unsafe, or inaccurate AI-generated content, please report it by opening an issue in our GitHub repository.

## Team Prompt Library

Our team uses a shared collection of AI prompts to ensure consistent, high-quality AI interactions. View our prompt library here:

[Team Prompt Library](https://github.com/your-org/workout-builder/wiki/Prompt-Library)

This library includes:
- Exercise explanation prompts
- Safety and modification guidance templates
- User interaction patterns
- Quality assurance guidelines

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Contributing

1. Create a new branch for your feature
2. Make your changes
3. Write tests for new functionality
4. Ensure all tests pass
5. Submit a pull request referencing the relevant issue

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built as part of Justice Through Code curriculum
- Exercise data based on evidence-based fitness principles
- AI integration powered by [OpenAI/Anthropic/etc.]
