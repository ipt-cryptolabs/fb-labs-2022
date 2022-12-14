import regex


class files:
	def __init__(self, file_name):
		self.file_name = file_name


	def read(self):
		file = open(self.file_name)
		t = file.read()
		file.close()
		t = regex.sub(r'\p{^IsCyrillic}', ' ', t.lower())
		t = regex.sub(r'\s+', ' ', t)
		t = regex.sub(r'ั', 'ะต', t)
		t = regex.sub(r'ั', 'ั', t)
		return t


	def read_wos(self):
		return regex.sub(r'\s', '', self.read())