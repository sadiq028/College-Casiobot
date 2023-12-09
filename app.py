import re
from flask import Flask, render_template, url_for, redirect, request, flash
import csv
import speech_recognition as sr
import requests
import os
import telepot
r = sr.Recognizer()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/college_info')
def college_info():
    return render_template('info.html')

@app.route('/Main')
def Main():
    return render_template('main.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/second')
def second():
    return render_template('secondfloor.html')

@app.route('/third')
def third():
    return render_template('thirdfloor.html')

@app.route('/departments')
def departments():
    return render_template('departments.html')

@app.route('/tour')
def tour():
    return render_template('tour.html')

@app.route('/sections/<Name>')
def sections(Name):
    path = 'static/images/'+Name
    List = os.listdir(path)
    img=[]
    for i in List:
        img.append('http://127.0.0.1:5000/static/images/'+Name+'/'+i)
    return render_template('main.html', img=img, head=Name)

@app.route('/aiml/<Name>')
def aiml(Name):
    path = 'static/images/Departments/'+Name
    List = os.listdir(path)
    img=[]
    for i in List:
        img.append('http://127.0.0.1:5000/static/images/Departments/'+Name+'/'+i)
    return render_template('departments.html', img=img,  head=Name)

@app.route('/ise/<Name>')
def ise(Name):
    print(Name)
    # path = 'static/images/Departments/'+Name
    # List = os.listdir(path)
    # img=[]
    # for i in List:
    #     img.append('https://cranessoftware0-my.sharepoint.com/:f:/g/personal/shareef_cranessoftware_com/EoxvruK6vh9NqkAJgG3oAZUBCZb-7QikL0FIclXjJn7gEg?e=o7mjAg/'+Name+'/'+i)
    return render_template('sub_departs.html')#, img=img, head=Name)

@app.route('/classrom/<Name>')
def classrom(Name):
    path = 'static/images/Departments/ISE/'+Name
    List = os.listdir(path)
    img=[]
    for i in List:
        img.append('http://127.0.0.1:5000/static/images/Departments/ISE/'+Name+'/'+i)
    return render_template('sub_departs.html', img=img, head=Name)

@app.route('/secondfloor/<Name>')
def secondfloor(Name):
    path = 'static/2nd_floor/'+Name
    List = os.listdir(path)
    img=[]
    for i in List:
        img.append('http://127.0.0.1:5000/static/2nd_floor/'+Name+'/'+i)
    return render_template('secondfloor.html', img=img, head=Name)

@app.route('/thirdfloor/<Name>')
def thirdfloor(Name):
    path = 'static/3rd_floor/'+Name
    List = os.listdir(path)
    img=[]
    for i in List:
        img.append('http://127.0.0.1:5000/static/3rd_floor/'+Name+'/'+i)
    return render_template('thirdfloor.html', img=img, head=Name)
    
@app.route('/notice')
def notice():
    try:
        TOKEN = "6183587922:AAEN4Lut72SSeYVG7pfWrKabv3SfrTHSnLI"
        bot=telepot.Bot(TOKEN)
        url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=-1"
        Text = None

        message = requests.get(url).json()
        try:
            Text = message['result'][0]['message']['text']
            print(Text)
            return render_template('notice.html', message=Text)
        except:
            file_id = message['result'][0]['message']['photo'][0]['file_id']
            bot.download_file(file_id, 'static/image2.jpg')
            print('image received')
            return render_template('notice.html', image='static/image2.jpg')
    except:
        return render_template('notice.html', message='WELCOME')

@app.route('/voice')
def voice():
    return render_template('voice.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

@app.route('/demo')
def demo():
    while True:
        print('speak')
        try:
                with sr.Microphone() as source2:
                        r.adjust_for_ambient_noise(source2)
                        audio2 = r.listen(source2)
                        MyText = r.recognize_google(audio2)
                        MyText = MyText.lower()
                        print("Did you say "+MyText)
                        if MyText:
                            break

        except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
                print("unknown error occured")

    File=''
    rows=[]
    Sem = None
    if '1st sem' in MyText or 'first sem' in MyText:
        Sem = '1st'
    if '2nd sem' in MyText or 'second sem' in MyText:
        Sem = '2nd'
    if '3rd sem' in MyText or 'thired sem' in MyText:
        Sem = '3rd'
    if '4th sem' in MyText or 'fourth sem' in MyText:
        Sem = '4th'
    if '5th sem' in MyText or 'fifth sem' in MyText:
        Sem = '5th'
    if '6th sem' in MyText or 'sixth sem' in MyText:
        Sem = '6th'
    if '7th sem' in MyText or 'seventh sem' in MyText:
        Sem = '7th'
    if '8th sem' in MyText or 'eighth sem' in MyText:
        Sem = '8th'

    if not(Sem is None):
        if 'advertisement' in MyText:
            path = 'static/'+Sem+'/advertisment'
            video = []
            for i in os.listdir(path):
                video.append('http://127.0.0.1:5000/static/'+Sem+'/advertisment/'+i)
            return render_template('voice.html', videos=video)
        
        if 'internal' in MyText:
            path = 'static/'+Sem+'/internal_time_table'
            images = []
            for i in os.listdir(path):
                images.append('http://127.0.0.1:5000/static/'+Sem+'/internal_time_table/'+i)
            return render_template('voice.html', images=images)

        if 'calendar' in MyText:
            path = 'static/'+Sem+'/calender'
            docs = []
            for i in os.listdir(path):
                docs.append('http://127.0.0.1:5000/static/'+Sem+'/calender/'+i)
            return render_template('voice.html', docs=docs)
        
        if 'class' in MyText:
            path = 'static/'+Sem+'/class_time_table'
            images = []
            for i in os.listdir(path):
                images.append('http://127.0.0.1:5000/static/'+Sem+'/class_time_table/'+i)
            return render_template('voice.html', images=images)

        if 'vtu' in MyText:
            path = 'static/'+Sem+'/vtu_time_table'
            images = []
            for i in os.listdir(path):
                images.append('http://127.0.0.1:5000/static/'+Sem+'/vtu_time_table/'+i)
            return render_template('voice.html', images=images)
        
        if 'subject' in MyText:
            path = 'static/'+Sem+'/subject'
            docs = []
            for i in os.listdir(path):
                docs.append('http://127.0.0.1:5000/static/'+Sem+'/subject/'+i)
            return render_template('voice.html', docs=docs)

        if 'student' in MyText:
            path = 'static/'+Sem+'/student_list'
            docs = []
            for i in os.listdir(path):
                docs.append('http://127.0.0.1:5000/static/'+Sem+'/student_list/'+i)
            return render_template('voice.html', docs=docs)
        
        if 'result' in MyText:
            path = 'static/'+Sem+'/result'
            docs = []
            for i in os.listdir(path):
                docs.append('http://127.0.0.1:5000/static/'+Sem+'/result/'+i)
            return render_template('voice.html', docs=docs)
            
        if 'general' in MyText:
            path = 'static/'+Sem+'/general_circuler'
            docs = []
            for i in os.listdir(path):
                docs.append('http://127.0.0.1:5000/static/'+Sem+'/general_circuler/'+i)
            return render_template('voice.html', docs=docs)
        if 'project' in MyText:
            path = 'static/'+Sem+'/co-ordinator'
            docs = []
            for i in os.listdir(path):
                docs.append('http://127.0.0.1:5000/static/'+Sem+'/co-ordinator/'+i)
            return render_template('voice.html', docs=docs)
        if 'classroom' in MyText:
            path = 'static/'+Sem+'/smartroom'
            docs = []
            for i in os.listdir(path):
                docs.append('http://127.0.0.1:5000/static/'+Sem+'/smartroom/'+i)
            return render_template('voice.html', docs=docs)
        else:
            return render_template('voice.html', message='Result not found, Try again')
    else:
        if MyText == 'hod' or MyText == 'h o d':
            return render_template('voice.html', images=['http://127.0.0.1:5000/static/images/hod.jpg'])
        if MyText == 'principal' or MyText == 'principle':
            return render_template('voice.html', images=['http://127.0.0.1:5000/static/images/hodprincipal.jpg'])
        if MyText == 'internship coordinator' or MyText == 'internship co ordinator' or MyText == 'internship co-ordinator':
            return render_template('voice.html', images=['http://127.0.0.1:5000/static/images/internship_coordinator.jpg'])
        if MyText == 'project coordinator' or MyText == 'project co ordinator' or MyText == 'project co-ordinator':
            return render_template('voice.html', images=['http://127.0.0.1:5000/static/images/project_coordinator.jpg'])
        if MyText == 'seminor coordinator' or MyText == 'seminor co ordinator' or MyText == 'seminar co-ordinator':
            return render_template('voice.html', images=['http://127.0.0.1:5000/static/images/seminor_coordinator.jpg'])
        if MyText == 'internship coordinator' or MyText == 'internship co ordinator' or MyText == 'internship co-ordinator':
            return render_template('voice.html', images=['http://127.0.0.1:5000/static/images/internship_coordinator.jpg'])
        else:
            return render_template('voice.html', message = 'Result not found, Try again')
        
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
