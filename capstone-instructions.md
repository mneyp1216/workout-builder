## **Workout Routine Builder**

### **The Challenge**

Beginners don't know how to start exercising. They need a simple routine to follow and someone to explain exercises in plain language.

### **Your Mission**

Build a conversational AI that:

* Asks about fitness level (beginner/intermediate)  
* Asks about available time (15 min / 30 min / 45 min)  
* Suggests a workout routine (3-5 exercises)  
* Explains how to do each exercise  
* Tracks completed workouts

### **Example Conversation**

Bot: Welcome\! Are you a beginner or intermediate exerciser?  
User: Beginner  
Bot: How much time do you have today?  
User: 20 minutes  
Bot: Perfect\! Here's your 20-minute beginner workout:  
     1\. Jumping Jacks \- 2 minutes  
     2\. Bodyweight Squats \- 10 reps  
     3\. Push-ups (modified) \- 5 reps  
     4\. Plank \- 30 seconds  
     5\. Repeat 2x  
     Want me to explain any exercise?  
User: How do I do a plank?  
Bot: \[AI explains plank form\]  
User: Done\!  
Bot: Awesome\! That's workout \#3 this week. Keep going\! 💪

### **What You'll Build**

* Hardcoded workout library (10-15 basic exercises)  
* Simple routine generator based on time/level  
* Use AI API to explain exercises in detail  
* Count workouts completed (simple counter in a file)

### **Technical Requirements**

* 4 intents (set level, get routine, explain exercise, log completion)  
* 3 pre-built routines (beginner 15/30 min, intermediate 30 min)  
* Track workout count