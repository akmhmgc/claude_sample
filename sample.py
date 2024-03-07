import anthropic

client = anthropic.Anthropic()

system_prompt = """
"""

messages = [
]

while True:
  print("あなた:")
  user_input = input()
  messages.append({
    "role": "user",
    "content": user_input
    })
  message = client.messages.create(
      model="claude-3-opus-20240229",
      system=system_prompt,
      max_tokens=1000,
      temperature=0,
      messages=messages
  )
  answer = message.content[0].text
  print(f'bot: {answer}')
  messages.append({
    "role": "assistant",
    "content": answer
    })
  
