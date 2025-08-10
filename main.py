from collections import Counter
import os
import xml.dom.minidom as md

rc = md.parse("rc.xml")
keyboard_tag = rc.getElementsByTagName('keyboard')

confirmation = False

os.system("clear")

print("Welcome to the Openbox Bind Configurator. Please put the shit this outputs in rc.xml. If you have eyes, should be straightforward :)")
print("")
print("Letters on the keyboard are lowercase. 'space' is spacebar, 'W' is Windows/Meta/Super key, 'A' is Alt key, F1-F12 keys, 'C' is Control. Each key has a Dash inbetween.")
print("")

mode = input("""Which mode? 
command(1)
mouse(2)
> """)

if mode == "2":
    

if mode == "1":
	keys = input("Type the keys you want to use for the command, with a '-' in between them : ")
	
	char_count = Counter(keys)
		
	for char, count in char_count.items():
		if count > 1:
			print("Duplicate characters")
			os.abort()
	for char in keys:
		if char.isupper() and char not in ['A', 'C', 'W', 'F']:
			print("Invalid keybind (Capital letters besides W, A, F1-F12, and C)")
			os.abort()
	
	
	confirm = input("do u like '" + keys + "' ? Y/n : ")
	if confirm == "n" or confirm == "N":
		print("oki")
		os.abort()
	else:
		print("")
		print("oki")
		confirmation = True
	
	if confirmation == True:
		print("")
		command = input("command plis : ")
		print("oki")
		notify_enabled = input("Do you want notify enabled? Y/n :")
		notify_enabled_xml = "true"
		if notify_enabled == "N" or notify_enabled == "n":
			print("oki")
			notify_enabled_xml = "false"
		else:
			notify_enabled_xml = "true"
	
	
	
		#Note to self: Change action name once other action types are added
		BindAction = '''
		<keybind key="''' + keys + ''' ">
		  <action name="Execute"> 
			<startupnotify>
			  <enabled>true</enabled>
			  <name>''' + command + '''</name>
			</startupnotify>
			<command>'''+ command + '''</command>
		  </action>
		</keybind>''' ##Just for reference
	
		print("")
		print("Writing XML CODE now")
	
		## WRITES THE XML CODE TO THE CONFIG FILE
		print("Creating elements...")
	
		keyboard_element = rc.getElementsByTagName("keyboard")[0]
		keybind_element = rc.createElement("keybind")
		keybind_element.setAttribute("key", keys)
	
		## TODO ADD MORE ACTIONS!!
		action_element = rc.createElement("action")
		action_element.setAttribute("name", "Execute")
	
		##Notify
		notify_element = rc.createElement("startupnotify")
		enabled = rc.createElement("enabled")
		enabled_textnode = rc.createTextNode(notify_enabled_xml)
		notification_name = rc.createElement("name")
		notification_textnode = rc.createTextNode(command)
		command_element = rc.createElement("command")
		command_textnode = rc.createTextNode(command)
	
	
	
	
		print("Structuring them...")
		keyboard_element.appendChild(keybind_element)
		keybind_element.appendChild(action_element)
		action_element.appendChild(notify_element)
		notify_element.appendChild(enabled)
		notify_element.appendChild(notification_name)
		enabled.appendChild(enabled_textnode)
		notification_name.appendChild(notification_textnode)
		action_element.appendChild(command_element)
		command_element.appendChild(command_textnode)
	
		
	
	
		print("Writing to file...")
	
		with open("config.xml", "w") as file:
		  # Convert the document to a string
			xml_str = rc.toxml()
		  # Write the string to the file
			file.write(xml_str)
	
		print("done")
		os.abort()
		#os.system("openbox --restart")
		
	