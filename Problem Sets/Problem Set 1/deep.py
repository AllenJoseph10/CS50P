question = (input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))

cleaned_question = question.lower().replace(" ", "")

match cleaned_question:
    case "42" | "forty-two" | "fortytwo":
        print("Yes")
    case _:
        print("No")
