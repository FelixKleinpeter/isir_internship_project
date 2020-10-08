# coding:utf-8

def fml_from_template(variable, filename, behaviour, question):
    output_string = """"""

    print(question)

    if question == -1:
        file_to_open = behaviour.lower()+"/"+filename
    else:
        file_to_open = behaviour.lower()+"/q"+str(question)+".xml"
    with open("behaviour/templates/"+file_to_open,"r") as f:
        lines = f.readlines()

    for line in lines:
        if line.strip() == "*":
            output_string += variable
        else:
            output_string += line

    with open("output/"+filename,"w") as f:
        f.write(output_string)
