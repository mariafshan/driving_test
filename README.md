# Background
Want to study for the Illinois driving test without a study partner? This Python code throws random questions from the official Illinois Driving handbook. Illinois requires drivers to answer 28 questions correctly out of 35 (80%). The IL handbook contains 86 questions so if you get at least 69 questions correctly then you should be ready to take the written test!

Practice questions and study material:
- The Illinois Secretary of State (SOS) official Driving Handbook: [Illinois Rules of the Road 2022](https://www.ilsos.gov/publications/pdf_publications/dsd_a112.pdf)

Author: [Maria Clarissa Fionalita](https://github.com/mariafshan/)

# How to Use
Run the code as it is and you should be good to start practicing. The code will prompt random questions from the driving handbook, input your answer accordingly.
- Input _T_ or _F_ if the question is marked _[T/F]_
- Input the corresponding letter answer if the question has multiple choice answers (e.g. _a_)

The input space is case-insensitive.

By default, the code is set so it will show 86 questions at random sequence. If you do not wish to go through all 86 questions, you can change the max variable of *random_questions_array()* function to your desired number of questions *(e.g. random_questions_array(max = 50))*

# Scoring
Each correct answer is worth 1 point. At the end of the practice session, the code will display:
1. The number of questions answered correctly
2. The % of the correctly answered questions
3. The questions that were answered incorrectly, user's answer, and the correct answer

Each question is marked with the chapter number from the guide book and the question number. E.g. _[4.1]_ means chapter 4 question 1.
Review the chapter in the guidebook for the questions answered incorrectly.
