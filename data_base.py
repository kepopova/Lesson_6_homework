def set_value(key, value):
    with open("example.db", "a") as file:
        file.write( key + ":" + value + "\n")


set_value("Password", "12345")
def get_value(key: str) -> str:
    with open("example.db", "r") as file:
        for line in file:
            if key + ":" in line
                return line.split(":")[1].replace("\n","")