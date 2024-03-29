# coding=utf-8
lang_aliases = {
	'az_en': 'Azerbaijani → English',	'hy_en': 'Armenian → English',
	'ar_en': 'Arabic → English',		'br_en': 'Burmese → English',
	'cz_en': 'Czech → English',			'de_en': 'Deutsch → English',
	'dv_en': 'Maldivian → English',		'el_en': 'Greek → English',
	'en_ru': 'English → Russian',		'fi_en': 'Finnish → English',
	'fr_en': 'French → English',		'jp_en':	'Japanese → English',
	'hu_en': 'Hungarian → English',		'kr_en':	'Korean → English',
	'la_en': 'Latin → English',			'lt_en': 'Lithuanian → English',
	'lv_en': 'Latvian → English',		'mk_en': 'Makedonian → English',
	'pl_en': 'Polish → English',		'pt_en': 'Portuguese → English',
	'ro_en': 'Romanian → English',		'ru_en': 'Russian → English',
	'sr_en': 'Serbian → English',		'sk_en': 'Slovak → English',
	'th_en': 'Thai → English',			'tk_en': 'Turkmen → English',
	'tr_en': 'Turkish → English',		'vi_en': 'Vietnamese → English',
	'uk_en': 'Ukrainian → English',		'zh_en': 'Chinese → English',
	'symbols_en': 'Unicode Symbols → English',
}

pairs = {
	'symbols_en': {
		'∆': 'delta',				'∞': 'infinity',
		'♥': 'love',				'❤': 'love',
		'♡': 'love',				'✽': 'flower',
		'❃': 'flower',				'✼': 'flower',
		'✻': 'flower',				'♀': 'female',
		'♂': 'male',				'☺': 'smile',
		'☻': 'smile',				'😊': 'smile',
		'😋': 'smile',				'☹': 'frowning',
		'😀': 'laugh',				'😁': 'laugh',
		'😂': 'laugh',				'😃': 'laugh',
		'😄': 'laugh',				'😅': 'laugh',
		'😆': 'laugh',				'😇': 'holy',
		'😈': 'devil',				'😉': 'wink',
		'😌': 'smile',				'😍': 'loved',
		'😎': 'smile',				'😏': 'smirking face',
		'😐': 'neutral face',		'😫': 'tired',
		'😑': 'expressionless',		'😒': 'unamused',
		'😓': 'cold sweat',			'😔': 'pensive face',
		'😕': 'confused',			'😖': 'confounded',
		'😗': 'kissing',			'😙': 'kissing',
		'😘': 'air kiss',			'😛': 'tongue',
		'😜': 'tongue',				'😝': 'tongue',
		'😞': 'disappointed',		'😟': 'worried',
		'😠': 'angry',				'😡': 'angry',
		'😢': 'crying',				'😣': 'persevering',
		'😥': 'disappointed',		'😦': 'frowning',
		'😧': 'anguished',			'😨': 'fearful face',
		'😩': 'wearyface',			'😪': 'sleepyface',
		'😭': 'crying',				'😮': 'wow',
		'😯': 'hushed',				'😱': 'screaming',
		'😲': 'wow',				'😳': 'flushed',
		'😴': 'sleeping',			'😵': 'dizzy',
		'😶': 'silent',				'😷': 'face mask',
		'★': 'star',				'☆': 'star',
		'✪': 'star',				'✫': 'star',
		'✯': 'star',				'✹': 'star',
		'✸': 'star',				'✶': 'star',
		'✷': 'star',				'✵': 'star',
		'✴': 'star',				'✵': 'star',
		'✧': 'star',				'✦': 'star',
		'⍟': 'star',				'⊛': 'star',
		'✰': 'star',				'✭': 'star',
		'٭': 'star',				'✺': 'asterisk',
		'✳': 'asterisk',			'✲': 'asterisk',
		'✱': 'asterisk',			'*': 'asterisk',
		'⁕': 'asterisk',			'﹡': 'asterisk',
		'❂': 'sun',					'=': 'equals',
		'+': 'plus',				'≠': 'unequals',
		'#': 'number',				'№': 'number',
		'~': 'approx',				'&': 'and',
		'|': 'or',					'∑': 'sum',
		'<': 'less than',			'>': 'greater than',
		'˄': 'arrowup',				'˅': 'arrowdown',
		'¤': 'currency',			'@': 'at',
		'∞': 'infinity',			'&': 'and',
		'|': 'or',					'±': 'plusminus',
		'∑': 'sum',					'∫': 'integral',
		'%': 'percent',				'√': 'squareroot',
		'¤': 'currency',			'™': 'trademark',
		'¶': 'pilcrow',				'¼': 'onequarter',
		'½': 'one half',			'¾': 'three quarters',
		'°': 'degree',				'µ': 'micro',
		'®': 'registered mark',		'©': 'copyright',
		'÷': 'divide',				'§': 'section',
		'☎': 'telephone',			'☏': 'telephone',
		'☞': 'pointing index',		'☜': 'pointing index',
		'☛': 'pointing index',		'☚': 'pointing index',
		'☸': 'steering wheel',		'☕': 'coffee',
		'☔': 'umbrella',			'☂': 'umbrella',
		'☢': 'radioactive',			'☣': 'biohazard',
		'☘': 'shamrock',			'☄': 'comet',
		'☠': 'deadly danger',		'☯': 'yin yang',
		'☨': 'lorraine cross',		'☼': 'sun',
		'⎈': 'helm',				'☮': 'peace symbol',
		'☭': 'hammer n sickle',		'☫': 'farsi',
		'☬': 'adi shakti',			'☪': 'star n crescent',
		'☩': 'jerusalem cross',		'☤': 'caduceus',
		'☥': 'ankh',				'☦': 'orthodox cross',
		'♁': 'earth',				'♆': 'neptune',
		'♔': 'white king',			'♚': 'black king',
		'♕': 'white queen',			'♛': 'black queen',
		'♖': 'white rook',			'♜': 'black rook',
		'♗': 'white bishop',		'♝': 'black bishop',
		'♘': 'white knight',		'♞': 'black knight',
		'♙': 'white pawn',			'♟': 'black pawn',
		'♤': 'spade suit',			'♠': 'spade suit',
		'♢': 'diamond suit',		'♦': 'spade suit',
		'♧': 'club suit',			'♣': 'club suit',
		'♩': 'note',				'♪': 'note',
		'♫': 'note',				'♬': 'note',
		'♭': 'music sign',			'♲': 'recycling',
		'♳': 'recycling',			'♴': 'recycling',
		'♵': 'recycling',			'♶': 'recycling',
		'♷': 'recycling',			'♸': 'recycling',
		'♹': 'recycling',			'♺': 'recycling',
		'♻': 'recycling',			'♼': 'recycling',
		'♽': 'recycling',			'♿': 'wheelchair',
		'⚐': 'flag',				'⚑': 'flag',
		'⚓': 'anchor',				'⚔': 'crossed swords',
		'⚕': 'aesculapius',			'⚖': 'scales',
		'⚗': 'alembic',				'⚘': 'flower',
		'⚙': 'gear',				'⚚': 'staff of hermes',
		'⚛': 'atom',				'⚜': 'fleur de lis',
		'⚝': 'star', 				'⚠': 'warning',
		'⚡': 'lightning',			'⚢': 'double female',
		'⚣': 'double male',			'⚤': 'female and male',
		'⚥': 'female and male',		'⚪': 'circle',
		'⚫': 'circle',				'⚬': 'circle',
		'⚭': 'marriage',			'⚮': 'divorce',
		'⚱': 'funeral urn',			'⚳': 'ceres',
		'⚴': 'pallas',				'⚰': 'coffin',
		'⚵': 'juno',				'⚶': 'vesta',
		'⚷': 'chiron',				'⚸': 'black moon',
		'✚': 'cross',				'✙': 'cross',
		'✛': 'cross',				'✜': 'cross',
		'✝': 'latin cross',			'✞': 'latin cross',
		'✟': 'latin cross',			'✐': 'pencil',
		'✏': 'pencil',				'✎': 'pencil',
		'✍': 'writing hand',		'✌': 'victory',
		'✋': 'hand',				'✊': 'fist',
		'✉': 'envelope',			'✈': 'airplane',
		'✇': 'tape drive',			'✆': 'telephone',
		'✅': 'done',				'✄': 'scissors',
		'✃': 'cutting scissors', 	'✂': 'scissors',
		'✁': 'cutting scissors', 	'✓': 'done',
		'✔': 'done',				'✕': 'multiply',
		'✖': 'multiply',			'✗': 'ballot x',
		'✘': 'ballot x',			'➗': 'divide',
		'⚹': 'sextile', 			'…': '...',
		'$': 'USD',		'€': 'EUR',		'₽': 'RUB',		'₢': 'BRN',
		'₣': 'FRF',		'£': 'GBP',		'₤': 'ITL',		'₦': 'NGN',
		'₧': 'ESP',		'₩': 'KRW',		'₪': 'ILS',		'₫': 'VND',
		'₭': 'LAK',		'₮': 'MNT',		'₯': 'GRD',		'₱': 'ARS',
		'₲': 'PYG',		'₳': 'ARA',		'₴': 'UAH',		'₵': 'GHS',
		'¢': 'cent',	'¥': 'CNY',		'元': 'CNY',		'円': 'YEN',
		'﷼': 'IRR',		'₠': 'EWE',		'฿': 'THB',		'₺': 'TRY',
		'₨': 'INR',		'₹': 'INR',		'₰': 'PF',		'₡': 'CRC',
		'৳': 'BDT',
	},

	'ar_en': { # Arabic → English
		'ا': 'a',	'أ': 'a',	'إ': 'i',	'ـ': 'a',
		'آ': 'aa',	'ى': 'a',	'ء': 'a',	'ع': 'a',
		'ﺒ': 'b',	'ﺐ': 'b',	'ﺑ': 'b',	'ﺏ': 'b',
		'ﺖ': 't',	'ﺘ': 't',	'ﺗ': 't',	'ﺕ': 't',
		'ﺚ': 't',	'ﺜ': 't',	'ﺛ': 't',	'ﺙ': 't',
		'ﺞ': 'dj',	'ﺠ': 'dj',	'ﺟ': 'dj',	'ﺝ': 'dj',
		'ﺢ': 'h', 	'ﺤ': 'h',	'ﺣ': 'h',	'ﺡ': 'h',
		'ﺦ': 'h',	'ﺨ': 'h',	'ﺧ': 'h',	'ﺥ': 'h',
		'ﺪ': 'd',	'ﺩ': 'd',	'ﺬ': 'z',	'ﺫ': 'z',
		'ﺮ': 'r',	'ﺭ': 'r',	'ﺰ': 'z',	'ﺯ': 'z',
		'ﺲ': 's',	'ﺴ': 's',	'ﺱ': 's',	'ﺳ': 's',
		'ﺶ': 'sh',	'ﺸ': 'sh',	'ﺷ': 'sh',	'ﺵ': 'sh',
		'ﺺ': 's',	'ﺼ': 's',	'ﺻ': 's',	'ﺹ': 's',
		'ﺾ': 'd',	'ﻀ': 'd',	'ﺿ': 'd',	'ﺽ': 'd',
		'ﻂ': 't',	'ﻄ': 't',	'ﻃ': 't',	'ﻁ': 't',
		'ﻆ': 'z',	'ﻈ': 'z',	'ﻇ': 'z',	'ﻅ': 'z',
		'ﻊ': 'aa',	'ﻌ': 'aa',	'ﻋ': 'aa',	'ﻉ': 'aa',
		'ﻎ': 'za',	'ﻐ': 'za',	'ﻏ': 'za',	'ﻍ': 'za',
		'ﻒ': 'f',	'ﻔ': 'f',	'ﻓ': 'f',	'ﻑ': 'f',
		'ﻖ': 'q',	'ﻘ': 'q',	'ﻗ': 'q',	'ﻕ': 'q',
		'ﻚ': 'k',	'ﻜ': 'k',	'ﻛ': 'k',	'ﻙ': 'k',
		'ﻞ': 'l',	'ﻠ': 'l',	'ﻟ': 'l',	'ﻝ': 'l',
		'ﻢ': 'm',	'ﻤ': 'm',	'ﻣ': 'm',	'ﻡ': 'm',
		'ﻦ': 'n',	'ﻨ': 'n',	'ﻧ': 'n',	'ﻥ': 'n',
		'ﻪ': 'h',	'ﻬ': 'h',	'ﻫ': 'h',	'ﻩ': 'h',
		'ﻮ': 'w',	'ﻭ': 'w',	'ﻲ': 'y',	'ﻴ': 'y',
		'ﻳ': 'y',	'ﻱ': 'y',	'چ': 'ch',	'گ': 'g',
		'ڴ': 'n',	'پ': 'p',	'ژ': 'zh',	'ڥ': 'v',
		'ۋ': 'v',	'ڤ': 'v',	'ؤ': 'u',	'ئ': 'e',
		'ب': 'b',	'ت': 't',	'ث': 'th',	'ج': 'j',
		'ح': 'h',	'خ': 'kh',	'د': 'd',	'ذ': 'th',
		'ر': 'r',	'ز': 'z',	'س': 's',	'ش': 'sh',
		'ص': 's',	'ض': 'dh',	'ط': 't',	'ظ': 'z',
		'غ': 'gh',	'ف': 'f',	'ق': 'q',	'ك': 'k',
		'ل': 'l',	'م': 'm',	'ن': 'n',	'ه': 'h',
		'و': 'oo',	'ي': 'ay',	'ة': 'h',	'ﻻ': 'la',
		'ﻷ': 'laa',	'ﻹ': 'lai',	'ﻵ': 'laa',

		# Diactrics
		'َ': 'a',	'ً': 'an',	'ِ': 'e',	'ٍ': 'en',
		'ُ': 'u',	'ٌ': 'on',	'ْ': '',		'ّٰ':'a',

		# Numbers
		'٠': '0',	'١': '1',	'٢': '2',	'٣': '3',
		'٤': '4',	'٥': '5',	'٦': '6',	'٧': '7',
		'٨': '8',	'٩': '9',
	},

	'az_en': { # Azerbaijani → English
		'ç': 'c',	'ə': 'a',	'ğ': 'g',	'ı': 'y',
		'ö': 'o',	'ş': 'sh',	'ü': 'u',	'j': 'zh',
		'y': 'dj',
		# legacy set:
		'ä': 'a',	'ƣ': 'g',	'ь': 'y',	'ƶ': 'zh',
		'ɵ': 'o',	'з': 'sh',
	},

	'br_en': { # Burmese → English
		# consonants
		'က': 'k',	'ခ': 'kh',	'ဂ': 'g',	'ဃ': 'ga',
		'င': 'ng',	'စ': 's',	'ဆ': 'sa',	'ဇ': 'z',
		'စျ': 'za',	'ည': 'ny',	'ဋ': 't',	'ဌ': 'ta',
		'ဍ': 'd',	'ဎ': 'da',	'ဏ': 'na',	'တ': 't',
		'ထ': 'ta',	'ဒ': 'd',		'ဓ': 'da',	'န': 'n',
		'ပ': 'p',	'ဖ': 'pa',	'ဗ': 'b',	'ဘ': 'ba',
		'မ': 'm',	'ယ': 'y',	'ရ': 'ya',	'လ': 'l',
		'ဝ': 'w',	'သ': 'th',	'ဟ': 'h',	'ဠ': 'la',
		'အ': 'a',

		# consonant character combos
		'ြ': 'y',			'ျ': 'ya',			'ွ': 'w',
		'ြွ': 'yw',			'ျွ': 'ywa',		'ှ': 'h',

		# independent vowels
		'ဧ': 'e',			'၏': '-e',			'ဣ': 'i',
		'ဤ': '-i',			'ဉ': 'u',			'ဦ': '-u',
		'ဩ': 'aw',			'သြော': 'aw',	'ဪ': 'aw',

		# numbers
		'၀': '0',	'၁': '1',	'၂': '2',		'၃': '3',
		'၄': '4',	'၅': '5',	'၆': '6',	'၇': '7',
		'၈': '8',	'၉': '9',

		# virama and tone marks which are silent in transliteration
		'္': '',		'့': '',		'း': '',
	},

	'cz_en': { # Czech → English
		'á': 'a',	'č': 'ch',	'ď': 'd',	'é': 'e',
		'ě': 'e',	'ň': 'n',	'ó': 'o',	'ř': 'r',
		'š': 'sh',	'ť': 't',	'ů': 'u',	'ú': 'u',
		'ž': 'zh',	'ý': 'i',	'í': 'i',	'ch': 'h',
		'Ch': 'H',	'CH': 'H',	'cH': 'h',
	},

	'de_en': { # Deutsch → English
		'ä': 'a',	'ö': 'o',	'ß': 'ss',	'ü': 'u',
	},

	'dv_en': { # Dhivehi / Maldivian → English
		'ހ': 'h',		'ށ': 'sh',	'ނ': 'n',	'ރ': 'r',
		'ބ': 'b',		'ޅ': 'lh',	'ކ': 'k',		'އ': 'a',
		'ވ': 'v',		'މ': 'm',		'ފ': 'f',		'ދ': 'dh',
		'ތ': 'th',	'ލ': 'l',		'ގ': 'g',		'ޏ': 'gn',
		'ސ': 's',	'ޑ': 'd',		'ޒ': 'z',		'ޓ': 't',
		'ޔ': 'y',		'ޕ': 'p',		'ޖ': 'j',		'ޗ': 'ch',
		'ޘ': 'tt',	'ޙ': 'hh',	'ޚ': 'kh',	'ޛ': 'th',
		'ޜ': 'z',		'ޝ': 'sh',	'ޞ': 's',	'ޟ': 'd',
		'ޠ': 't',	'ޡ': 'z',		'ޢ': 'a',		'ޣ': 'gh',
		'ޤ': 'q',		'ޥ': 'w',		'ަ': 'a',	'ާ': 'aa',
		'ި': 'i',	'ީ': 'ee',	'ު': 'u',	'ޫ': 'oo',
		'ެ': 'e',	'ޭ': 'ey',	'ޮ': 'o',	'ޯ': 'oa',
		'ް': '',
	},

	'el_en': { # Greek → English
		'α': 'a',	'β': 'v',	'γ': 'g',	'δ': 'd',
		'ε': 'e',	'ζ': 'z',	'η': 'i',	'θ': 'th',
		'ι': 'i',	'κ': 'k',	'λ': 'l',	'μ': 'm',
		'ν': 'n',	'ξ': 'ks',	'ο': 'o',	'π': 'p',
		'ρ': 'r',	'σ': 's',	'τ': 't',	'υ': 'y',
		'φ': 'f',	'χ': 'x',	'ψ': 'ps',	'ω': 'o',
		'ά': 'a',	'έ': 'e',	'ί': 'i',	'ό': 'o',
		'ύ': 'y',	'ή': 'i',	'ώ': 'o',	'ς': 's',
		'ϊ': 'i',	'ΰ': 'y',	'ϋ': 'y',	'ΐ': 'i',
	},

	'en_ru': { # English → Russian
		'a': 'а',	'b': 'б',	'c': 'к',	'd': 'д',
		'e': 'е',	'f': 'ф',	'g': 'г',	'h': 'х',
		'i': 'и',	'j': 'дж',	'k': 'к',	'l': 'л',
		'm': 'м',	'n': 'н',	'o': 'о',	'p': 'п',
		'q': 'к',	'r': 'р',	's': 'с',	't': 'т',
		'u': 'у',	'v': 'в',	'w': 'в',	'x': 'кс',
		'y': 'й',	'z': 'з',	'`': 'ь',	'``': 'ъ',
		'sch': 'щ',	'Sch': 'Щ',	'SCH': 'Щ', 'sCH': 'Щ',
		'scH': 'щ',	'zh': 'ж',	'zH': 'ж',	'Zh': 'Ж',
		'ZH': 'Ж',	'ts': 'ц',	'Ts': 'Ц',	'tS': 'ц',
		'TS': 'Ц',	'ch': 'ч',	'Ch': 'Ч',	'CH': 'Ч',
		'cH': 'ч',	'sh': 'ш',	'Sh': 'Ш',	'SH': 'Ш',
		'sH': 'ш',	'yu': 'ю',	'yU': 'ю',	'Yu': 'Ю',
		'YU': 'Ю',	'ya': 'я',	'Ya': 'Я',	'yA': 'я',
		'YA': 'Я',	'Yo': 'Ё',	'YO': 'Ё',	'yo': 'ё',
		'yO': 'ё',	'th': 'з',	'Th': 'З',	'TH': 'З',
		'tH': 'з',	'ee': 'и',	'Ee': 'И',	'EE': 'И',
		'eE': 'и',	'ck': 'к',	'Ck': 'К',	'CK': 'К',
		'cK': 'к',	'ce': 'се',	'CE': 'СЕ',	'Ce':	'Се',
		'cE':	'сЕ',	'ci': 'си',	'CI': 'СИ',	'Ci':	'Си',
		'cI':	'сИ',	'cy': 'сай','CY': 'САЙ','Cy':	'Сай',
		'cY':	'сАЙ',
	},

	'fi_en': { # Finnish → English
		'å': 'a',	'ä': 'a',	'ö': 'o',	'š': 'sh',
		'ž': 'zh',
	},

	'fr_en': { # French → English
		'é': 'e',	'à': 'a',	'è': 'e',	'ù': 'u',
		'â': 'a',	'ê': 'e',	'î': 'i',	'ô': 'o',
		'û': 'u',	'ç': 's',	'ë': 'e', 	'ï': 'i',
		'ü': 'u', 	'ÿ': 'y',	'æ': 'ae',	'œ': 'oe',
	},

	'hu_en': { # Hungarian → English
		'ä': 'a',	'á': 'a',	'é': 'e',	'ë': 'e',
		'í': 'i',	'ö': 'o',	'ó': 'o',	'ő': 'o',
		'ü': 'u',	'ű': 'u',	'ú': 'u',
	},

	'hy_en': { # Armenian → English
		'ա': 'a',	'բ': 'b',	'գ': 'g',	'դ': 'd',
		'ե': 'e',	'զ': 'z',	'է': 'e',	'ը': 'e',
		'թ': 't',	'ժ': 'zh',	'ի': 'i',	'լ': 'l',
		'խ': 'kh',	'ծ': 'ts',	'կ': 'k',	'հ': 'h',
		'ձ': 'j',	'ղ': 'l',	'ճ': 'tsh',	'մ': 'm',
		'յ': 'y',	'ն': 'n',	'շ': 'sh',	'ո': 'o',
		'չ': 'сh',	'պ': 'p',	'ջ': 'j',	'ռ': 'r',
		'ս': 's',	'վ': 'v',	'տ': 't',	'ր': 'r',
		'ց': 'ts',	'ւ': 'u',	'փ': 'ph',	'ք': 'kh',
		'և': 'ev',	'օ': 'o',	'ֆ': 'f',
	},

	'la_en': { # Latin → English
		# Old Italic Script
		'𐌀': 'a',	'𐌁': 'b',	'𐌂': 'c',	'𐌃': 'd',
		'𐌄': 'e',	'𐌅': 'v',	'𐌆': 'z',		'𐌇': 'h',
		'𐌉': 'i',		'𐌊': 'k',	'𐌋': 'l',		'𐌌': 'm',
		'𐌍': 'n',	'𐌑': 'sh',	'𐌏': 'o',	'𐌈': 'th',
		'𐌎': 'sh',	'𐌐': 'p',	'𐌒': 'q',	'𐌓': 'r',
		'𐌔': 's',		'𐌕': 't',	'𐌖': 'u',	'𐌗': 'x',
		'𐌘': 'ph',	'𐌙': 'kh',	'𐌚': 'f',		'𐌞': 'u',
		'𐌡': 'v',	'𐌜': 'ch',	'𐌢': 'x',	'𐌝': 'i',
	},

	'lt_en': { # Lithuanian → English
		'ą': 'a',	'č': 'ch',	'c': 'ts',	'ę': 'e',
		'ė': 'e',	'į': 'i',	'y': 'i',	'š': 'sh',
		'ų': 'u',	'ū': 'u',	'ž': 'zh'
	},

	'lv_en': { # Latvian → English
		'ā': 'a',	'č': 'c',	'ē': 'e',	'ģ': 'g',
		'ī': 'i',	'ķ': 'k',	'ļ': 'l',	'ņ': 'n',
		'š': 's',	'ū': 'u',	'ž': 'z',
	},

	'mk_en': { # Makedonian → English
		'ќ': 'kj',	'љ': 'lj',	'њ': 'nj',	'č': 'ch',
		'а': 'a',	'б': 'b',	'в': 'v',	'г': 'g',
		'ǵ': 'g',	'д': 'd',	'ѓ': 'g',	'е': 'e',
		'ж': 'zh',	'з': 'z',	'ѕ': 'dz',	'и': 'i',
		'к': 'k',	'л': 'l',	'м': 'm',	'н': 'n',
		'о': 'o',	'п': 'p',	'р': 'r',	'с': 's',
		'т': 't',	'у': 'u',	'ф': 'f',	'х': 'h',
		'ц': 'ts',	'ч': 'ch',	'џ': 'dzh',	'ш': 'sh',
		'š': 'sh',	'ḱ': 'k',	'j': 'iy',	'è': 'e',
		'ѝ': 'i',	'ô': 'o',	'ć': 'ts',	'ž': 'zh'
	},

	'pl_en': { # Polish → English
		'ą': 'a',	'ć': 'ts',	'ę': 'e',	'ł': 'l',
		'ń': 'n',	'ó': 'o',	'ś': 's',	'ź': 'z',
		'ż': 'zh',
	},

	'pt_en': { # Portuguese → English
		'á': 'a',	'â': 'a',	'ã': 'a',	'à': 'a',
		'ç': 's',	'é': 'e',	'ê': 'e',	'í': 'i',
		'ó': 'o',	'ô': 'o',	'õ': 'o',	'ú': 'u',
	},

	'ro_en': { # Romanian → English
		'ă': 'a',	'ș': 'sh',	'ş': 's',	'ț': 'ts',
		'ţ': 't',	'â': 'i',	'î': 'i',	'j': 'zh',
	},

	'ru_en': { # Russian → English
		'а': 'a',	'б': 'b',	'в': 'v',	'г': 'g',
		'д': 'd',	'е': 'e',	'з': 'z',	'и': 'i',
		'й': 'y',	'к': 'k',	'л': 'l',	'м': 'm',
		'н': 'n',	'о': 'o',	'п': 'p',	'р': 'r',
		'с': 's',	'т': 't',	'у': 'u',	'ф': 'f',
		'ц': 'c',	'ы': 'y',	'э': 'e',	'х': 'h',
		'ь': '',		'ъ': '',		'ё': 'yo',	'ж': 'zh',
		'ч': 'ch',	'ш': 'sh',	'щ': 'sch',	'ю': 'yu',
		'я': 'ya',
	},

	'sr_en': { # Serbian → English
		'а': 'a',	'б': 'b',	'в': 'v',	'г': 'g',
		'д': 'd',	'е': 'e',	'ж': 'zh',	'з': 'z',
		'и': 'i',	'j': 'iy',	'к': 'k',	'л': 'l',
		'м': 'm',	'н': 'n',	'о': 'o',	'п': 'p',
		'р': 'r',	'с': 's',	'т': 't',	'у': 'u',
		'ф': 'f',	'х': 'h',	'ц': 'ts',	'ч': 'ch',
		'ш': 'sh',	'љ': 'lj',	'њ': 'nj',	'đ': 'dj',
		'ž': 'zh',	'ђ': 'dj',	'џ': 'dj',	'š': 'sh',
		'č': 'ch',
	},

	'sk_en': { # Slovak → English
		'ä': 'a',	'á': 'a',	'č': 'ch',	'ď': 'd',
		'é': 'e',	'ĺ': 'll',	'ľ': 'l',
		'ň': 'n',	'ó': 'o',	'ô': 'uo',	'ŕ': 'rr',
		'š': 'sh',	'ť': 't',	'ú': 'u',	'ý': 'i',
		'ž': 'zh',
	},

	'th_en': { # Thai → English
		# Vowels
		'ะ': 'a',		'ั': 'a',		'อา': 'a',
		'ิ': 'i',		'ึ': 'ue',		'อํา': 'am',	'อู': 'u',
		'ุ': 'u',		'เอะ': 'e',		'เอ': 'e',		'แอะ': 'ae',
		'แอ': 'ae',		'็อ': 'o',		'เอือ': 'ua',	'ัวะ': 'ua',
		'ิว': 'io',		'ัย': 'ai', 	'ใ': 'ai',		'ไอย': 'ai',
		'อัย': 'ai',
		'็อย': 'oi',	'ุย': 'ui',		'า': 'a',		'ไอ': 'ai',
		'ี': 'i',		'ี': 'i',		'ือ': 'ue',		'ื': 'ue',
		'ู': 'u',		'เ': 'e',		'ํา': 'am',		'ใอ': 'ai',
		'แ':	'ae',		'โ': 'o',		'อัว': 'ua',	'เออะ': 'ua',
		'อ': 'o',		'็': 'o',		'อัวะ': 'ua',	'อิ': 'i',
		'อุ': 'u',		'อื': 'u',		'อึ':	'u',		'อี': 'i',
		'ัว': 'ua',		'ว': 'ua',		'าว': 'ao',		'าย': 'ai',
		'เอย': 'oei',	'วย': 'uai',	'ออย': 'qui',	'อาย':'ai',
		'โอย': 'oi',	'อุย': 'ui',	'อาว': 'ao',	'เอา': 'ao',

		'َِ': '',	'์': '',		'่': '',		'้': '', '๊': '', #???

		# Extra vowels
		'ำ': 'am',		'ฤ': 'ri',		'ฦ': 'lue',		'ฤๅ': 'rue',
		'ฦๅ': 'lue',	'ไ': 'ai',		'ฤา': 'ru',		'เอีย': 'ia',
		'เอยะ': 'ia',	'ออ': 'o',

		# Consonants
		'ก': 'k',	'ข': 'kh',	'ฃ': 'kh',	'ค': 'kh',
		'ฅ': 'kh',	'ฆ': 'kh',	'ง': 'ng',	'จ': 'ch',
		'ฉ': 'ch',	'ช': 'ch',	'ซ': 's',	'ฌ': 'ch',
		'ญ': 'y',	'ฎ': 'd',	'ฏ': 't',	'ฐ': 'th',
		'ฑ': 'th',	'ฒ': 'th',	'ณ': 'n',	'ด': 'd',
		'ต': 't',	'ถ': 'th',	'ท': 'th',	'ธ': 'th',
		'น': 'n',	'บ': 'b',	'ป': 'p',	'ผ': 'ph',
		'ฝ': 'f',	'พ': 'ph',	'ฟ': 'f',	'ภ': 'ph',
		'ม': 'm',	'ย': 'y',	'ร': 'r',	'ล': 'l',
		'ว': 'w',	'ศ': 's',	'ษ': 's',	'ส': 's',
		'ห': 'h',	'ฬ': 'l',	'ฮ': 'h',
	},

	'tk_en': { # Turkmen → English
		'ä': 'a',	'ç': 'ch',	'ň': 'n',	'ö': 'o',
		'ş': 'sh',	'ž': 'zh',	'ü': 'u',	'ý': 'y',
	},

	'tr_en': { # Turkish → English
		'ç': 'ch',	'ğ': 'g',	'ı': 'y',	'ö': 'o',
		'ň': 'n',	'ş': 'sh',	'ü': 'u',	'ī': 'i',
		'â': 'a',	'û': 'u',	'î': 'i'
	},

	'vi_en': { # Vietnamese → English
		'ả': 'a',		'ẳ': 'a',		'ẩ': 'a',		'đ': 'd',
		'ẹ': 'e',	'ẽ': 'e',	'ẻ': 'e',		'ế': 'e',
		'ề': 'e',		'ệ': 'e',	'ễ': 'e',		'ể': 'e',
		'ọ': 'o',	'ố': 'o',		'ồ': 'o',		'ổ': 'o',
		'ộ': 'o',	'ỗ': 'o',		'ơ': 'o',	'ớ': 'o',
		'ờ': 'o',	'ợ': 'o',	'ỡ': 'o',	'ở': 'o',
		'ị': 'i',	'ĩ': 'i',	'ỉ': 'i',		'Ỉ': 'i',
		'ủ': 'u',		'ụ': 'u',	'ũ': 'u',	'ư': 'u',
		'ứ': 'u',	'ừ': 'u',	'ự': 'u',	'ữ': 'u',
		'ử': 'u',		'Ử': 'u',	'ỷ': 'y',		'Ỷ': 'y',
		'ỳ': 'y',	'ỵ': 'y',	'ỹ': 'y',	'ạ': 'a',
		'ấ': 'a',		'ầ': 'a',		'ậ': 'a',	'ẫ': 'a',
		'ắ': 'a',		'ằ': 'a',	'ặ': 'a',	'ẵ': 'a',
		'á': 'a'
	},

	'uk_en': { # Ukrainian → English
		'а': 'a',	'б': 'b',	'в': 'v',	'г': 'g',
		'ґ': 'g',	'д': 'd',	'є': 'ye',	'е': 'e',
		'ж': 'zh',	'з': 'z',	'и': 'i',	'ї': 'yi',
		'і': 'i',	'й': 'y',	'к': 'k',
		'л': 'l',	'м': 'm',	'н': 'n',	'о': 'o',
		'п': 'p',	'р': 'r',	'с': 's',	'т': 't',
		'у': 'u',	'ф': 'f',	'х': 'h',	'ц': 'ts',
		'ы': 'y',	'ь': '`',	'ч': 'ch',	'ш': 'sh',
		'щ': 'sch',	'ю': 'yu',	'я': 'ya',
	}
}