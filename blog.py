from observer import Publisher, Subscriber
publishers = {}
subscribers = {}
while(True):

	element_type = int(input("\n\n1. Create a publisher \n2. Create a subscriber \n3. Register a subscriber to publisher \n4. Unregister a subscriber\n5. Update content in publisher \n"))
		
	if(element_type == 1):
		name = input("Enter the publisher name : ")
		name_cpy = name
		try:
			name = Publisher()
			publishers[name_cpy] = name
			#print(publishers)
			print("Publisher "+name_cpy+" successfully created")
		except:
			print("Publisher "+name_cpy+" couldn't be created")

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
		pub_name = input("Enter the publisher's name : ")
		#print(publishers)
		#print(subscribers)
		publishers[pub_name].register(subscribers[subs_name])

	elif(element_type == 4):
		subs_name = input("Enter the subscriber's name : ")
		pub_name = input("Enter the publisher's name : ")
		publishers[pub_name].unregister(subscribers[subs_name])

	elif(element_type == 5):
		pub_name = input("Enter the publisher's name : ")
		val = input("Enter the content : ")
		publishers[pub_name].update(val)
