file:str = "test.G"
file_lines:list = []
tokens = []
variables = {

}

with open(file, "r") as f:
    for line in f:
        line = line.strip()
        print(line)
        file_lines.append(line)

for line in file_lines:
    line_tokens = []
    current_token = ""
    for token in line:
        if token in (" ", "\t"):
            if current_token != "":
                line_tokens.append(current_token)
                current_token = ""
        else:
            current_token += token
    if current_token != "":
        line_tokens.append(current_token)
    if line_tokens != []:
        tokens.append(line_tokens)

for token in tokens:
    print(token)
    
    if token[1] == "=" and len(token) == 3:
        data = token[2]
        asm_type = None

        if (data.startswith('"') and data.endswith('"')) or (data.startswith("'") and data.endswith("'")):
            asm_type = "db"

        elif data.lower() in ("true", "false"):
            asm_type = "db"

        else:
            asm_type = "dq"

        # print("это переменая вот инфа о ней :" + "\n" + f"название переменой : {token[0]}" + "\n" + f"значение переменой : {token[2]}" + "\n" + f"тип переменой (asm тип) : {asm_type}")
        variables[token[0] + "_name"] = token[0]
        variables[token[0] + "_data"] = token[2]
        variables[token[0] + "_asm_type"] = asm_type
print(variables)

        

