"""
File: Inside Out
Name: Monica Peng
----------------------
Using different shapes to compose a drawing of inside out.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow

# Set the width and height of window
WINDOW_WIDTH = 680
WINDOW_HEIGHT = 400
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='Disney Pixar Presents')


def main():
    """
    Title: INSIDE OUT

    This is one of my favourite Disney animations.
    There are five different characters:
    Fear, Anger, Joy, Sadness and Disgust (L-R).
    """
    background()
    fear()
    anger()
    joy()
    sadness()
    disgust()
    title()


def title():
    label = GLabel('INSIDE')
    label.font = 'Cooper Black-45'
    label.color = 'white'
    window.add(label, (window.width-label.width)/2, label.height+20)
    label2 = GLabel('OUT')
    label2.font = 'Cooper Black-50'
    label2.color = 'white'
    window.add(label2, (window.width - label2.width) / 2, label.height+label2.height + 20)

    label3 = GLabel('MEET THE LITTLE VOICES INSIDE YOUR HEAD.')
    label3.font = 'Arial Rounded MT Bold-13'
    label3.color = 'white'
    window.add(label3, (window.width - label3.width) / 2, window.height-20)


def disgust():
    # Define the colors
    face_c = '#bce474'
    hair_c = '#336c09'
    body_c = '#4d9860'
    neck_c = '#a9759c'
    shadow_c = '#172b04'

    shadow = GRect(50, 53)
    shadow.filled = True
    shadow.fill_color = shadow_c
    shadow.color = shadow_c
    window.add(shadow, x=485, y=190)

    face = GOval(50, 53)
    face.filled = True
    face.fill_color = face_c
    face.color = face_c
    window.add(face, x=485, y=190)

    hair1 = GRect(shadow.width, shadow.height*0.35)
    hair1.filled = True
    hair1.fill_color = hair_c
    hair1.color = hair_c
    window.add(hair1, shadow.x, shadow.y)

    hair2 = GRect(5, shadow.height)
    hair2.filled = True
    hair2.fill_color = hair_c
    hair2.color = hair_c
    window.add(hair2, shadow.x, shadow.y)

    hair2 = GRect(5, shadow.height)
    hair2.filled = True
    hair2.fill_color = hair_c
    hair2.color = hair_c
    window.add(hair2, shadow.x+shadow.width-5, shadow.y)

    body = GPolygon()
    body.add_vertex((shadow.x+shadow.width/2, shadow.y+shadow.height+1))
    body.add_vertex((shadow.x, 315))
    body.add_vertex((shadow.x+shadow.width, 315))
    body.filled = True
    body.fill_color = body_c
    body.color = body_c
    window.add(body)

    neck = GPolygon()
    neck.add_vertex((shadow.x + shadow.width / 2, shadow.y + shadow.height + 1))
    neck.add_vertex((shadow.x + shadow.width / 2 -3, shadow.y+ shadow.height+8))
    neck.add_vertex((shadow.x + shadow.width / 2 +3, shadow.y+ shadow.height+8))
    neck.filled = True
    neck.fill_color = neck_c
    neck.color = neck_c
    window.add(neck)


def sadness():
    # Define the colors
    face_c = '#86b7ec'
    body_c = '#cfdee3'
    bottom_c = '#304890'
    hair_c = '#3f6ec2'

    hair = GOval(72, 72)
    hair.filled = True
    hair.fill_color = hair_c
    hair.color = hair_c
    window.add(hair, x=385, y=220)

    face = GOval(60, 60)
    face.filled = True
    face.fill_color = face_c
    face.color = face_c
    window.add(face, x=395, y=230)

    body = GRect(70, 55)
    body.filled = True
    body.fill_color = body_c
    body.color = body_c
    window.add(body, x=386, y=262)

    bottom = GRect(70, 25)
    bottom.filled = True
    bottom.fill_color = bottom_c
    bottom.color = bottom_c
    window.add(bottom, body.x, body.y+body.height)

    left_lens = GOval(23, 23)
    window.add(left_lens, x=396, y=234)

    right_lens = GOval(23, 23)
    window.add(right_lens, left_lens.x+left_lens.width, left_lens.y)


def joy():
    # Define the colors
    face_c = '#f3dd9b'
    bottom_c = '#eff68e'
    hair_c = '#5781cd'

    face = GOval(45, 45)
    face.filled = True
    face.fill_color = face_c
    face.color = face_c
    window.add(face, x=307.5, y=150)

    bottom = GPolygon()
    bottom.add_vertex((330, 210))
    bottom.add_vertex((290, 315))
    bottom.add_vertex((370, 315))
    bottom.filled = True
    bottom.fill_color = bottom_c
    bottom.color = bottom_c
    window.add(bottom)

    hair = GPolygon()
    hair.add_vertex((307.5, 180))
    hair.add_vertex((317, 162))
    hair.add_vertex((332, 166))
    hair.add_vertex((336, 163))
    hair.add_vertex((337, 164))
    hair.add_vertex((352.5, 180))
    hair.add_vertex((351, 158))
    hair.add_vertex((340, 152))
    hair.add_vertex((335, 150))
    hair.add_vertex((330, 150))
    hair.add_vertex((325, 150))
    hair.add_vertex((320, 152))
    hair.add_vertex((309, 158))
    hair.add_vertex((307.5, 180))

    hair.filled = True
    hair.fill_color = hair_c
    hair.color = hair_c
    window.add(hair)


def anger():
    # Define the colors
    face_c = '#d22322'
    body_c = '#eee5d5'
    bottom_c = '#7b585e'
    tie_c = '#6f3a39'

    width = 70
    height = 30

    face = GRect(width, height)
    face.filled = True
    face.fill_color = face_c
    face.color = face_c
    window.add(face, x=205, y=250)

    body = GRect(width, height)
    body.filled = True
    body.fill_color = body_c
    body.color = body_c
    window.add(body, face.x, face.y+height)

    bottom = GRect(width, height)
    bottom.filled = True
    bottom.fill_color = bottom_c
    bottom.color = bottom_c
    window.add(bottom, body.x, body.y+height)

    tie = GPolygon()
    tie.add_vertex((body.x+width/2, body.y+1))
    tie.add_vertex((body.x+width/2-3, body.y+3))
    tie.add_vertex((body.x + width / 2, body.y + 6))
    tie.add_vertex((body.x + width / 2 + 3, body.y + 3))
    tie.filled = True
    tie.fill_color = tie_c
    tie.color = tie_c
    window.add(tie)

    tie_lower = GPolygon()
    tie_lower.add_vertex((body.x + width / 2, body.y + 6))
    tie_lower.add_vertex((body.x + width / 2 - 6, body.y + 22))
    tie_lower.add_vertex((body.x + width / 2, body.y + 28))
    tie_lower.add_vertex((body.x + width / 2 + 6, body.y + 22))
    tie_lower.filled = True
    tie_lower.fill_color = tie_c
    tie_lower.color = tie_c
    window.add(tie_lower)


def fear():
    # Define the colors
    face_c = '#a98fde'
    body_c = '#d5d3d3'
    bottom_c = '#372e5b'
    bowtie_c = '#5b1c3c'

    face = GRect(20, 30)
    face.filled = True
    face.fill_color = face_c
    face.color = face_c
    window.add(face, x=155, y=155)

    body = GRect(20, 80)
    body.filled = True
    body.fill_color = body_c
    body.color = body_c
    window.add(body, x=155, y=190)

    bottom = GRect(20, 45)
    bottom.filled = True
    bottom.fill_color = bottom_c
    bottom.color = bottom_c
    window.add(bottom, x=155, y=270)

    left_bowtie = GPolygon()
    left_bowtie.add_vertex((152, 188))
    left_bowtie.add_vertex((152, 200))
    left_bowtie.add_vertex((164, 194))
    left_bowtie.filled = True
    left_bowtie.fill_color = bowtie_c
    left_bowtie.color = bowtie_c
    window.add(left_bowtie)

    right_bowtie = GPolygon()
    right_bowtie.add_vertex((178, 188))
    right_bowtie.add_vertex((178, 200))
    right_bowtie.add_vertex((166, 194))
    right_bowtie.filled = True
    right_bowtie.fill_color = bowtie_c
    right_bowtie.color = bowtie_c
    window.add(right_bowtie)

    ctr_bowtie = GOval(10, 10)
    ctr_bowtie.filled = True
    ctr_bowtie.fill_color = bowtie_c
    ctr_bowtie.color = bowtie_c
    window.add(ctr_bowtie, x=160, y=189)

    hair = GPolygon()
    hair.add_vertex((165, 150))
    hair.add_vertex((168, 155))
    hair.add_vertex((167, 157))
    hair.color = 'white'
    window.add(hair)


def background():

    # Define the colors used in the drawings
    bg_upper_c = '#04245d'
    bg_lower_c = '#0e3673'
    bg_circle_c_1 = '#49233c'
    bg_circle_c_2 = '#3c6fa8'
    bg_circle_c_3 = '#4e3680'
    bg_circle_c_4 = '#7c8e52'
    bg_circle_c_5 = '#36367e'
    bg_circle_c_6 = '#3f732b'
    bg_circle_c_7 = '#20588b'

    # Create the background with the shapes
    bg_upper = GRect(width=window.width, height=window.height * 0.75)
    bg_upper.filled = True
    bg_upper.fill_color = bg_upper_c
    bg_upper.color = bg_upper_c
    window.add(bg_upper)

    bg_circle_2 = GOval(200, 200)
    bg_circle_2.filled = True
    bg_circle_2.fill_color = bg_circle_c_2
    bg_circle_2.color = bg_circle_c_2
    window.add(bg_circle_2, x=300, y=-70)

    bg_circle_1 = GOval(200, 200)
    bg_circle_1.filled = True
    bg_circle_1.fill_color = bg_circle_c_1
    bg_circle_1.color = bg_circle_c_1
    window.add(bg_circle_1, x=130, y=-50)

    bg_circle_3 = GOval(90, 90)
    bg_circle_3.filled = True
    bg_circle_3.fill_color = bg_circle_c_3
    bg_circle_3.color = bg_circle_c_3
    window.add(bg_circle_3, x=-10, y=120)

    bg_circle_4 = GOval(170, 170)
    bg_circle_4.filled = True
    bg_circle_4.fill_color = bg_circle_c_4
    bg_circle_4.color = bg_circle_c_4
    window.add(bg_circle_4, x=80, y=170)

    bg_circle_5 = GOval(165, 165)
    bg_circle_5.filled = True
    bg_circle_5.fill_color = bg_circle_c_5
    bg_circle_5.color = bg_circle_c_5
    window.add(bg_circle_5, x=250, y=180)

    bg_circle_6 = GOval(180, 180)
    bg_circle_6.filled = True
    bg_circle_6.fill_color = bg_circle_c_6
    bg_circle_6.color = bg_circle_c_6
    window.add(bg_circle_6, x=380, y=170)

    bg_circle_7 = GOval(85, 85)
    bg_circle_7.filled = True
    bg_circle_7.fill_color = bg_circle_c_7
    bg_circle_7.color = bg_circle_c_7
    window.add(bg_circle_7, x=550, y=30)

    bg_lower = GRect(width=window.width, height=window.height * 0.25)
    bg_lower.filled = True
    bg_lower.fill_color = bg_lower_c
    bg_lower.color = bg_lower_c
    window.add(bg_lower, x=0, y=window.height - bg_lower.height)


if __name__ == '__main__':
    main()
