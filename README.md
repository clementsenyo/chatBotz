# Chatbot Project

This project implements a simple chatbot that responds to user queries based on predefined question-answer pairs. It also includes a trivia game and a weather reporting feature.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Description](#description)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, you need to have Python installed. You can install the necessary dependencies using pip.

```bash
pip install -r requirements.txt
Usage
To run the chatbot, execute the following command:

bash
Copy code
python chatbot.py --question "Your question here"
You can use additional command-line arguments to interact with the chatbot:

bash
Copy code
python chatbot.py --add --question "Your new question" --answer "The answer to your question"
python chatbot.py --remove --question "Question to remove"
python chatbot.py --list
python chatbot.py --import --filetype "CSV" --filepath "path/to/your/file.csv"
python chatbot.py --log "DEBUG"
Project Structure
chatbot.py: Main script for the chatbot.
requirements.txt: List of dependencies.
tests.py: Unit tests for the chatbot.
Description
Arguments
--question: Enter your question.
--answer: Enter your answer.
--add: Add a new question and answer pair.
--remove: Remove a question.
--list: List all questions.
--log: Enable logging.
--import: Import questions from a file.
--filetype: Specify the file type (only CSV is supported).
--filepath: Path to the file.
#Logging
Logging is set up to store logs in std.log with different levels of verbosity. Enable logging by using the --log argument.

#Question-Answer Pairs
The chatbot uses a dictionary of predefined question-answer pairs to respond to user queries. It can also provide weather reports for specific questions.

#Trivia Game
The chatbot includes a trivia game with a set of predefined questions. Start the game by typing "trivia" as your question.

#Weather Report
For certain questions, the chatbot provides a weather report for a specified location using the wttr.in API.

Importing Questions
You can import questions from a CSV file using the --import argument along with --filetype and --filepath. The CSV file should have questions and answers separated by commas.

#Testing
Unit tests are provided to verify the functionality of the chatbot. Run the tests using:
python -m unittest tests.py

#Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any feature enhancements or bug fixes.

#License
This project is licensed under the MIT License. See the LICENSE file for details.

#Example CSV File for Import
Question,Answer 1,Answer 2,Show Weather,Location
How are the reviews of digit course?,The feedback of the students from digit are excellent,Students find digit as a great platform to develop software skills,true,Goslar
Where will be the classes of the course?,The classes of the course will be at ostfalia,The classes will also be at clausthal,false
How long is the course?,The course is of 2 years,Course can also be long depending on performance of student,true,Wolfenbüttel

You can copy this content into your `README.md` file to provide a comprehensive guide for your project.
