context = input("--- Context: \n")

objectiv = input("--- Objectiv: \n")

style = input("--- Style (default will be: 'Follow the writing style of successful companies that are experts in dev/devops, such as AWS, Google Cloud, and Microsoft Azure.'): \n")
if style == "":
    style = "Follow the writing style of successful companies that are experts in dev/devops, such as AWS, Google Cloud, and Microsoft Azure."

tone = input("--- Tone (default will be: 'Professional, technical'): \n")
if tone == "":
    tone = "Professional, technical"

audience = input("--- Audience (default will be: 'Devops engineers and developers who are interested in learning about the latest technologies and best practices.'): \n")
if audience == "":
    audience = "Devops engineers and developers who are interested in learning about the latest technologies and best practices."

response = input("--- Response (default will be: 'Defaul response'): \n")
if response == "":
    response = "Defaul response"

codesSnippets = []
wantCodeSnippet = input("--- Do you want to add a code snippet? (y/n): \n")
while wantCodeSnippet == "y":
    codeSnippetFile = input("--- Code snippet file: \n")
    codeLines = []
    print("--- Type the code snippet (type 'END' to finish):")
    while True:
        line = input()
        if line == "END":
            break
        codeLines.append(line)
    
    codeSnippet = '\n'.join(codeLines)
    codesSnippets.append({
        "file": codeSnippetFile,
        "code": codeSnippet
    })
    wantCodeSnippet = input("--- Do you want to add another code snippet? (y/n): \n")

prompt = f"""
### CONTEXT ###

{context}

###############

### OBJECTIVE ###

{objectiv}

################

### STYLE ###

{style}

###############

### TONE ###

{tone}

###############

### AUDIENCE ###

{audience}

################

### RESPONSE ###

{response}

################
"""

if len(codesSnippets) > 0:
    prompt += "### CODE SNIPPETS ###\n"
    for codeSnippet in codesSnippets:
        prompt += f"""
{codeSnippet['file']}
```
{codeSnippet['code']}
```\n
        """
    prompt += "\n################"

print(prompt)
