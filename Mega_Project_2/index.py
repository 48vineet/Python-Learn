import time

import pyautogui
import pyperclip
from google import genai

client = genai.Client(api_key="")
SYSTEM_PROMPT = """
You are a person named vineet who speaks hinglish as well as english . He is is from india and is a coder you analyse chat history and speak like harry the traits of vineet is he is introvert and aftere few talks he become the extrovert so respond  like vineet and give short replies
"""


def ask_ai(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SYSTEM_PROMPT}\nUser: {prompt}\nJarvis:"
        )
        return response.text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I had trouble answering that."


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05

time.sleep(3)

# Focus app
pyautogui.click(718, 739)
time.sleep(1)

# Move to start
pyautogui.moveTo(495, 159)
time.sleep(0.2)

# HARD press
pyautogui.mouseDown()

# 🔥 FORCE DRAG WITH SMALL STEPS (KEY FIX)
for i in range(50):
    pyautogui.moveRel(8, 8)
    time.sleep(0.01)

# Final move to end
pyautogui.moveTo(937, 636, duration=1.0)

# Release
pyautogui.mouseUp()
time.sleep(0.4)

# Copy
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.3)
pyautogui.click(495, 159)

chatHistory = pyperclip.paste()

# Get AI reply
ai_reply = ask_ai(chatHistory)

# Copy AI reply to clipboard
pyperclip.copy(ai_reply)
time.sleep(0.2)

# Click input field
pyautogui.click(624, 677)
time.sleep(0.2)

# Paste reply
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.1)

# Send (Enter)
pyautogui.press('enter')
