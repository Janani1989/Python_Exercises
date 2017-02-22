"""This program performs 2 tasks:
1. Removes valid comments from an input C program provided by the user
2. Reports invalid comments as errors 
"""
import re
import sys

#Get user input on the source program

filename=raw_input("Enter the file name of the C program")
f1=open(filename,'r')
content=f1.read()

#1.Pattern Match the valid comments and substitute them with empty string

regex = re.compile(r'(\/\*(?:.|\n\s*\S*\*)*?\/)|(//.*)') #comments could either be of style /* */(single|multiline) or //(singleline)
valid_comments=regex.sub("",content);
f2=open('withoutcomments.txt','w')  
f2.write(valid_comments);

#2.Find out the invalid comments and report to user

#2.a.Remove valid multiline comments from the original file

regex1=re.compile(r'(/\*(.*?)(\*/))',re.MULTILINE|re.DOTALL)
multi_match=regex1.findall(content)
valid=content
for n in multi_match:
    pattern=re.search("/\*",n[1])
    if(pattern==None):
        valid=valid.replace(n[0],"")

#2.b.Pattern match for incorrect single and multiline comments

regex=re.compile(r'((/n/s*|.*?)(/(/|\*.*|.*)))')
matches=regex.findall(valid)
for m in matches:
    #m2 holds the incorrect comments
    m1=m[1].strip();
    if((m1=='')or(m1.endswith((";","{","}",")","else",">"))==True)or(m1.startswith("case")==True)):
        if(m[2]!=''):
            if(m[3]!='/')and(m[3].startswith('*')==False):
                print "Invalid Comment : ",m[2],"\n"

#FINDING OUT INCORRECT MULTILINE COMMENTS

            elif(m[3].startswith('*')==True):
                if(m[3].endswith("*/")==False):
                    print "Unterminated Comment: ",m[2],"\n"

    

