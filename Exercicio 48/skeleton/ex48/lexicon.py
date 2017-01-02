lexicon = {'north': 'direction', 
			'south':'direction', 
			'east': 'direction', 
			'go': 'verb',
			'kill': 'verb',
			'eat': 'verb',
			'the': 'stop',
			'in': 'stop',
			'of': 'stop',
			'bear': 'noun',
			'princess': 'noun',
			'IAS': 'error'}


def scan(text):

        text = text
        words = text.split()
        content = []

        for word in words:
        	try:
        		category = 'number'
        		value = int(word)
        		content.append((category, value))
        	except:
        		category = lexicon.get(word, 'error')
        		value = word
        		content.append((category, word))

        return content