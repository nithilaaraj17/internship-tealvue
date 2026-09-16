import csv
with open("student.csv","r") as inputfile:
    reader = csv.DictReader(inputfile)
    with open("Result.csv","w",newline="") as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(["name","java","python","dbms","total","average","grade"])
        
        for row in reader:
            name = row["name"]
            java = int(row["java"])
            python = int(row["python"])
            dbms = int(row["dbms"])
            
            total = java+python+dbms
            average = total/3
            
            if average>=90:
                grade ="A+"
            elif average >=80:
                grade ="A"
            elif average >=70:
                grade ="B"
            elif average >=60:
                grade = "C"
            elif average >=50:
                grade = "D"
            else:
                grade ="F"
            
            writer.writerow([name,java,python,dbms,total,round(average,2),grade])
print("Student result calculated successful")
print("result saved in result.csv")
            