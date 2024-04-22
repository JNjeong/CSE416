from flask import Flask, jsonify, request
import requests, sys, json
import random
application = Flask(__name__)

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

@application.route("/menu", methods=["POST"])
def menu_information():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "Lunch(점심)\nPrice : 4,500won\nTime : 11:30~13:30\nFried tofu soup(유부장국)\nKimchi Pilaf(김치필라프)\nChicken Cutlet&mustard(치킨가스&스프)\nGreen Salad&Green grape sauce(그린샐러드/청포도소스)\nYogurt(요구르트)\nKimchi(포기김치)"
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
                                "label": "Course Information",
                                "messageText": "You can enter the name of the course, the lecture title, or just numbers to check the credits, prerequisites, textbook, major topics, etc. of the corresponding course."
                            },
                            {
                                "action":  "message",
                                "label": "Professor Information",
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


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)