import pypokedex, urllib3
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk

# FUNCTIONS
def get_image(pokemon):
	# Get image
	http = urllib3.PoolManager()
	response = http.request("GET", pokemon.sprites.front.get("default"))
	image = Image.open(BytesIO(response.data))

	# Show Image
	img = ImageTk.PhotoImage(image)
	pokemon_image.config(image=img)
	pokemon_image.image = img


correct, wrong, pokemon_id = 0, 0, 895
def check_pokemon(event=None):
	global pokemon_id
	global wrong
	global correct

	# Get current pokemon
	pokemon = pypokedex.get(dex=pokemon_id)
	typed_name = entry_name.get().lower()



	# Show the correct pokemon's name
	pokemon_correct_name.config(text=pokemon.name.capitalize())
	pokemon_correct_name.pack(padx=10, pady=10)

	# Progress
	progress.config(text=f"{pokemon_id}/898")
	progress.pack(padx=10, pady=10)

	# If correct
	if typed_name==pokemon.name:
		correct+=1
		print("Correct")
	elif (pokemon.name=="nidoran-f" or pokemon.name=="nidoran-m") and (typed_name=="nidoran"): # Nidoran bug
		correct+=1
		print("Correct")
	else:
		wrong+=1
		print("Wrong")


	# Last pokemon
	if pokemon_id==898:
		label_score.config(text=f"Correct: {correct} / Wrong: {wrong}")
		entry_name.config(command=entry_name.pack_forget())
		btn_load.config(command=btn_load.pack_forget())

	else: 
		pokemon_id+=1 # Next pokemon
		entry_name.delete(0, 'end') # Clear entry
		pokemon = pypokedex.get(dex=pokemon_id) # Update pokemon

		get_image(pokemon) # Show image
		label_score.config(text=f"Correct: {correct} / Wrong: {wrong}") # Update score


# Just to show
def load_default():
	# Remove
	btn_default.config(command=btn_default.pack_forget())
	title_label.config(text=" ", font=20)

	# Add stuffs
	pokemon = pypokedex.get(dex=pokemon_id)
	get_image(pokemon) # Image
	label_score.config(text=f"Correct: {correct} / Wrong: {wrong}") # Score
	entry_name.pack(padx=10, pady=10) # Label
	btn_load.pack(padx=10, pady=10) # Load button



window = tk.Tk()
window.geometry("600x500")
window.title("Dex")
window.config(padx=10, pady=10)

# Title
title_label = tk.Label(window, text="Dex \nUltimate Quiz")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

# Image
pokemon_image = tk.Label(window)
pokemon_image.pack()

# Score
label_score = tk.Label(window)
label_score.config(font=("Arial", 20))
label_score.pack(padx=10, pady=10)


# Creates but does not show (Just shows after click on start button)
entry_name = tk.Entry(window)#, height=1)
entry_name.config(font=("Arial", 20))

btn_load = tk.Button(window, text="Load", command=check_pokemon)
btn_load.config(font=("Arial", 20))

pokemon_correct_name = tk.Label(window)
pokemon_correct_name.config(font=("Arial", 24))

progress = tk.Label(window)
progress.config(font=("Arial", 16))

entry_name.bind('<Return>', check_pokemon) # Get entry value with enter button

# Main
btn_default = tk.Button(window, text="Start", command=load_default)
btn_default.config(font=("Arial", 20))
btn_default.pack(padx=10, pady=10)
	
window.mainloop()