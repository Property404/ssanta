import random
# Create Contact class
class Contact:
	def __init__(self, name, email):
		self.name=name
		self.email=email
	def assign_kid(self, kid):
		self.kid=kid
	def get_kid(self):
		return self.kid

# Get contacts from file and assign "kid" to each one
def load_contacts(filename):
	#Make contact list
	raw = open(filename,"r").read();
	raw = raw.replace("\r","");
	raw_list = raw.split("\n");
	contact_list=[];
	
	#split into name and email
	for i in raw_list:
		contact_list.append(Contact(i[0:i.rfind(" ")],i[i.rfind(" ")+1::]))
		
	#Randomize Contacts
	contacts=[];
	for i in range(len(contact_list)):
		element=random.choice(contact_list)
		contact_list.remove(element)
		contacts.append(element);
	
	#Assign kids
	for i in range(len(contacts)):
		contacts[i].assign_kid(contacts[i+1 if i!=len(contacts)-1 else 0])
	return contacts

def show_contacts(contacts):
	display=""
	for i in contacts:
		display+=("Secret Santa: "+i.name+"("+i.email+")\n");
		display+=("Kid: "+i.kid.name+"\n\n");
	return display