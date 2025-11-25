import time

def hello_ai():
    print("=" * 50)
    print("🤖 Welcome to the AI Learning Hub! 🚀")
    print("=" * 50)
    print()
    
    # Get student name
    name = input("👤 What's your name, student? ")
    print(f"\n✨ Hello, {name}! Nice to meet you! ✨\n")
    
    # Get student details
    age = input("🎂 How old are you? ")
    school = input("🏫 Which school do you attend? ")
    interest = input("🎯 What's your main interest in AI? (e.g., Robotics, Games, Data) ")
    
    # Display summary
    print("\n" + "=" * 50)
    print("📋 Student Profile Summary:")
    print("=" * 50)
    print(f"👤 Name: {name}")
    print(f"🎂 Age: {age}")
    print(f"🏫 School: {school}")
    print(f"🎯 Interest: {interest}")
    print("=" * 50)
    
    print("\n🎉 You're all set to start your AI journey! 🌟")
    print("💡 Keep learning, stay curious, and have fun! 🚀\n")

if __name__ == "__main__":
    hello_ai()