from observer import Subject, Subscriber

class Subscriber(Subscriber):
	def __init__(self, name):
		super().__init__(name)

	def getNotified(self, _update):
		print("{} got {} message".format(self.name, _update))


Subjects = {}
subscribers = {}

while(True):

	element_type = int(input("\n\n1. Create a group \n2. Create a user \n3. Register a user to group \n4. Unregister a user to group\n5. Send message in group \n"))
		
	if(element_type == 1):
		name = input("Enter the group name : ")
		name_cpy = name
		try:
			name = Subject(name)
			Subjects[name_cpy] = name
			#print(Subjects)
			print("Subject "+name_cpy+" successfully created")
		except Exception as e:
			print(e)
			print("Subject "+name_cpy+" couldn't be created")

	elif(element_type == 2):
		name = input("Enter the User name : ")
		name_cpy = name
		try:
			name = Subscriber(name)
			subscribers[name_cpy] = name
			#print(subscribers)
			print("User "+name_cpy+" successfully created")
		except:
			print("User "+name_cpy+" couldn't be created")


	elif(element_type == 3):
		subs_name = input("Enter the User's name : ")
		pub_name = input("Enter the Group's name : ")
		#print(Subjects)
		#print(subscribers)
		Subjects[pub_name].register(subscribers[subs_name])

	elif(element_type == 4):
		subs_name = input("Enter the User's name : ")
		pub_name = input("Enter the Group's name : ")
		Subjects[pub_name].unregister(subscribers[subs_name])

	elif(element_type == 5):
		pub_name = input("Enter the User's name : ")
		val = input("Enter the content : ")
		Subjects[pub_name].update(val)
