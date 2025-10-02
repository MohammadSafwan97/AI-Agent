import litellm
import os
import sys
from Listen import listen   # your microphone input function
from speak import speak     # your text-to-speech function

# -------------------------------
# API Key setup
# -------------------------------
litellm.api_key = os.getenv("OPENAI_API_KEY")
if not litellm.api_key:
    print("❌ Error: API key not found. Please set OPENAI_API_KEY")
    sys.exit(1)

# Model
MODEL = "gpt-4o-mini"

def myagent():
    conversation = []
    active = False  # starts inactive

    speak(" Initiating Jarvis...")
    print("🎤 Say 'Jarvis' to activate me.")

    while True:
        request = listen(timeout=8, phrase_time_limit=10).lower().strip()

        # If nothing understood, keep listening
        if not request:
            continue

        # -------------------------------
        # Wake word detection
        # -------------------------------
        wake_words = ["jarvis", "jarv", "javis", "jarviz", "jar"]
        if any(w in request for w in wake_words) and not active:
            active = True
            speak("Yes? What can I do?")
            print("✅ Jarvis activated. Waiting for your command...")

            # Immediately capture the command after wake word
            command = listen(timeout=12, phrase_time_limit=15).lower().strip()
            if command:
                # If user says exit/bye directly after wake
                if command in ["exit", "bye", "stop"]:
                    speak("Goodbye")
                    print("⏸️ Jarvis going inactive. Say 'Jarvis' to wake me again.")
                    active = False
                    continue

                # Otherwise, send command to LLM
                conversation.append({"role": "user", "content": command})
                try:
                    response = litellm.completion(
                        model=MODEL,
                        max_tokens=100,
                        messages=conversation,
                    )
                    reply = response["choices"][0]["message"]["content"]
                    print(f"Agent: {reply}\n")
                    speak(reply)
                    conversation.append({"role": "assistant", "content": reply})
                except Exception as e:
                    print(f"⚠️ LLM Error: {str(e)}")
                    speak("Sorry, I had trouble processing that.")
            continue  # skip to next loop

        # -------------------------------
        # If inactive, ignore everything
        # -------------------------------
        if not active:
            continue

        # -------------------------------
        # Deactivation keywords
        # -------------------------------
        if request in ["exit", "bye", "stop"]:
            speak("Goodbye")
            print("⏸️ Jarvis is now inactive. Say 'Jarvis' to wake me again.")
            active = False
            continue

        # -------------------------------
        # Normal conversation when active
        # -------------------------------
        conversation.append({"role": "user", "content": request})

        try:
            response = litellm.completion(
                model=MODEL,
                max_tokens=200,
                messages=conversation,
            )

            reply = response["choices"][0]["message"]["content"]
            print(f"Agent: {reply}\n")
            speak(reply)
            conversation.append({"role": "assistant", "content": reply})

        except Exception as e:
            print(f"⚠️ LLM Error: {str(e)}")
            speak("Sorry, I had trouble processing that.")


if __name__ == "__main__":
    myagent()
