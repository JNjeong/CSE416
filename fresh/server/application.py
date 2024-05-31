from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests, sys, json, random, re

import os
import schedule
import time

application = Flask(__name__)

@application.route('/menu', methods=["POST"])
def index():
    req = request.get_json()
    params = req['action']['detailParams']

    if 'sys_date' not in params and 'sys_number' not in params.keys():
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "잘못입력함"
                        }
                    }
                ]
            }
        }
        
    elif 'sys_number' in params.keys():
        url = "https://housing.igc.or.kr/about/cafeteria_menu.do?c_date=2024-"
        if 'sys_number1' in params.keys():
            month = month = params['sys_number']['origin']
            day = params['sys_number1']['origin']
            url = url + month +"-"+ day
        else : 
            mid = len(params['sys_number']['origin'])//2
            month = params['sys_number']['origin'][:mid]
            day = params['sys_number']['origin'][mid:]
            url = url + month +"-"+ day
            
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    
        dl_elements = []
        list_wrap_divs = soup.find_all('div', class_='list_wrap')
    
        for list_wrap_div in list_wrap_divs:
            dl_elements += list_wrap_div.find_all('dl')
        dl_strings = []
        for dl in dl_elements:
            dt_dd_pairs = dl.find_all(['dt', 'dd'])
            dt_dd_strings = []
            for i in range(0, len(dt_dd_pairs), 2):
                dt_text = dt_dd_pairs[i].get_text(strip=True)
                dd_text = dt_dd_pairs[i+1].get_text(strip=True)
                dt_dd_strings.append(f'{dt_text}\n{dd_text}')
            dl_strings.append('\n\n'.join(dt_dd_strings))
            
        month = params['sys_number']['origin'][:2]
        day = params['sys_number']['origin'][-2:]
        if not dl_strings:
                dl_strings.append("No Operation on " + month +" "+day)
            
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": '\n'.join(dl_strings)
                        }
                    }
                ]
            }
        }
        
    
    else :
        rkey = ""
        rvalue = ""
        for key, value in params.items(): 
            rkey += key + " " 
            rvalue += str(value) + " "
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": params['sys_date']['origin']
                        }
                    }
                ]
            }
        }
        
    return jsonify(response)

@application.route("/webhook/", methods=["POST"])
def webhook():
    request_data = request.json
    call_back = requests.post(request_data['callback_url'], json={
        "version": "2.0", "template": { "outputs": [{
            "simpleText": {"text": request_data['result']['choices'][0]['message']['content']}
        }]}})
    print(call_back.status_code, call_back.json())
    return 'OK'
@application.route("/question", methods=["POST"])
def call_openai_api():
    user_request = request.json.get('userRequest', {})
    callback_url = user_request.get('callbackUrl')
    try:
        api = requests.post('https://api.asyncia.com/v1/api/request/', json={
            "apikey": "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",
            "messages" :[{"role": "user", "content": user_request.get('utterance', '')}],
            "userdata": [["callback_url", callback_url]]},
            headers={"apikey":"A0.2462d323-043e-42aa-9a4a-4f7fb19a936c.WqZI2W5x3tDlQj9QeSy--5R5oyb2QrfWKg"}, timeout=2)
    except requests.exceptions.ReadTimeout:
        pass    
    return jsonify({
      "version" : "2.0",
      "useCallback" : True
    })

@application.route("/random", methods=["POST"])
def random_function():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": str(random.randint(1, 10))
                    }
                }
            ]
        }
    }
    return jsonify(response)

@application.route("/jihoon", methods=["POST"])
def professor_information():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "Prof. Jihoon Ryoo,\nemail : jihoon.ryoo@sunykorea.ac.kr,\nOffice : C413,\nOffice hours: Tuesday/Thursday 2:00 - 3 PM or by appointment if necessary"
                    }
                }
            ]
        }
    }
    return jsonify(response)

@application.route("/welcome", methods=["POST"])
def welcomeblock():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": "SUNY Korea Chatbot",
                        "description": "Welcome to our channel! Here are our features:",
                        "thumbnail": {
                            "imageUrl": "welcom.jpeg"
                        },
                        "buttons": [
                            {
                                "action": "message",
                                "label": "Course Info",
                                "messageText": "You can enter the name of the course, the lecture title, or just numbers to check the credits, prerequisites, textbook, major topics, etc. of the corresponding course."
                            },
                            {
                                "action":  "message",
                                "label": "Professor Info",
                                "messageText": "You can find out the professor's department, email, office, office hours, etc."
                            },
                            {
                                "action":  "message",
                                "label": "School Map",
                                "messageText": "You can check a simple map of the school"
                            },
                            {
                                "action":  "message",
                                "label": "IGC Cafeteria Menu",
                                "messageText": "You can enter the date with menu(ex : 0409menu), to find out the meal menu at the IGC cafeteria."
                            },
                            {
                                "action":  "message",
                                "label": "Degree Work",
                                "messageText": "Not yet"
                            },
                            {
                                "action":  "message",
                                "label": "ChatGPT answers",
                                "messageText": "If you ask a question that we don't know, you will be automatically connected to ChatGPT to help you with the answer."
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)


@application.route("/AMS126", methods=["POST"])
@application.route("/CSE416", methods=["POST"])
@application.route("/CSE114", methods=["POST"])
def course_information():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": "CSE114",
                        "description": "An introduction to procedural and object-oriented programming methodology. Topics include program structure, conditional and iterative programming, procedures, arrays and records, object classes, encapsulation, information hiding, inheritance, polymorphism, file I/O, and exceptions. Includes required laboratory. This course has been designated as a High Demand/Controlled Access (HD/CA) course. Students registering for HD/CA courses for the first time will have priority to do so.",
                        "thumbnail": {
                            "imageUrl": "cse114.png"
                        },
                        "buttons": [
                            {
                                "action": "message",
                                "label": "Prerequisite",
                                "messageText": "Prerequisites: Level 5 or higher on the math placement exam Advisory Prerequisite: CSE101 or ISE108"
                            },
                            {
                                "action":  "message",
                                "label": "Textbook",
                                "messageText": "Allen B. Downey and Chris Mayfield, Think Java: How to Think Like a Computer Scientist, 2nd Edition, ISBN: 9781491929551"
                            },
                            {
                                "action":  "message",
                                "label": "Major Topics",
                                "messageText": "1.Introduction to Objects in Java, using predefined objects (e.g. String) 2.Review of program control statements: conditionals and loops with an introduction to formal methods (preconditions, post conditions, loop invariant) 3.Writing more complex classes. 4.Arrays and the ArrayList class. 5.Inheritance and polymorphism in Java, simple examples, the Java class hierarchy. 6.Exceptions and File I/O. 7.Introduction to graphical user interface components. 8.Recursive programming, basic examples (factorial, Fibonacci numbers, Towers of Hanoi, etc...) 9.Documenting sources of code, effects of software piracy on business and individuals"                         }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)

@application.route("/vrtour", methods=["POST"])
def vrtour():
    response = {
        "version":"2.0",
        "template" : {
            "outputs" : [
                {
                    "basicCard" : {
                        "title" : "VR Tour",
                        "description" : "VISIT : https://www.igc.or.kr/vr/indexe.html"
                    }
                }
            ]
        }
       
    }
    return jsonify(response)

major_requirements = {
    "computer science" : "Common Requirement(SBC) : ARTS, GLO, HUM, QPS, SBS, SNW, TECH, USA, WRT, STAS, EXP+, SBS+, STEM+, CER, DIV, ESI, SPK, WRTD\n\nIntroductory(CSE114,CSE214,CSE215,CSE216,CSE220)\nAdvanced(CSE303,CSE310,CSE316,CSE320,CSE373,CSE416\n4 upper-division CSE electives 300 above\nElectives(One of AMS151/AMS161, Both AMS301,AMS310)\nScience(One of BIO201/202/203/204, CHE131/133/152/154, PHY126/127/131/133/141, AST203/205,CHE132/321/322/331/332,GEO102/103/112/113/122,PHY125/132/134/142/251/252))",
    "applied mathematics and statistics" : "Common Requirement(SBC) : ARTS, GLO, HUM, QPS, SBS, SNW, TECH, USA, WRT, STAS, EXP+, SBS+, STEM+, CER, DIV, ESI, SPK, WRTD\n\nRequired(AMS151/161, AMS210/MAT211, AMS261/MAT203)\nComputing(AMS326,CSE101/114,ESG111)\nUpper Divisions(AMS301, One of AMS310/AMS311, One of AMS315/361/MAT303, 6 AMS courses numbered 301 above)\nUpper Writing(AMS300)",
    "business management" : "Common Requirement(SBC) : ARTS, GLO, HUM, QPS, SBS, SNW, TECH, USA, WRT, STAS, EXP+, SBS+, STEM+, CER, DIV, ESI, SPK, WRTD\n\nCore(ACC210/214,BUS215/220/301/326/330/346/348/353/446,ECO108, One of MAT112/119/123)\nOne of any Specialization('Accounting':ACC310/311,one of ACC313/314/400/BUS488, 'Finance':four of BUS317/331/332/336/355/356/365/366/376/ECO383/BUS406/488, 'Marketing':BUS358/359/448,one of BUS302/334/335/357/360/362/363/378/449/488, 'Operations Management':BUS340,three of BUS370/371/372/375/393/488)\nUpper Writing(BUS301)",
    "electrical and computer engineering" : "Common Requirement(SBC) : ARTS, GLO, HUM, QPS, SBS, SNW, TECH, USA, WRT, STAS, EXP+, SBS+, STEM+, CER, DIV, ESI, SPK, WRTD\n\nIntroductory(ESE123/124)\nCore(ESE118/224/271/272/280/305/306/315/319/323/324/331/342)\nOne of any Specialization('Circuits and VSLI':ESE330/411, 3 technical electives, 'Communications, Signal Processing, and Networking':ESE337,one of ESE346/442, 3 technical electives), 'Nanoelectronics and Photonics':ESE332/334,3 technical electives, 'Power and Energy Systems':ESE350/451, 3 technical electives\nDesign(ESE440/441)\nUpper Writing(ESE300)\nEngineering Ethics(ESE301)\nScience(One of BIO201/202/203/204, CHE131/133/152/154, PHY126/127/131/133/141, AST203/205,CHE132/321/322/331/332,GEO102/103/112/113/122,PHY125/132/134/142/251/252)\nMathematics(one of AMS151/161, one of AMS261/MAT203, one of AMS361/MAT303, one of AMS201/MAT211)",
    "mechanical engineering" : "Common Requirement(SBC) : ARTS, GLO, HUM, QPS, SBS, SNW, TECH, USA, WRT, STAS, EXP+, SBS+, STEM+, CER, DIV, ESI, SPK, WRTD\n\nCore(MEC101/102/203/220/225/260/262/301/305/325/363/364)\nLaboratories(MEC316/317)\nMaterials Science(ESG332)\nEngineering Design(MEC310/320/410/411/422/440/411)\nEngineering Economics(EST392)\nTechnical Electives(3 technical electives)\nUpper Writing(MEC300)\nScience(One of BIO201/202/203/204, CHE131/133/152/154, PHY126/127/131/133/141, AST203/205,CHE132/321/322/331/332,GEO102/103/112/113/122,PHY125/132/134/142/251/252)\nMathematics(one of AMS151/161, one of AMS261/MAT203, one of AMS361/MAT303, one of AMS201/MAT211)",
    "technology and society" : "Common Requirement(SBC) : ARTS, GLO, HUM, QPS, SBS, SNW, TECH, USA, WRT, STAS, EXP+, SBS+, STEM+, CER, DIV, ESI, SPK, WRTD\n\nCore(EST194/202/304/331/391/392/393/440/441, one of EST240/291/305/325/326/339/342/344/364, one of EST205/207/209/221/310/323/327)\n3 electives(EST100/106/201/205/207/221/240/280/291/305/310/320/323/325/327/339/342/364/475/488/499)\nScience(One of BIO201/202/203/204, CHE131/133/152/154, PHY126/127/131/133/141, AST203/205,CHE132/321/322/331/332,GEO102/103/112/113/122,PHY125/132/134/142/251/252)\nMathematics(one of AMS151/161, one of AMS261/MAT203, one of AMS361/MAT303, one of AMS201/MAT211)",
                      }
@application.route("/degreework", methods=["POST"])
def degreework():
    request_data = json.loads(request.get_data(), encoding='utf-8')
    params = request_data['action']['params']
    param_data = json.loads(params['coursename'])
    lower_param_data = param_data.lower()
    response = {
        "version" : "2.0",
        "template" : {
            "outputs" : [
                {
                    "simpleText" : {
                        "text" : major_requirements[lower_param_data]
                    }
                }
            ]
        }
    }
    return jsonify(response)

if __name__ == "__main__":

    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_coursesem.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_courses.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_courses2.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_professors.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_qa.py")
    schedule.every().day.at("00:00:00").do(os.system, "python drivedownload_qgpt.py")
    while True:
        schedule.run_pending()
        time.sleep(1)

    application.run(host='0.0.0.0', port=80, debug=True)