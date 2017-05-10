import pandas as pd
import csv


Complete = pd.read_csv('mailing.csv')

#===drop duplicates
NewSet = Complete.drop_duplicates(subset="EMPLID", keep='first')
NewSet.to_csv('OutputMailing.csv')


#head to make sure its input right
#print(MasterForAttend.head())
#print(AttendanceMaster.head())

#newset1 = AllAttendance["Names"].value_counts()
#print (newset1)
#newset1.to_csv('OutputJcohortCount.csv')

#===what class of data is this?
#print(type(AllAttendance))






#===creating a set is a way to do unique entries
#===didnt work for me
#NewSet = set(AllAttendance)
#print(NewSet)
      




    
