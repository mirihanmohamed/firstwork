mathgrade=float(input('Enter the score for math: '))
#print(mathgrade)
sciencegrade=float(input('Enter the score for Science: '))
englishgrade=float(input('Enter The Score for English: '))
totalscore=mathgrade+sciencegrade+englishgrade
print("Total Score: "+str(totalscore))
averagescore=totalscore/3
print("Average Score: " +str(averagescore))
if averagescore>=90:
    print("Grade : A")
elif averagescore>=80:
    print("Grade : B")
elif averagescore>=70:
    print("Grade : C")
elif averagescore>=60:
    print("Grade : D")
else:
    print("Grade : F")
