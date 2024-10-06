import datetime

class SimpleAIAssistant:
    def __init__(self):
        self.reminders = []

    def greet(self):
        return "Hello! How can I assist you today?"

    def set_reminder(self, reminder):
        self.reminders.append(reminder)
        return f"Reminder set: {reminder}"

    def show_reminders(self):
        if not self.reminders:
            return "You have no reminders set."
        return "Your reminders:\n" + "\n".join(self.reminders)

    def answer_question(self, question):
        if "how are you" in question.lower():
            return "I'm just a program, but thanks for asking!"
        elif "time" in question.lower():
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
        else:
            return "I'm not sure how to answer that. Try asking something else."

def main():
    assistant = SimpleAIAssistant()
    print(assistant.greet())

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        elif user_input.lower().startswith("remind me to"):
            reminder = user_input[13:]  # Extract reminder text
            print(assistant.set_reminder(reminder))
        elif user_input.lower() == "show reminders":
            print(assistant.show_reminders())
        else:
            print(assistant.answer_question(user_input))

if __name__ == "__main__":
    main()
