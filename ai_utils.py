from google import genai


MODEL_NAME = "gemini-3.1-flash-lite"


def generate_response(client, prompt):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text