from observer import Subject, Subscriber, Publisher

class groupSubscriber(Subscriber):
	def __init__(self, name):
		super().__init__(name)
		self.publisher = Publisher(name)

	def getNotified(self, _update):
		print("group user {} got {} message in {} group".format(self.name, _update['message'], _update['group']))

	def publish(self, _subject, _update):
		self.publisher.addSubject(_subject)
		self.publisher.publish(_subject, _update)


class blogSubscriber(Subscriber):
	def __init__(self, name):
		super().__init__(name)

	def getNotified(self, _update):
		print("blog user {} got {} message in {} group".format(self.name, _update['message'], _update['group']))


Subjects = {}
Subscribers = {}

def main():
	while(True):

		element_type = int(input("\n\n1. Create a subject \n2. Create a user \n3. Register a user to subject \n4. Unregister user from a subject\n5. Send message in subject \n6. Display users in subject\n"))
			
		if(element_type == 1):
			name = input("Enter the subject name : ")
			name_cpy = name
			try:
				name = Subject(name)
				Subjects[name_cpy] = name
				#print(Subjects)
				print("[CREATED] Subject "+name_cpy+" successfully created")
			except:
				print("[ERROR] Subject "+name_cpy+" couldn't be created")

		elif(element_type == 2):
			name = input("Enter the User name : ")
			usr_type = int(input("\n1. Blog Subscriber\n2. Group Subscriber\n"))
			name_cpy = name
			try:
				if (usr_type == 1):
					name = blogSubscriber(name)
				elif (usr_type == 2):
					name = groupSubscriber(name)
				Subscribers[name_cpy] = name
				#print(Subscribers)
				print("[CREATED] User "+name_cpy+" successfully created")
			except Exception as e:
				print(e)
				print("[ERROR] User "+name_cpy+" couldn't be created")


		elif(element_type == 3):
			subs_name = input("Enter the User's name : ")
			pub_name = input("Enter the Subject's name : ")
			#print(Subjects)
			#print(Subscribers)
			try:
				Subjects[pub_name].register(Subscribers[subs_name])
				print("[SUCCESS] User "+subs_name+" successfully registered to "+pub_name);
			except:
				print("[ERROR] Registration failed")

		elif(element_type == 4):
			subs_name = input("Enter the User's name : ")
			pub_name = input("Enter the Subject's name : ")
			try:
				Subjects[pub_name].unregister(Subscribers[subs_name])
				print("[SUCCESS] User "+subs_name+" successfully unregistered to "+pub_name);
			except:
				print("[ERROR] Unregister failed")

		elif(element_type == 5):
			user_name = input("Enter the User's name : ")
			grp_name = input("Enter the Subject's name : ")
			message = input("Enter the content : ")
			val = {'message':message, 'group':grp_name}
			try:
				Subscribers[user_name].publish(Subjects[grp_name], val)
				# print("[SUCESS] User "+user_name+" sent the message successfully")
			except:
				print("[ERROR] Failed to send message")

		elif(element_type == 6):
			grp_name = input("Enter the Subject's name : ")

			try:
				subject = Subjects[grp_name]
				for subscriber in subject.subscribers:
					print("* {} of type {} *".format(subscriber.name,type(subscriber)))
			except:
				print("[ERROR] Failed to send message")

		else:
			exit()

if (__name__ == "__main__"):
	main()