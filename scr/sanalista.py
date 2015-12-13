def etsisanat(sanalista):
	for i in sanalista:
		if i == "drink":
				return "get_first"
		elif i == "dance":
			return "dance"
		elif i == "wiggle" or i == "dirty dance":
			return "wiggle_wiggle"
		elif i == "get":
			for a in sanalista:
				if a == "naked":
					return "get_naked"
				elif a == "dressed":
					return "get_dressed"
		elif i == "suicide" or i == "die":
			return "suicide"
		elif i == "move":
			for a in sanalista:
				if a == "left":
					return "move_left"
				if a == "right":
					return "move_right"
		elif i == "masturbate" or i == "fap" or i == "wank":
			return "winwin"
		elif i == "please" or i == "fuck":
			for a in sanalista:
				if a == "yourself":
					return "winwin"
		elif i == "sing" or i == "jodlaa":
			return "sing"
		elif i == "undress":
			return "get_naked"
		elif i == "put":
			for a in sanalista:
				if a == "clothes":
					return "get_dressed"
		elif i == "moonwalk":
			return "moonwalk"
		elif i == "kill":
			return "killed"
		elif i == "helikopteri" or i == "helicopter":
			return "heli"
		elif i == "beer":
			return "beer"
		elif i == "use":
			for a in sanalista:
				if a == "force":
					return "force"
		elif i == "join":
			for a in sanalista:
				if a == "darkside":
					return "dark_side"
		elif i == "penus":
			return "penus"
		elif i == "jump":
			return "jump"
		elif i == "stop":
			return "stop"
		elif i == "fuck":
			for a in sanalista:
				if a == "you" or a == "u":
					return "fuck_you"
		elif i == "fu":
			return "fuck_you"
		elif i == "oh":
			for a in sanalista:
				if a == "my" or a == "god":
					return "oh_my"
		elif i == "happy":
			for a in sanalista:
				if a == "ending":
					return "happy_ending"
		elif i == "go":
			return "go"
		elif i == "smoke" or i == "smoking":
			return "smoke"
		elif i == "start":
			for a in sanalista:
				if a == "smoking":
					return "smoke"
		elif i == "salainensana":
			return "skip"
		else:
			return "unknown"
	
