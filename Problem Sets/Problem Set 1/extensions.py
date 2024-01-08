type = input("File name: ")

type_new = type.lower().replace(" ", "")

if type_new.endswith(".gif"):
    print("image/gif")
elif type_new.endswith(".jpg"):
    print("image/jpeg")
elif type_new.endswith(".jpeg"):
    print("image/jpeg")
elif type_new.endswith(".png"):
    print("image/png")
elif type_new.endswith(".pdf"):
    print("application/pdf")
elif type_new.endswith(".txt"):
    print("text/plain")
elif type_new.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
