from observer import Subject, Subscriber

class Subscriber(Subscriber):
	def __init__(self, name):
		super().__init__(name)

	def getNotified(self, _update):
		print("{} got {} message".format(self.name, _update))


Subjects = {}
subscribers = {}

while(True):

	element_type = int(input("\n\n1. Create a Subject \n2. Create a subscriber \n3. Register a subscriber to Subject \n4. Unregister a subscriber \n5. Update content in Subject \n"))
		
	if(element_type == 1):
		name = input("Enter the Subject name : ")
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
		name = input("Enter the subscriber name : ")
		name_cpy = name
		try:
			name = Subscriber(name)
			subscribers[name_cpy] = name
			#print(subscribers)
			print("Subscriber "+name_cpy+" successfully created")
		except:
			print("Subscriber "+name_cpy+" couldn't be created")


	elif(element_type == 3):
		subs_name = input("Enter the subscriber's name : ")
		pub_name = input("Enter the Subject's name : ")
		#print(Subjects)
		#print(subscribers)
		Subjects[pub_name].register(subscribers[subs_name])

	elif(element_type == 4):
		subs_name = input("Enter the subscriber's name : ")
		pub_name = input("Enter the Subject's name : ")
		Subjects[pub_name].unregister(subscribers[subs_name])

	elif(element_type == 5):
		pub_name = input("Enter the Subject's name : ")
		val = input("Enter the content : ")
		Subjects[pub_name].update(val)
