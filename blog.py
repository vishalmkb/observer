from observer import Subject, Subscriber

class Subscriber(Subscriber):
	def __init__(self, name):
		super().__init__(name)

	def getNotified(self, _update):
		print("{} got '{}' message".format(self.name, _update))


Subjects = {}
Subscribers = {}

while(True):

	element_type = int(input("\n\n1. Create a Blog \n2. Create a subscriber \n3. Register a subscriber to Subject \n4. Unregister a subscriber \n5. Update content in Blog \n"))
		
	if(element_type == 1):
		name = input("Enter the Blog name : ")
		name_cpy = name
		try:
			name = Subject(name)
			Subjects[name_cpy] = name
			#print(Subjects)
			print("[CREATED] Blog "+name_cpy+" successfully created")
		except Exception as e:
			print(e)
			print("[ERROR] Blog "+name_cpy+" couldn't be created")

	elif(element_type == 2):
		name = input("Enter the subscriber name : ")
		name_cpy = name
		try:
			name = Subscriber(name)
			Subscribers[name_cpy] = name
			#print(Subscribers)
			print("[CREATED] Subscriber "+name_cpy+" successfully created")
		except:
			print("[ERROR] Subscriber "+name_cpy+" couldn't be created")


	elif(element_type == 3):
		subs_name = input("Enter the subscriber's name : ")
		pub_name = input("Enter the Blog's name : ")
		#print(Subjects)
		#print(Subscribers)
		try:
			Subjects[pub_name].register(Subscribers[subs_name])
			print("[SUCCESS] Subscriber "+subs_name+" successfully registered to "+pub_name);
		except:
			print("[ERROR] Registration failed")


	elif(element_type == 4):
		subs_name = input("Enter the subscriber's name : ")
		pub_name = input("Enter the Blog's name : ")
		try:
			Subjects[pub_name].unregister(Subscribers[subs_name])
			print("[SUCCESS] Subscriber "+subs_name+" successfully unregistered to "+pub_name);
		except:
			print("[ERROR] Unregister failed")

	elif(element_type == 5):
		pub_name = input("Enter the Blog's name : ")
		val = input("Enter the content : ")
		try:
			print("[SUCCESS] Content updated");
			Subjects[pub_name].update(val)
		except:
			print("[ERROR] Couldn't update content")

