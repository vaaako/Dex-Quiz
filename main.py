import pypokedex
from PIL import Image, ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

# pokemon = pypokedex.get(name="vaporeon")
# print(pokemon.dex)
# print(pokemon.name)
# print(pokemon.abilities)
# print(pokemon.types)
# print(pokemon.sprites.front.get("default"))

right = 0
wrong = 0
pokemon_id = 1

window = tk.Tk()
window.geometry("600x500")
window.title("VakoDex")
window.config(padx=10, pady=10)

# Título
title_label = tk.Label(window, text="VakoDex \nSuper Desafio")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

# Imagem
pokemon_image = tk.Label(window)
pokemon_image.pack()

# Score
label_score = tk.Label(window)
label_score.config(font=("Arial", 20))
label_score.pack(padx=10, pady=10)

# pokemon_information = tk.Label(window)
# pokemon_information.config(font=("Arial", 20))
# pokemon_information.pack(padx=10, pady=10)

# pokemon_types = tk.Label(window)
# pokemon_types.config(font=("Arial", 20))
# pokemon_types.pack(padx=10, pady=10)


# FUNCTIONS
def get_image(pokemon):
	# Pega imagem
	http = urllib3.PoolManager()
	response = http.request("GET", pokemon.sprites.front.get("default"))
	image = Image.open(BytesIO(response.data))

	# Exibe imagem
	img = ImageTk.PhotoImage(image)
	pokemon_image.config(image=img)
	pokemon_image.image = img

	# Exibe info do pokemon
	# pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
	# pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())

def check_pokemon(event=None):
	global pokemon_id
	global wrong
	global right

	# Pegar pokemon atual
	pokemon = pypokedex.get(dex=pokemon_id)
	pokemon_name = entry_name.get()

	# Checar se está correto
	if pokemon_name==pokemon.name:
		right+=1
		print("Acertou")
	else:
		wrong+=1
		print("Errou")

	# Se chegou no final
	if pokemon_id==898:
		label_score.config(text=f"Right: {right} / Wrong: {wrong}")
		entry_name.config(command=entry_name.pack_forget())
		btn_load.config(command=btn_load.pack_forget())
	pokemon_id+=1 # Se não terminou, próximo pokemon

	# Limpar entry
	entry_name.delete(0, 'end')
	
	# Atualizar pokemon atual
	pokemon = pypokedex.get(dex=pokemon_id)

	# Exibir imagem
	get_image(pokemon)
	# Atualizar pontuação
	label_score.config(text=f"Right: {right} / Wrong: {wrong}")


# Só serve pra mostrar
def load_default():
	# Remover botão de start
	btn_default.config(command=btn_default.pack_forget())
	pokemon = pypokedex.get(dex=1)

	# Imagem
	get_image(pokemon)
	# Score
	label_score.config(text=f"Right: {right} / Wrong: {wrong}")

	# Label
	entry_name.config(font=("Arial", 20))
	entry_name.pack(padx=10, pady=10)

	# Botão Load
	btn_load.config(font=("Arial", 20))
	btn_load.pack(padx=10, pady=10)

# Cria mas não exibe (Só exibir depois que clicar em start)
entry_name = tk.Entry(window)#, height=1)
btn_load = tk.Button(window, text="Load", command=check_pokemon)
entry_name.bind('<Return>', check_pokemon) # Pegar valor da entry com enter

btn_default = tk.Button(window, text="Start", command=load_default)
btn_default.config(font=("Arial", 20))
btn_default.pack(padx=10, pady=10)
	
window.mainloop()