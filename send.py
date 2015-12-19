# smtplib module send mail
import smtplib
import getpass
def send_gmail(sender, password, receiver, subject, body):
	#Connect to Server
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	#Log in
	server.login(sender, password)

	#PRepare message
	message = '\r\n'.join(['To: %s' % receiver,
						'From: %s' % sender,
						'Subject: %s' % subject,
						'', body])
						
	# Attempt to send message
	status=1
	try:
		server.sendmail(sender, [receiver], message)
		print ('email sent')
	except:
		print ('error sending mail')
		status=0;
	server.quit()
	return status