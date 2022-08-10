n = int(input("How many numbers you want to put into list?: "))
base = 1
ScoreList = []

while base != (n+1):
    Score = int(input("Score of class: "))
    ScoreList.append(Score)
    base += 1

Max = max(ScoreList)
ScoreList.remove(Max)
if ScoreList.count(Max) >0 :
    while ScoreList.count(Max) != 0:
        ScoreList.remove(Max)

Second = max(ScoreList)
print("The First-Runner Up got a score of: " + str(Second))
