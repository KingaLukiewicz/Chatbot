import os
from dotenv import load_dotenv
from anthropic import (
    Anthropic,
    RateLimitError,
    APIConnectionError,
    AuthenticationError,
    APIError,
)

load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
MODEL = "claude-haiku-5"
MAX_TOKENS = 1024
history = []


def ask_claude(question):
    """Sends a question to the Claude model and returns the response."""
    history.append({"role": "user", "content": question})

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=history,
        )

        answer = response.content[0].text
        return answer
    except AuthenticationError:
        history.pop()
        return "ERROR: problem with API key. Check .env file."
    except RateLimitError:
        history.pop()
        return "ERROR: Too many requests. Please wait a moment and try again."
    except APIConnectionError:
        history.pop()
        return "ERROR: Connection error."
    except APIError as error:
        history.pop()
        return f"ERROR: Something went wrong on server side ({error})."


def main():
    """Main function to run the chatbot."""
    print("=" * 50)
    print("Chatbot AI, Type 'quit' to quit.")
    print("=" * 50)
    print()

    while True:
        question = input("\nYou: ")
        if question.lower().strip() == "quit":
            print("Goodbye!")
            break
        elif question.lower().strip() == "":
            print("Please enter a question.")
            continue
        answer = ask_claude(question)
        print(f"Claude: {answer}")


if __name__ == "__main__":
    main()
