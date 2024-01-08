question = str(input("Greeting: "))

cleaned_question = str(question.lower().replace(" ", ""))

substring = "hello"

if substring in cleaned_question:
    print("$0")
elif cleaned_question.startswith("h"):
    print("$20")
else:
    print("$100")
