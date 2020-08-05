# coding:utf-8

def xml_from_question(question, filename):
    words = question.split()
    output_string = """<?xml version="1.0" encoding="ISO-8859-1" ?>
    <fml-apml>
    	<bml>
    		<speech id="s1" start="0.0" language="english" voice="marytts" type="SAPI4" text="">
    			<description level="1" type="gretabml">
    				<reference>tmp/from-fml-apml.pho</reference>
    			</description>
                """
    for i, ids in enumerate([(0,1),(2,2),(3,3),(4,6)]):
        output_string += "\n\t"
        output_string += """<tm id="tm""" + str(i+1) + """"/>"""
        output_string += "\n\t\t"
        for w in words[ids[0]:ids[1]+1]:
            output_string += w + " "
    output_string += "\n\t"
    output_string += """<tm id="tm""" + str(i+2) + """"/>"""

    output_string += """
    			<pitchaccent id="pa2" type="HStar" level="medium" start="s1:tm3" end="s1:tm4" importance="1"/>
    			<boundary type="LL" id="b1" start="s1:tm5" end="s1:tm5+0.5"/>
    		</speech>
    	</bml>
    	<fml>
    		<deictic id="d1" type="selftouch" start="s1:tm2" end="s1:tm3" importance="1.0"/> <!-- target="Andre_chair0" -->
    		<performative id="p1" type="greet" start="s1:tm1" end="s1:tm2" importance="1.0"/>
    		<emotion id="e1" type="joyStrong" start="s1:tm2" end="s1:tm3" importance="1.0"/>
    		<performative id="p2" type="propose" start="s1:tm3" end="s1:tm5" importance="1.0"/>
    	</fml>
    </fml-apml>
    """

    with open("output/"+filename,"w") as f:
        f.write(output_string)
