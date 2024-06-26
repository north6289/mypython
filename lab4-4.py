std = {"name" : "Pongsakorn Poompanthong" , "age":16, "gpa":3.75 ,"old_sch":"กาญจนาภิเษกวิทยาลัย"}
print (std)
print ("สวัสดีคุณ %s" % std["name"])
print("อายุ %d เกรดเฉลี่ย %.2f จบการศึกษาจาก %s" % (std["age"] , std["gpa"] , std["old_sch"]))