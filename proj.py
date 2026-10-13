import json

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    message = input("Enter your message: ")
except ValueError:
    print("invalid age .. must be a number")
except:
    print("something went wrong please try again..!")

submission = {
    "name": name,
    "age": age,
    "message": message
}

print(json.dumps(submission))