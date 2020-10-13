# coding:utf-8

def fml_from_template(variable, filename, behaviour, question, username = ""):
    output_string = """"""

    if question == -1:
        file_to_open = behaviour.lower()+"/"+filename
    elif question >= 9:
        file_to_open = behaviour.lower()+"/q"+str(9)+".xml"
    else:
        file_to_open = behaviour.lower()+"/q"+str(question+1)+".xml"
    with open("behaviour/templates/"+file_to_open,"r") as f:
        lines = f.readlines()

    for line in lines:
        if line.strip() == "*":
            output_string += variable
        elif line.strip() == "USERNAME":
            output_string += username
        else:
            output_string += line

    with open("output/"+filename,"w") as f:
        f.write(output_string)
