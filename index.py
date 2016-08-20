# coding=utf-8
import re
from bencher import Timer
from dictionary import pairs, lang_aliases

class Metagrapher(object):
	# Transliteration pairs and language aliases, imported
	# from the standard dictionary in the beginning ↑:
	pairs = pairs
	aliases = lang_aliases

	# Allows to override presetted dictionary language pairs with
	# the user-defined pairs:
	overrider = lambda self, a, b: {x: b[x] if x in b else a[x] for x in a}

	# Sorts dictionary by key's symbolic length (lengthful's first!), to handle
	# large patterns firstly (i.e. starting with a replacement of "SCH" and then
	# safely replacing "CH"). Returns the sorted list of tuples:
	sort_by_keylen = lambda self, d: sorted(d.items(), key=lambda t: -len(t[0]))

	__version__ = '16.3.9'

	def __init__(self, string='', take_from_cjk=''):

		# If cjk (Chinese-Japan-Korean) flag is enabled, loading “Heavy” Dictionaries:
		if ('c' in take_from_cjk) | ('j' in take_from_cjk) | ('k' in take_from_cjk):
			with Timer():
				self.load_cjk(take_from_cjk)
		self.string = string

	def __str__(self):
		return self.string

	def __getattr__(self, name):
		if (name in self.pairs.keys()) | ('any' in name):
			def wrapper_fn(*args, **kw):
				return self.generic_lang(name, *args, **kw)
			return wrapper_fn
		else:
			raise AttributeError(name)

	def generic_lang(self, langpairs, string=None, override={}):
		if string == None:
			string = self.string
		if (len(langpairs) > 0) & ('any_' in langpairs):
			targetlang = langpairs.replace('any', '').strip()
			langpairs = tuple(x for x in self.pairs.keys() if targetlang in x)
			if len(langpairs) < 1:
				raise AttributeError(name)
		else:
			langpairs = (langpairs,)
		self.sieve(string, langpairs, override)
		return self

	def translate(self, string, langpairs, override={}):
		langpairs = self.overrider(langpairs, override)
		# Preliminary replacing the combinations containing more than one character:
		string = self.replace_patterns(string, langpairs)
		new = []

		# Handling characters from the language compliance matrix, the length of which doesn't exceed 1:
		for i, char in enumerate(string):
			is_upper = char.isupper()
			next_char = string[i+1] if i < len(string)-1 else ''
			next_is_upper = next_char.isupper() if((next_char != ' ') & (next_char != '')) else True
			lower_char = self.safe_lower(char)
			if lower_char in langpairs:
				if is_upper:
					if (len(langpairs[lower_char]) > 1) & (not next_is_upper):
						new.append(langpairs[lower_char].capitalize())
					else:
						new.append(self.safe_upper(langpairs[lower_char]))
				else:
					new.append(langpairs[lower_char])
			else:
				new.append(char)
		return ''.join(new)

	def replace_patterns(self, string, pairs, handle_sigle_chars=False, spaced=False):
		for lp in self.sort_by_keylen(pairs):
			if (not handle_sigle_chars) & (len(lp[0]) < 2):
				continue
			string = string.replace(lp[0], " {} ".format(lp[1]) if spaced else lp[1])
		return string

	def sieve(self, string=None, langpairs=(), override={}):
		# Sieving a bunch of language substitution pairs through the "self.translate" method:
		for langpair in langpairs:
			# If the langpair is from the CJK group, handling additional formalities, like
			# the words separation by the frequency dictionaries
			if ('zh_' in langpair) | ('jp_' in langpair) | ('kr_' in langpair):
				string = self.cjk_processing(string, langpair)

			string = self.translate(
				string=string,
				langpairs=self.pairs[langpair],
				override=override
			)
		self.string = self.refine_output(string)
		return self

	def load_cjk(self, take_from_cjk):
		import json
		if('c' in take_from_cjk):
			# Loading Chinese Ideographs Dictionary (26 653 Ideographs):
			# CJK Unified Ideographs (Common) + CJK Unified Ideographs Extension A (Rare)
			pairs['zh_en'] = json.load(open('zh_dict.json', 'r'))
			# Loading the TPS Frequency Dictionary of Mandarin Chinese
			# (26 704 most frequently used words, for sentences separation):
			pairs['zh_freq'] = open('zh_freq_words.dict', 'r').read().split(',')
		if('j' in take_from_cjk):
			# Loading Standard Japanese Ideographs Hepburn Dictionary
			# (224 Ideographs: Hiragana + Katakana):
			pairs['jp_en'] = json.load(open('jp_dict.json', 'r'))
			# Loading Japanese Kakasi Kanji Decomposition (Kanji-Kana Inversion) Dictionary:
			pairs['jp_decomp'] = json.load(open('jp_kakasi_decomposition.json', 'r'))
			# Loading Japanese Frequency Dictionary (Merged lists from Wiktionary 2013/2015):
			pairs['jp_freq'] = open('jp_freq_words.dict', 'r').read().split(',')
		if('k' in take_from_cjk):
			pass

		return self

	def refine_output(self, string):
		string = re.sub(r'\s+([\]}，；）\)、：？！。，,.!?’”])', r'\1', string)
		string = re.sub(r'([\[{（\(‘“])\s+', r'\1', string)
		return re.sub(r'\s{2,}', ' ', string).strip()

	def cjk_processing(self, string, langpairs):
		if 'zh_' in langpairs:
			words_markers = []
			string = string.replace('{', '{{').replace('}', '}}')
			string = re.sub(r'(\d+)', r' \1 ', string)
			for word in self.pairs['zh_freq']:
				buff = string.replace(word, "{"+str(len(words_markers))+"}")
				if buff != string:
					words_markers.append(" {} ".format(word))
					string = buff
			string = string.format(*words_markers)
			return string
		elif 'jp_' in langpairs:
			words_markers = []
			string = string.replace('{', '{{').replace('}', '}}')
			string = self.replace_patterns(
				string,
				self.pairs['jp_decomp'],
				handle_sigle_chars=True,
				spaced=True
			)
			string = re.sub(r'(\d+)', r' \1 ', string)
			for word in self.pairs['jp_freq']:
				buff = string.replace(word, "{"+str(len(words_markers))+"}")
				if buff != string:
					words_markers.append(" {} ".format(word))
					string = buff
			string = string.format(*words_markers)
			return string

	def custom(self, pairs={}, string=None):
		if (type(pairs) is not dict) | (pairs == {}):
			return self
		if string == None:
			string = self.string
		for pair in pairs:
			string = string.replace(pair, pairs[pair])
		self.string = string
		return self
	replace = custom
	manual = custom

	def languages(self):
		return sorted(((lang, self.aliases[lang]) for lang in self.pairs))
	get_languages = languages
	language_list = languages
	all_languages = languages

	def safe_upper(self, string):
		new = []
		for c in string:
			buff = c.upper()
			new.append( c if(len(buff) > 1) else buff )
		return ''.join(new)

	def safe_lower(self, string):
		new = []
		for c in string:
			buff = c.lower()
			new.append( c if(len(buff) > 1) else buff )
		return ''.join(new)

	def lower(self):
		self.string = self.safe_lower(self.string)
		return self

	def upper(self):
		self.string = self.safe_upper(self.string)
		return self

	def get(self):
		return self.string
	text = get
	get_string = get

	def set(self, string):
		self.string = string
		return self
	set_text = get
	set_string = get

	def slugify(self, separator='-', allow_symbols="-'_~"):
		# You can manually add allowed (and potentially unsafe for a URI) symbols,
		# for example, by calling method allow_symbols="$@:;?=+-&!*'_.,~"
		buffer = self.string.strip()
		allowed_chars = re.compile(r'[^A-Za-z0-9\s{}{}]'.format(separator, allow_symbols))
		doubled_separators = re.compile(separator + r'{2,}')
		buffer = re.sub(allowed_chars, '', buffer)
		buffer = separator.join(buffer.split(' '))
		buffer = re.sub(doubled_separators, separator, buffer)
		return buffer[:2000] # 2000 characters is reasonable maximum for a URI
	get_slug = slugify
	slug = slugify
	url = slugify
	uri = slugify