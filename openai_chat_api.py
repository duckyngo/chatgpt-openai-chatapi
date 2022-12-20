

import openai
import PySimpleGUI as sg

openai.api_key = "YOUR_API_KEY"

def get_response(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Enter a message:'), sg.InputText()],
            [sg.Button('Send'), sg.Button('Exit')] ]

window = sg.Window('OpenAI Chat Bot', layout)

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Exit':
    break
  if event == 'Send':
    message = values[0]
    response = get_response(message)
    sg.popup(response)

window.close()