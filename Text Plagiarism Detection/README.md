# Text Plagiarism Detection

## What is Plagiarism
Plagiarism is an act of stealing someone else’s work and admitting and passing them off as one's own, 
and now we have a system to detect this act.
Plagiarism has become a serious issue now days due to the presence of vast resources easily 
available on the web, which makes developing plagiarism detection tool a useful and challenging task 
due to the scalability issues.

The detection tool then highlights the sections where the text is similar, 
and determines whether there is plagiarism or not. 
Proposed solution is using python language.


## What does the above python source code does ?
1. It imports the two text files which are to be checked for plagiarism.  
2. This text plag detector consists of three parts. 
3. In first part, Html file is created(named as difference_report_v3.html) and difference
between both the files are written to it.
4. In second part, it reads both the text files and converts it into lists ( after splitting the string).
5. After that, it compares both the lists and prints the similar lists.  
6. In third part of the project, it shows/prints the similarity percentage between the two files imported earlier.

## Language and Software used :
1. Python 3.8
2. Pycharm IDE
3. Web Browser(Google Chrome) 


## Screenshots :-

1) HTML FILE CONTENTS :

<img src="https://github.com/utkarsh-yadav1231/Plagiarism-Detection/blob/master/Text%20Plagiarism%20Detection/Other%20Files/Output%20HTML_diff.PNG" alt="SS 1"/>

2) Output file :

<img src="https://github.com/utkarsh-yadav1231/Plagiarism-Detection/blob/master/Text%20Plagiarism%20Detection/Other%20Files/Output%20Text_Plag.PNG" alt="SS 2"/>
