import json

message="Uzywajcie tego kodu (jezeli linijki sie zle formatuja to dodajcie \\n za slowem zeby wsatwic nowa linijke)"
letter_preset="./data/5tall.json"
addEmptyLineBetweenLines=True
message=message.split("\n")

with open(letter_preset,"r") as f:
	data=json.loads("\n".join(f.read().split("\n")[:-10]))

lines=[["" for i in range(len(data["a"]))] for j in range(len(message))]

for k in range(len(message)):
	for i in message[k].lower():
		for j in range(len(lines[0])):
			lines[k][j]+=data[i][j]+"  "

for i in lines:
	print("\n".join(i))
	if (addEmptyLineBetweenLines):
		print()