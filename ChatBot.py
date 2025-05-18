import traceback
import datetime
import random
import argparse
import logging
import csv
import os
import requests

parser = argparse.ArgumentParser(description='Process some arguments.')
parser.add_argument('--question', help='Enter your question.')
parser.add_argument('--answer', help='Enter your answer.')
parser.add_argument('--__new__answer', help='Enter your __new__answer')
parser.add_argument('--add', action='store_true', help='Add question.')
parser.add_argument('--remove', action='store_true', help='Remove question.')
parser.add_argument('--list', action='store_true', help='List questions.')

parser.add_argument('--log', help='Enable Logging.')
group = parser.add_argument_group('CSV Import Command')
group.add_argument('--import', action='store_true', help='Import questions from File.')
group.add_argument('--filetype', help='FileType')
group.add_argument('--filepath', help='Path of File')




args = parser.parse_args()

logger=logging.getLogger()

if(args.log):
    logger.setLevel(args.log)
else:
    logger.setLevel("DEBUG")

logging.basicConfig(filename='C:\\Users\\rohit\\OneDrive\\Desktop\\code\\std.log', filemode='a', format='%(asctime)s : %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')    

vartime = datetime.datetime.now()
currenttimestring = vartime.strftime('%X')

qa_pairs = {
     "What are the reviews of digit course?": {
                "answers" : [
                "The feedback of the students from digit are excellent.",
                "Students find digit as a great platform to develop software skills.",
            ],
            "show_weather" : "true",
            "location" : "Goslar" 
     },
     "How are the reviews of digit course?": {
                "answers" : [
                "The feedback of the students from digit are excellent.",
                "Students find digit as a great platform to develop software skills.",
            ],
            "show_weather" : "true",
            "location" : "Goslar" 
     },
    "Where will be the classes of the course?": {
        "answers" : [
        "The classes of the course will be at ostfalia.",
        "The classes will also be at clausthal.",
            ],
            "show_weather" : "false"
    },        
    
     "How long is the course?": {
        "answers" : [
         "The course is of 2 years.",
         "Course can also be long depending on performance of student.",
            ],
            "show_weather" : "true",
            "location" : "Wolfenbüttel"
     
    },   



    "Do we have to submit assignment of each subject?": {
        "answers" :[
         "No the submission of assignments is not important in ostfalia.",
        "You must submit all assignments in courses which are in clausthal.",
            ],
            "show_weather" : "false",
    },
            
        
     "are the classes online or offline?": {
        "answers" :[
        "Mostly classes are on-site.",
        "In winter when the weather is bad then sometimes we have online classes.",
            ],
            "show_weather" : "true",
            "location" : "Clausthal" 
    },        
            
     "Do we need german language for digit course?": {
        "answers" :[
        "For starting the course you need A2 certificate.",
        "Before your master thesis you need B1.",
            ],
            "show_weather" : "true",
            "location" : "Wolfenbüttel",
    },        
                          
     
    "Does attendance matter for the classes?": {
        "answers" :[
         "It totally depends on you to attend the classes.",
         "But you must attend all the classes.",
         "Attendance in tu clausthal for assignment classes is necessary.",
            ],
            "show_weather" : "false",
    }, 
            
    
    "Does the student identity card consists a semester ticket?": {
        "answers" :[
        "The student card of ostfalia has a semester ticket till hannover.",
        "Unfortunately clausthal identity card does not have asemester ticket.",
            ],
            "show_weather" : "true",
            "location" : "Wolfenbüttel"
    },        
    "From when are the exams?": {
        "answers" :[
        "Exams in ostfalia are in feburary."
        "Exams in clausthal are in march.",   
            ],
            "show_weather" : "false",
    }, 

    "Tell me something about exams.": {
        "answers" :[
        "Exams in ostfalia are in feburary.",
        "Exams in clausthal are in march.",
            ],
            "show_weather" : "true",
            "location" : "Wolfenbüttel"
    },        

  
     "Where will be the classes of the course and how long is the course?": {
        "answers" :[
        "The classes will be in ostfalia.The course is usually 2 years long.",
        "The classes will also be in clausthal.The course duration canexceed depending on the students performance.",
            ],
            "show_weather" : "false",
     },        

            

     "From when do we have exams and does attendance matter for the classes?": {
         "answers" :[
        "Exams are from feburary in ostfalia and attendance does notmatter for classes in ostfalia ."
        "Exams are from march in clausthal and attendance for theassignment classes are important in clausthal.",
            ],
            "show_weather" : "false"
    },
   
}


conversation_history = {}


keyword_suggestions = {
    "semester": ["How are the reviews of digit course?",
                 "Where will be the classes of the course?",
                 "How long is the course?",
                 "Do we have to submit assignment of each subject?",
                 "are the classes online or offline?",
                 
    ],
    "ostfalia": [
        "From when do we have exams and does attendance matter for the classes?",
        "Where will be the classes of the course and how long is the course?",
        "Does attendance matter for the classes?",
        "From when are the exams?",
        "Tell me something about exams.",
        "Do we need german language for digit course?"
    ],
}

class TriviaGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["A. Paris", "B. Rome", "C. Madrid"], "answer": "A"},
            {"question": "Which planet is known as the Red Planet?", "options": ["A. Mars", "B. Venus", "C. Jupiter"], "answer": "A"},
            { "question": "What is the capital of Japan?", "options" : ["A. Beijing" , "B. Tokyo" , "C. Seoul"], "answer": "B"},
            {"question": "Which city hosted the 2008 Summer Olympics?", "options":["A. Beijing" , "B. London" , "C. Athens"], "answer": "A" },
            {"question": "Which continent does Greenland belong to?", "options":["A. Africa" , "B. Asia" , "C. Europe"], "answer": "C"},
            {"question": "Which language is the official language of Germany?", "options":["A. English" , "B. Dutch" , "C. Deutsch"], "answer": "C"},
            {"question": "Which river flows through the capital city  of some European countries?", "options":["A. Rhine" , "B. Nile" , "C. Tiber"], "answer": "A"},
            {"question": "What is the currency in Germany?", "options":["A. Dollar" , "B. Euro" , "C.Swiss Franc"], "answer": "B"},
            {"question": "What is the tallest mountain in the world?", "options":["A. Lhoste" , "B. K2" , "C. Everest"], "answer": "C"},
            {"question":  "Where is the main office of Siemens AG in Germany?", "options":["A. Munich" , "B. Berlin" , "C. Braunshweig"], "answer": "A"}
        ]
        self.score = 0
        self.current_question_index = 0
        self.max_questions = 10
        self.exit = False

    def ask_question(self):
        question_data = self.questions[self.current_question_index]
        print(f'\nQuestion No {self.current_question_index+1}. {question_data["question"]}')
        print(f'Score {self.score}/{self.max_questions}')
        for option in question_data["options"]:
            print(option)

        user_answer = input("Your answer (Enter A, B, or C): ").upper()
        if(user_answer == "TRIVIA"):
            print(f"Game Over! Your final score is {self.score}.")
            self.exit = True
            return
        if user_answer == question_data["answer"]:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {question_data['answer']}.\n")

        self.current_question_index += 1

    def start_game(self):
        print("Trivia Game Activated! ")
        while self.current_question_index < self.max_questions:
            if self.exit:
                break
            self.ask_question()

        print(f"Game Over! Your final score is {self.score}.")

trivia_game = TriviaGame()

def get_weather_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    return T


def chatbot(question):
    if question == "trivia":
        trivia_game.start_game()
        return
    if question in qa_pairs:
        selected_response = random.choice(qa_pairs[question]["answers"])
        conversation_history[question] = selected_response
        if(qa_pairs[question]["show_weather"]=="true"):
            print(get_weather_report(qa_pairs[question]["location"]))
        return selected_response
    else:
        response = provide_suggestions(question.lower())
        conversation_history[question] = response
        return response

def provide_suggestions(keyword):
    if keyword == "trivia":
        trivia_game.start_game()
        return
    if keyword in keyword_suggestions:
        suggestions = keyword_suggestions[keyword]
        suggestion_text = "\n".join([f"{i}. {suggestion}" for i,
suggestion in enumerate(suggestions, start=1)])
        return (f"Select a question by typing the corresponding number:\n{suggestion_text}")
    else:
        return "I don't have suggestions for that keyword."

def main():
    logger.debug('inside main')
    if args.list:
        print("here")
        logger.debug('listing questions')
        logger.debug(qa_pairs)
        
        print_properly(qa_pairs)
    elif args.add:
        logger.debug('adding question')
        qa_pairs[args.question] = { "answers" : [args.answer]} 
        print_properly(qa_pairs)  
    elif args.remove:
        logger.debug('removing question')
        del qa_pairs[args.question]
        print_properly(qa_pairs)
    elif args.question:
        logger.debug('asking question')
        user_input = args.question
        
        response = chatbot(user_input)
        print(f"Chatbot: {response}")
        exit()
    elif args.filepath:
        if(args.filetype != 'CSV'):
            print("Filetype not supported!")
        import_qa_from_csv(args.filepath)
    else:
        logger.debug('asking question')
        run_chatbot()
    logger.debug('exiting main')

def run_chatbot():
    try:
        print(currenttimestring + ' Hello')
        vartime = datetime.datetime.now()
        print(currenttimestring + " How can I help you?")
        while True:
            user_input = input("You: ")

            if (user_input.lower() == "exit" or user_input.lower() == "bye"):
                break

            response = chatbot(user_input)
            print(f"Chatbot: {response}")
    except:
        print("something went wrong")

def print_properly(qa_pairs):
    for index, key in enumerate(qa_pairs):
        print(f"Question No {index+1}: ",key)
        for i, value in enumerate(qa_pairs[key]["answers"]):
            print(f"Answers {i+1} : ", value)
        print(f"\n")


def import_qa_from_csv(file_path):
    try:
       
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Invalid file path: {file_path}")

        
        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"Insufficient access privilege rights: {file_path}")

        if not file_path.lower().endswith('.csv'):
            raise ValueError(f"Unsupported file type: {file_path}")

        
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                qas = row[0].split(",")
                qa_pairs[qas[0]]={"answers" : qas[1:], "show_weather" : False}
            run_chatbot()
            

    except FileNotFoundError as e:
        logging.error(traceback.format_exc())
        logging.error(str(e))
        print(f"Warning: {e}")
    except PermissionError as e:
        logging.error(traceback.format_exc())
        logging.error(str(e))
        print(f"Warning: {e}")
    except ValueError as e:
        logging.error(traceback.format_exc())
        logging.error(str(e))
        print(f"Warning: {e}")
    except csv.Error as e:
        logging.error(traceback.format_exc())
        logging.error(f"Error while processing CSV: {e}")
        print(f"Warning: Error while processing CSV - {e}")
    except Exception as e:
        logging.error(traceback.format_exc())
        logging.error(f"Unhandled Exception: {e}", exc_info=True)
        print("An unexpected error occurred. Please check the log file for details.")   
         



if __name__ == "__main__":
    main()
