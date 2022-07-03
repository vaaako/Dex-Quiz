# Dex-Ultimate-Quiz
Guess the name of the 898 pokemons<br>
Project made for fun (First time using tkinter)
<br>

Knowed Bugs:
- Nidoran gets wrong becausa don't have the signal
- Pokemons with signals like "Mr. Mime" or "Farfetch'd" get wrong

# Requirements
- Intall the requirements.txt with `pip3 install -r requirements.txt`
- For **tkinter**:
	- Ubuntu: `sudo apt-get install python3-tk`
	- Fedora: `sudo dnf install python3-tkinter`

# PIL ImportError
If you get the error `ImportError: cannot import name 'ImageTk' from 'PIL'`<br>
Run the command: 
	- Ubuntu: `sudo apt-get install python3-pil python3-pil.imagetk`
	- Fedora: `sudo dnf install python3-pillow-tk.x86_64 python3-pillow.x86_64 `
	- ArchLinux `sudo pacman -S python-pillow `

