import os
import datetime
import reports
import emails

def pdf_body(description_path):
    """It extracts the name and weight information from all the description files and outputs a string in the requested format"""
    name = []
    weight = []

    for file in os.listdir(description_path):
        with open(os.path.join(description_path, file)) as txt_file:
            k = txt_file.readlines()
            val_name = k[0].strip()
            val_weight = k[1].strip()
            name.append("name: " + val_name)
            weight.append("weight: " + val_weight)

    output = ''

    for i in range(len(name)):
        output += name[i] + '<br />' + weight[i] + '<br />' + '<br />'

    return output

if __name__ == "__main__":
    description_path = os.path.join(os.getcwd(), 'supplier-data', 'descriptions')
    current_date = datetime.date.today().strftime("%B %d, %Y") # converts the current date from datetime object to string
    title = 'Processed Update on ' + current_date 
    destination =  '/tmp/processed.pdf'
    email_subject = 'Upload Completed - Online Fruit Store'  # subject line give in assignment for email
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'  # body line give in assignment for email
    reports.generate_report(destination, title, pdf_body(description_path))
    email = emails.generate_email("automation@example.com", "student-01-a6f586ec50d3@example.com",
                         email_subject, email_body, "/tmp/processed.pdf")  # structuring email and attaching the file. Then sending the email, using the cus$
    emails.send_email(email)    
    