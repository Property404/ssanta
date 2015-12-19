import getpass
import settings
import send
import ss_contact #Not contacting Nazis
CONTACTS_FILE = "contacts.txt"

# Multi-string replacement
def multi_replace(string, replacements):
	for i in replacements:
		string=string.replace(i[0], i[1])
	return string

# Send mass of emails
def send_secret_santas(sender, password):
	contacts = ss_contact.load_contacts(CONTACTS_FILE);
	for i in contacts:
		# Fix message
		replacements=[
			["$santa", i.name],
			["$kid", i.kid.name],
			["$santa_email",i.email],
			["$kid_email",i.kid.email],
		]
		subject = multi_replace(settings.subject, replacements);
		body = multi_replace(settings.body,replacements);
		
		# Send email
		print("Sending email to: "+i.name+"("+i.email+")");
		send.send_gmail(sender,password,i.email,subject,body);

	# Make Record
	record = open("record.txt","w");
	record.write(ss_contact.show_contacts(contacts));
	record.close();

# Program Body
if __name__=="__main__":
	send_secret_santas(input("Address: "), getpass.getpass("Password:"))
