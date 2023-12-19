from flask import Flask, render_template,json,request,redirect,url_for,send_file
from flask_restful import Resource, Api
import json, string, random, os
import flask
import webbrowser
import sys

app=Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/sample1',methods = ['GET', 'POST'])
def sample1():
    return render_template('sample1.html')

@app.route("/sample1card", methods=["POST"])
def sample1card():
    words=[]
    words.append("Save The Date")
    words.append("you are invited to the")
    words.append("Wedding of")
    
    Mobile = request.form.get("mobile")
    print(Mobile)
    UPI_ID = request.form.get("pa")
    print(UPI_ID)
    
    words.append(f"{Mobile} & {UPI_ID}")
    words.append("That Will Be Held On")
    Payee_name = request.form.get("pn")
    print(Payee_name)
    words.append(Payee_name)
    Amount = request.form.get("am")
    print(Amount)
    words.append(Amount)
    Transaction_Ref_ID = request.form.get("tr")
    print(Transaction_Ref_ID)
    words.append(Transaction_Ref_ID)
    Transaction_Note = request.form.get("tn")
    print(Transaction_Note)
    if len(Transaction_Note)>35:
        l1=Transaction_Note[:30]
        l2=Transaction_Note[30:len(Transaction_Note)]
        words.append(l1)
        words.append(l2)

    elif len(Transaction_Note)<30:
        words.append(Transaction_Note)
        words.append("............................")

    words.append("Reception to fallow")
    words.append("Togather with their family")


    print(words)


    from PIL import Image, ImageDraw, ImageFont

    # Open the image
    image = Image.open("static\sample1\My Invitation2 (21).jpeg")

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the font and size
    font = ImageFont.truetype("static\sample1\Ribbon-BF64d2471cd139f.otf", 300)

    i = 0
    c=0
    for word in words:
        print(c)
        if c==0:
            # font = ImageFont.truetype("Calaya-Italic-BF64abb5ba43439.otf", 120)
            x=500
            i=0
            
        if c==1:
            x=1050
            font = ImageFont.truetype("arial", 100)
        
        if c==2:
            x=1260
            font = ImageFont.truetype("static\sample1\Daylight.otf", 200)

        if c==3:
            x=1450
            i=0
            font = ImageFont.truetype("static\sample1\Ribbon-BF64d2471cd139f.otf", 500)
        if c==4:
            x=2100
            font = ImageFont.truetype("static\sample1\Fontspring-DEMO-betmrounded-italic.otf", 150)
            i=0
        if c==5:
            x=2400
            font = ImageFont.truetype("static\sample1\Myriad Pro Bold.ttf", 320)
        if c==6:
            x=2700
            font = ImageFont.truetype("static\sample1\Myriad Pro Bold.ttf", 170)
        if c==7:
            x=2930
            font = ImageFont.truetype("static\sample1\somethingdifferent-alvlm.otf", 150)
        if c==8:
            x=3130
            font = ImageFont.truetype("arial", 80)
        if c==9:
            x=3250
            font = ImageFont.truetype("arial", 55)
            
        if c==10:
            x=3450
            font = ImageFont.truetype("static\sample1\BobbersPersonalUseRegular-6YdjD.ttf", 200)
            
        if c==11:
            x=900
            font = ImageFont.truetype("arial", 100)
            
        text = word
        #-------------------Adjust this as needed
        y = x 

        # Define the text color
        text_color = (255, 255, 255)  # RGB color, in this case, white

        # Add text to the image
        text_width, text_height = draw.textsize(text, font)
        image_width, image_height = image.size
        text_x = (image_width - text_width) // 2
        text_y = y

        draw.text((text_x+i, text_y), text, fill=text_color, font=font)
        
        c=c+1
            
        

    #----------------Save the modified image

    filen=f"{Mobile}&{UPI_ID}"+".jpg"
    image.save(filen)

    #-----------------Close the image
    image.close()

    image_path=filen

    mimetype = 'image/jpeg'  

    return send_file(image_path, mimetype=mimetype, as_attachment=True)


@app.route('/sample2',methods = ['GET', 'POST'])
def sample2():
    return render_template('sample2.html')


@app.route("/sample2card", methods=["POST"])
def sample2card():
    words=[]
    words.append("Save The Date")

    Mobile = request.form.get("mobile")
    print(Mobile)
    UPI_ID = request.form.get("pa")
    print(UPI_ID)
    
    words.append(f"{Mobile}     {UPI_ID}")
    words.append("That Will Be Held On")
    Payee_name = request.form.get("pn")
    print(Payee_name)
    words.append(Payee_name)
    Amount = request.form.get("am")
    print(Amount)
    words.append(Amount)
    Transaction_Ref_ID = request.form.get("tr")
    print(Transaction_Ref_ID)
    words.append(Transaction_Ref_ID)
    Transaction_Note = request.form.get("tn")
    print(Transaction_Note)
    if len(Transaction_Note)>35:
        l1=Transaction_Note[:30]
        l2=Transaction_Note[30:len(Transaction_Note)]
        words.append(l1)
        words.append(l2)

    elif len(Transaction_Note)<30:
        words.append(Transaction_Note)
        words.append("............................")

    words.append("Reception to fallow")


    print(words)


    from PIL import Image, ImageDraw, ImageFont
    import codecs

    # Open the image
    image = Image.open("static\sample2\My Invitation2 (47).jpeg")

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the font and size
    font = ImageFont.truetype("static\sample2\Daylight.otf", 300)

    i = 0
    c=0
    for word in words:
        print(c)
        if c==0:
            x=500
            i=0
        if c==1:
            x=1650
            i=100
            font = ImageFont.truetype("static\sample2\Calaya-Italic-BF64abb5ba43439.otf", 300)
        if c==2:
            x=2100
            font = ImageFont.truetype("static\sample2\Fontspring-DEMO-betmrounded-italic.otf", 150)
            i=0
        if c==3:
            x=2400
            font = ImageFont.truetype("static\sample2\Myriad Pro Bold.ttf", 320)
        if c==4:
            x=2700
            font = ImageFont.truetype("static\sample2\Myriad Pro Bold.ttf", 170)
        if c==5:
            x=2930
            font = ImageFont.truetype("static\sample2\somethingdifferent-alvlm.otf", 150)
        if c==6:
            x=3130
            font = ImageFont.truetype("arial", 80)
        if c==7:
            x=3250
            font = ImageFont.truetype("arial", 55)
            
        if c==8:
            x=3450
            font = ImageFont.truetype("static\sample2\BobbersPersonalUseRegular-6YdjD.ttf", 200)
            
        text = word
        #-------------------Adjust this as needed
        y = x 

        # Define the text color
        text_color = (255, 255, 255)  # RGB color, in this case, white

        # Add text to the image
        text_width, text_height = draw.textsize(text, font)
        image_width, image_height = image.size
        text_x = (image_width - text_width) // 2
        text_y = y

        draw.text((text_x+i, text_y), text, fill=text_color, font=font)
        
        c=c+1

    #----------------Save the modified image
    filen=f"{Mobile}&{UPI_ID}"+".jpg"
    image.save(filen)
    #-----------------Close the image
    image.close() 

    image_path=filen

    mimetype = 'image/jpeg'

    return send_file(image_path, mimetype=mimetype, as_attachment=True)


@app.route('/sample3',methods = ['GET', 'POST'])
def sample3():
    return render_template('sample3.html')

@app.route("/sample3card", methods=["POST"])
def sample3card():
    words=[]
    Mobile = request.form.get("mobile")
    print(Mobile)
    UPI_ID = request.form.get("pa")
    print(UPI_ID)
    
    words.append(f"{Mobile}")
    words.append(f"{UPI_ID}")
    Payee_name = request.form.get("pn")
    print(Payee_name)
    words.append(Payee_name)
    Amount = request.form.get("am")
    print(Amount)
    words.append(Amount)
    Transaction_Ref_ID = request.form.get("tr")
    print(Transaction_Ref_ID)
    words.append(Transaction_Ref_ID)
    Transaction_Note = request.form.get("tn")
    print(Transaction_Note)
    if len(Transaction_Note)>35:
        l1=Transaction_Note[:30]
        l2=Transaction_Note[30:len(Transaction_Note)]
        words.append(l1)
        words.append(l2)

    elif len(Transaction_Note)<30:
        words.append(Transaction_Note)
        words.append("............................")

    words.append("Reception to fallow")


    print(words)

    from PIL import Image, ImageDraw, ImageFont
    import codecs

    # Open the image
    image = Image.open("static\sample3\My Invitation2 (20).jpeg")

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Define the font and size
    font = ImageFont.truetype("static\sample3\BobbersPersonalUseRegular-6YdjD.ttf", 400)

    i = 0
    c=0
    for word in words:
        print(c)
        if c==0:
            # font = ImageFont.truetype("COM4S_M.TTF", 120)
            x=1330
            i=0
        if c==1:
            x=1900
            i=0
        if c==2:
            x=2470
            font = ImageFont.truetype("static\sample3\Myriad Pro Bold.ttf", 200)
            i=140
        if c==3:
            x=2700
            font = ImageFont.truetype("arial", 120)
        if c==4:
            x=2850
            font = ImageFont.truetype("arial", 55)
        if c==5:
            x=2900
            font = ImageFont.truetype("arial", 55)
        if c==6:
            x=3050
            font = ImageFont.truetype("static\sample3\BobbersPersonalUseRegular-6YdjD.ttf", 150)

        text = word
        #-------------------Adjust this as needed
        y = x 

        # Define the text color
        text_color = (255, 255, 255)  # RGB color, in this case, white

        # Add text to the image
        text_width, text_height = draw.textsize(text, font)
        image_width, image_height = image.size
        text_x = (image_width - text_width) // 2
        text_y = y

        draw.text((text_x+i, text_y), text, fill=text_color, font=font)
        
        c=c+1
            
        

    #----------------Save the modified image
    filen=f"{Mobile}&{UPI_ID}"+".jpg"
    image.save(filen)

    #-----------------Close the image
    image.close()

    image_path=filen

    mimetype = 'image/jpeg'  

    return send_file(image_path, mimetype=mimetype, as_attachment=True)


    
app.run(debug=True)