import pandas as pd

def input_data():
    data = {
        "Name": [],
        "Age": [],
        "Email": []
    }

    while True:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        email = input("Enter your email: ")

        data["Name"].append(name)
        data["Age"].append(age)
        data["Email"].append(email)

        another = input("Add another entry? (y/n): ").lower()
        if another != 'y':
            break

    return data

def export_to_excel(data, filename="output.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data successfully exported to {filename}")

if __name__ == "__main__":
    user_data = input_data()
    export_to_excel(user_data)
