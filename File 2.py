data= {
    "name" : "sudh",
    "mail_id" : "sudh@gmail.com",
    "phone number" : 956456546,
    "subject" : ["data science " , "big data " , "data analytics" ]
}


import json
with open("data.json", "w") as ABC:
    json.dump(data, ABC) 

with open("data.json", "r") as ABC:
    Data1 = json.load(ABC)
    print(Data1) 




import csv
Data = [["name" , "email_id" , "phone_number"],
        ["sudh" ,"sudh@gmail.com" , 92342424],
        ["krish" , "krish@gmail.com" , 9324242]
]

with open("data.csv" , "w" ) as f : 
    writer = csv.writer(f)
    
    for i in Data:  
        writer.writerow(i) 


with open("data.csv" , 'r') as f :
    read_data = csv.reader(f)
    
    for i in read_data:
        print(i)

with open("Binary.bin" , "wb" ) as f :
    f.write(b"\x01\x02\x03\x3454235")

with open("Binary.bin","rb")as f :
    print(f.read()) 
