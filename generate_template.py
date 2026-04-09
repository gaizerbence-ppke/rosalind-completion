import os

def generateTemplate():
    problem_id = input("Input problem id:")
    problem_id = "".join(char.lower() for char in problem_id if char.isalnum())

    directory_content = os.listdir()

    largest = 0
    for element in directory_content:
        if '_' in element:
            underscore_location = element.find('_')
            dir_id = element[underscore_location + 1:]
            if dir_id == problem_id:
                print(f"Problem ID already exists ({element})")
                return
            numberpart = element[:underscore_location]
            if numberpart.isnumeric():
                num = int(element[:element.find('_')])
                largest = max(num, largest)
    id = largest + 1

    dirname = f"{id}_{problem_id}"

    os.makedirs(dirname)
    with open(os.path.join(dirname, "main.py"), "w") as f:
        f.write(
            f"""
import os

def solveProblem(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        pass

print(solveProblem("sample.txt"))
print("########################")
print(solveProblem("rosalind_{problem_id}.txt"))
            """
        )
    with open(os.path.join(dirname, "sample.txt"), "w"):
        pass
    with open(os.path.join(dirname, f"rosalind_{problem_id}.txt"), "w"):
        pass

if __name__ == "__main__":    
    generateTemplate()