# coding:utf-8

import random as rd
from math import ceil


def xml_from_question(question, filename, behaviour):

    # =========== SPEECH PART ===========
    words = question.split()
    output_string = """<?xml version="1.0" encoding="ISO-8859-1" ?>
    <fml-apml>
    	<bml>
    		<speech id="s1" start="0.0" language="english" voice="marytts" type="SAPI4" text="">
    			<description level="1" type="gretabml">
    				<reference>tmp/from-fml-apml.pho</reference>
    			</description>
                """
    t = len(words)
    w = [(int(t*k/4),int(t*(k+1)/4)-1) for k in range(4)]
    for i, ids in enumerate(w):
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
    	<fml>"""

    # =========== GESTURE PART ===========
    pool = [("deictic", "selftouch"), ("performative", "suggest"), ("performative", "rythm"), ("performative", "suggest"), ("beat", "left"), ("beat", "right")]

    splits = min([len(words) // 10, 5])
    segments = [ceil(5 / i) for i in range(1, splits+1)]
    segments += [1]
    segments.reverse()

    if behaviour == "WARM":
        output_string += """
            <emotion id="e1" type="joyStrong" start="s1:tm0" end="s1:tm4" importance="1.0"/>
            <emotion id="e2" type="small_joy" start="s1:tm4" end="s1:tm5+30" importance="1.0"/>
        """
    for i in range(len(segments) - 1):
        output_string += sentence_from_pool(pool, str(i+1), "tm"+str(segments[i]), "tm"+str(segments[i+1]))
    output_string += """
    	</fml>
    </fml-apml>
    """

    with open("output/"+filename,"w") as f:
        f.write(output_string)

def sentence_from_gesture(gesture_type, gesture, id, start, end):
    return "\n\t<" + gesture_type + " id=\"" + id + "\" type=\"" + gesture + "\" start=\"s1:" + start + "\" end=\"s1:" + end + "\" importance=\"1.0\"/>"

def sentence_from_pool(gesture_pool, id, start, end):
    chosen_gesture = gesture_pool[rd.randint(0, len(gesture_pool))-1]
    return sentence_from_gesture(chosen_gesture[0], chosen_gesture[1], id, start, end)
