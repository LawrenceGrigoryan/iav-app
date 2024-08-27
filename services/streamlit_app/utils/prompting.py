import random

tones = [
    "Sarcastic",
    "Playful",
    "Dry",
    "Deadpan",
    "Whimsical",
    "Witty",
    "Dark",
    "Self-deprecating",
    "Absurd",
    "Cynical"
]

styles = [
    "Slapstick",
    "Satire",
    "Parody",
    "Puns/Wordplay",
    "Observational",
    "Surreal",
    "Irony",
    "Anecdotal",
    "Black Humor",
    "Blue Humor",
    "Character Comedy",
    "Sitcom"
]

emotions = [
    "positive",
    "negative"
]

prompt_template = """\
Act as a professional comedian. Write a hilarious joke. Make it non-trivial and funny for a broad audience.
Your joke should consist of a setup and punchline. Keep things short and concise.

Here is some auxiliary information that you must consider when writing a joke:

1. Tone: {tone}
2. Style: {style}
3. Emotion: {emotion}\
"""


def compile_prompt(context: str) -> str:
    # randomly choose a style
    tone = random.choice(tones)
    # randomly choose a tone
    style = random.choice(styles)
    # randomly choose an emotion
    emotion = random.choice(emotions)
    
    # compile the prompt
    prompt = prompt_template.format(tone=tone, style=style, emotion=emotion)
    
    # add context if provided by the user
    if context:
        prompt += f"\n\nContext for a joke: {context}"

    return prompt
