import json
import openai
import requests
from gtts import gTTS
import os

with open('HW3.json', 'r') as file:
    data = json.load(file)

    person_name = data['name']
    first_interest = data[' interests '][0]
    second_project = data['projects'][1]['client']
    second_pet=data["pets"][1][' name ']

    print("The name is ",person_name)
    print("The first item in interests",first_interest)
    print("The second project client",second_project)
    print("The name of the second pet",second_pet)

    api_key = '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'
    openai.api_key = api_key

    # Create a conversation by incorporating the JSON data into a story prompt
    prompt = f"Once upon a time, there was a {data[' occupation ']} named {data['name']}. "
    prompt += f"{data['name']} lived in {data[' city ']} and was {data[' age ']} years old. "

    prompt += f"{data['name']} had a diverse set of interests, including {', '.join(data[' interests '])}. "
    prompt += f"They had completed their {data[' education ']} and worked on various projects. "

    project_list = ""
    for project in data['projects']:
        project_list += f"In {project[' year ']}, they worked on a project called '{project['name']}' for {project['client']}. "
    prompt += project_list

    pet_list = ""
    for pet in data['pets']:
        pet_list += f"They had a {pet[' type ']} named {pet[' name ']}. "
    prompt += pet_list

    prompt += "Tell me more about their exciting life."

    # Make an API call to generate the story
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150  # Adjust as needed for the desired story length
    )

    # Extract and print the generated story
    generated_story = response.choices[0].text


    output_file = 'story.txt'
    with open(output_file, 'w') as file:
        file.write(generated_story)

    print(generated_story)

    input_file = "story.txt"

    # Read text from the file
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Create a gTTS object to convert text to speech
    tts = gTTS(text, lang="en")  # You can specify the language (e.g., "en" for English)

    # Save the generated speech to an output file
    output_file = "output.mp3"
    tts.save(output_file)

    # Play the generated speech using your system's default audio player
    os.system(f"start {output_file}")















