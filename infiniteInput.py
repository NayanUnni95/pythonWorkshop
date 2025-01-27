question = 'Enter the permission [y|n]: '
permission = input(question)
data = []
while permission == 'y':
    data.append(input("Enter the value : "));
    permission = input(question)
print("Entered values are : ", data)
    