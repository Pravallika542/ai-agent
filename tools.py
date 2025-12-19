from google import genai
import os

class GeminiTool:
    def __init__(self):
        self.client = genai.Client(
            api_key="paste your google api key here"
        )

    def run(self, prompt):
        response = self.client.models.generate_content(
            model="models/gemini-flash-lite-latest",
            contents=prompt
        )
        return response.text