# open("logfiles.txt", "w").close()
# open("output.txt", "w").close()
# open("stats.csv", "w").close()
x = input("Do you want to clear the recordings (Y/N)")
if x == "Y":
    open("logfiles.txt", "w").close()
    open("output.txt", "w").close()
    open("stats.csv", "w").close()