
import matplotlib.pyplot as plt


marks = []

for i in range(5):
  m = int(input(f"Enter {i+1} student marks: "))     
  marks.append(m)

for i in range(5):
    current_marks = marks[i]
    
    if current_marks >= 90:
        grade = "A" 
        remark = "EXCELLENT"
    elif current_marks >= 80:
        grade = "B"
        remark = "VERY GOOD"
    elif current_marks >= 70:
        grade = "C"
        remark = "GOOD"
    else:
        grade = "D"
        remark = "NOT BAD"

    print(f"Student {i+1}: Marks={current_marks}, Grade={grade}, remark={remark}")
  
  #x-axis (students)
students = [1, 2, 3, 4, 5]

#graph
plt.plot(students,marks, marker='o')

plt.title("Students marks graph")
plt.xlabel("students")
plt.ylabel("marks")

plt.show()

plt.savefig("graph.png")
plt.close()
plt.show() 

