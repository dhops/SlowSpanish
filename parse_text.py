import re

def extract_names_and_texts(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Regex to find all occurrences of names in brackets and the following text
    pattern = re.compile(r'\[([^\]]+)\](.*?)(?=\[|$)', re.DOTALL)
    matches = pattern.findall(content)

    names = []
    texts = []

    for match in matches:
        names.append(match[0])
        texts.append(match[1].strip())

    return names, texts

# Example usage
filename = 'leyenda.txt'
names, texts = extract_names_and_texts(filename)

print("Names:")
print(names)
print("\nTexts:")
print(texts)
