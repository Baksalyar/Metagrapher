import unittest
from index import Metagrapher

class LangSpecificTests(unittest.TestCase):

	def test_DeEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'',
			'',
			'',
			'',

			'',
			'',
			'',
			'',
		]
		control_set = [
			'',
			'',
			'',
			'',

			'',
			'',
			'',
			'',
		]
		resulting_set = [mg.de_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_ArEn_Transliteration(self):
		pass

	def test_AzEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'abcçdeəfgğƣhxıьijkqlmnoöɵprsştuüvyz',
			'ABCÇDEƏFGĞƢHXIЬIJKQLMNOÖƟPRSŞTUÜVYZ',
			'AbCçDeƏfGğƢhXıЬiJkQlMnOöƟpRsŞtUüVyZ',
			'aBcÇdEəFgĞƣHxIьIjKqLmNoÖɵPrSşTuÜvYz',

			'Ağıllı düşmən nadan dostdan yaxşıdır',
			'Ot kökü üstə bitər',
			'Yetənə yetir, yetməyənə bir daş atır',
			'Tazıya tut deyir, dovşana qaç',
		]
		control_set = [
			'abccdeafggghxyyizhkqlmnoooprsshtuuvdjz',
			'ABCCDEAFGGGHXIYIZHKQLMNOOOPRSSHTUUVDJZ',
			'AbCcDeAfGgGhXyYiZhkQlMnOoOpRsShtUuVdjZ',
			'aBcCdEaFgGgHxIyIzhKqLmNoOoPrSshTuUvDjz',

			'Agylly dushman nadan dostdan djaxshydyr',
			'Ot koku usta bitar',
			'Djetana djetir, djetmadjana bir dash atyr',
			'Tazydja tut dedjir, dovshana qac',
		]
		resulting_set = [mg.az_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_BrEn_Transliteration(self):
		pass

	def test_CzEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzž',
			'AÁBCČDĎEÉĚFGHCHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ',
			'AáBcČdĎeÉěFgHcHiÍjKlMnŇoÓpQrŘsŠtŤuÚůVwXyÝzŽ',
			'aÁbCčDďEéĚfGhChIíJkLmNňOóPqRřSšTťUúŮvWxYýZž',

			'Ber rád, když dávají',
			'S chutí do toho a půl je hotovo',
			'Strpení přináší spasení',
			'Vlas má svůj stín',
		]
		control_set = [
			'aabcchddeeefghhiijklmnnoopqrrsshttuuuvwxyizzh',
			'AABCCHDDEEEFGHHIIJKLMNNOOPQRRSSHTTUUUVWXYIZZH',
			'AaBcChdDeEeFgHhiIjKlMnNoOpQrRsShtTuUuVwXyIzZH',
			'aAbCchDdEeEfGhHIiJkLmNnOoPqRrSshTtUuUvWxYiZzh',

			'Ber rad, kdyzh davaji',
			'S huti do toho a pul je hotovo',
			'Strpeni prinashi spaseni',
			'Vlas ma svuj stin',
		]
		resulting_set = [mg.cz_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_DeEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'aäbcdefghijklmnoöpqrstuüvwxyzß',
			'AÄBCDEFGHIJKLMNOÖPQRSTUÜVWXYZ',
			'aÄbCdEfGhIjKlMnOöPqRsTuÜvWxYz',
			'AäBcDeFgHiJkLmNoÖpQrStUüVwXyZß',

			'Auf einen großen Klotz gehört ein großer Keil',
			'Das Weib ist des Mannes größtes Glück oder Unglück',
			'Die Arznei ist oft ärger als das Übel',
			'Mancher küßt die Hand, die er abbhauen möchte',
		]
		control_set = [
			'aabcdefghijklmnoopqrstuuvwxyzss',
			'AABCDEFGHIJKLMNOOPQRSTUUVWXYZ',
			'aAbCdEfGhIjKlMnOoPqRsTuUvWxYz',
			'AaBcDeFgHiJkLmNoOpQrStUuVwXyZss',

			'Auf einen grossen Klotz gehort ein grosser Keil',
			'Das Weib ist des Mannes grosstes Gluck oder Ungluck',
			'Die Arznei ist oft arger als das Ubel',
			'Mancher kusst die Hand, die er abbhauen mochte',
		]
		resulting_set = [mg.de_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_DvEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'ހށނރބޅކއވމފދތލގޏސޑޒޓޔޕޖޗ',
			'ަާިީުޫެޭޮޯް',

			'ހުރިހާ އިންސާނުން ވެސް އުފަންވަނީ، ދަރަޖަ',
			'އާއި ޙައްޤު ތަކުގައި މިނިވަންކަމާއި ހަމަހަމަކަން',
			'ލިބިގެންވާ ބައެއްގެ ގޮތުގައެވެ. އެމީހުންނަށް ހެޔޮ',
			'ވިސްނުމާއި ހެޔޮ ބުއްދީގެ ބާރު ލިބިގެން ވެއެވެ',
		]
		control_set = [
			'hshnrblhkavmfdhthlggnsdztypjch',
			'aaaieeuooeeyooa',

			'hurihaa ainsaanun ves aufanvanee، dharaja',
			'aaaai hhaaqu thakugaai minivankamaaai hamahamakan',
			'libigenvaa baaeage gothugaaeve. aemeehunnash heyo',
			'visnumaaai heyo buadheege baaru libigen veaeve',
		]
		resulting_set = [mg.dv_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_ElEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'αβγδεζηθικλlμνξοπρστυφχψωάέίόύήώςϊΰϋΐ',
			'ΑΒΓΔΕΖΗΘΙΚΛLΜΝΞΟΠΡΣΤΥΦΧΨΩΆΈΊΌΎΉΏΣΪΰΫΐ',
			'αΒγΔεΖηΘιΚλLμΝξΟπΡσΤυΦχΨωΆέΊόΎήΏςΪΰΫΐ',
			'ΑβΓδΕζΗθΙκΛlΜνΞοΠρΣτΥφΧψΩάΈίΌύΉώΣϊΰϋΐ',

			'Τα μαγειρεμένα κρεμμύδια, χωρίς τη σάλτσα τους, μπορούν να προστεθούν σε ομελέτες',
			'Η γλώσσα κόκαλα δεν έχει, αλλά κόκαλα τσακίζει',
			'Τα μεγάλα πνεύματα συναντώνται',
		]
		control_set = [
			'avgdezithikllmnksoprstyfxpsoaeioyiosiyyi',
			'AVGDEZITHIKLLMNKSOPRSTYFXPSOAEIOYIOSIyYi',
			'aVgDeZiThiKlLmNksOpRsTyFxPsoAeIoYiOsIyYi',
			'AvGdEzIthIkLlMnKsoPrStYfXpsOaEiOyIoSiyyi',

			'Ta mageiremena kremmydia, xoris ti saltsa toys, mporoyn na prostethoyn se omeletes',
			'I glossa kokala den exei, alla kokala tsakizei',
			'Ta megala pneymata synantontai',
		]
		resulting_set = [mg.el_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_EnRu_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'abcdefghijklmnopqrstuvwxyz',
			'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
			'AbCdEfGhIjKlMnOpQrStUvWxYz',
			'aBcDeFgHiJkLmNoPqRsTuVwXyZ',

			'pischa dlya uma PISCHA DLYA UMA',
			'zhit` schastlivo i ne tuzhit`',
			'Yuliya Checherina yulya checherina',
			'No man is an island',
			'Hope for the best, but prepare for the worst',
			'Keep your friends close and your enemies closer',
		]
		control_set = [
			'абкдефгхиджклмнопкрстуввксйз',
			'АБКДЕФГХИДЖКЛМНОПКРСТУВВКСЙЗ',
			'АбКдЕфГхИджКлМнОпКрСтУвВксЙз',
			'аБкДеФгХиДжкЛмНоПкРсТуВвКсйЗ',

			'пища для ума ПИЩА ДЛЯ УМА',
			'жить щастливо и не тужить',
			'Юлия Чечерина юля чечерина',
			'Но ман ис ан исланд',
			'Хопе фор зе бест, бут препаре фор зе ворст',
			'Кип ёур фриендс клосе анд ёур енемиес клосер',
		]
		resulting_set = [mg.en_ru(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_FiEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'abcdefghijklmnopqrstuvwxyzåäöžš',
			'ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖŽŠ',
			'aBcDeFgHiJkLmNoPqRsTuVwXyZåÄöŽš',
			'AbCdEfGhIjKlMnOpQrStUvWxYzÅäÖžŠ',

			'Ei pidä tehdä kärpäsestä härkää',
			'Joka menneitä muistelee, sitä tikulla silmään',
			'On vähäkin tyhjää parempi',
			'Sitä niittää mitä kylvää',
		]
		control_set = [
			'abcdefghijklmnopqrstuvwxyzaaozhsh',
			'ABCDEFGHIJKLMNOPQRSTUVWXYZAAOZHSH',
			'aBcDeFgHiJkLmNoPqRsTuVwXyZaAoZhsh',
			'AbCdEfGhIjKlMnOpQrStUvWxYzAaOzhSH',

			'Ei pida tehda karpasesta harkaa',
			'Joka menneita muistelee, sita tikulla silmaan',
			'On vahakin tyhjaa parempi',
			'Sita niittaa mita kylvaa',
		]
		resulting_set = [mg.fi_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_FrEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'aàâæbcçdeéèêëfghiîïjklmnoôœpqrstuùûüvwxyÿz',
			'AÀÂÆBCÇDEÉÈÊËFGHIÎÏJKLMNOÔŒPQRSTUÙÛÜVWXYŸZ',
			'aÀâÆbCçDeÉèÊëFgHiÎïJkLmNoÔœPqRsTuÙûÜvWxYÿZ',
			'AàÂæBcÇdEéÈêËfGhIîÏjKlMnOôŒpQrStUùÛüVwXyŸz',

			'À qui il a été beaucoup donné, il sera beaucoup demandé',
			'A qui la tête fait mal, souffre par tout le corps',
			'Ce qui croît soudain, périt le lendemain',
		]
		control_set = [
			'aaaaebcsdeeeeefghiiijklmnoooepqrstuuuuvwxyyz',
			'AAAAEBCSDEEEEEFGHIIIJKLMNOOOEPQRSTUUUUVWXYYZ',
			'aAaAebCsDeEeEeFgHiIiJkLmNoOoePqRsTuUuUvWxYyZ',
			'AaAaeBcSdEeEeEfGhIiIjKlMnOoOepQrStUuUuVwXyYz',

			'A qui il a ete beaucoup donne, il sera beaucoup demande',
			'A qui la tete fait mal, souffre par tout le corps',
			'Ce qui croit soudain, perit le lendemain',
		]
		resulting_set = [mg.fr_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_HyEn_Transliterateion(self):
		mg = Metagrapher()
		testing_set = [
			'աբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքևօֆ',
			'ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔևՕՖ',
			'աԲգԴեԶէԸթԺիԼխԾկՀձՂճՄյՆշՈչՊջՌսՎտՐցՒփՔևՕֆ',
			'ԱբԳդԵզԷըԹժԻլԽծԿհՁղՃմՅնՇոՉպՋռՍվՏրՑւՓքևօՖ',

			'Արևն ամպի տակ չի մնայ',
			'Խնձորը ծառից հեռու չի ընկնում',
			'Կարմիր կովը կաշին չի փոխի',
			'Ուշ լինի, (ա)նուշ լինի',
		]
		control_set = [
			'abgdezeetzhilkhtskhjltshmynshoсhpjrsvtrtsuphkhevof',
			'ABGDEZEETZHILKHTSKHJLTSHMYNSHOСHPJRSVTRTSUPHKhevOF',
			'aBgDeZeEtZhiLkhTskHjLtshMyNshOсhPjRsVtRtsUphKhevOf',
			'AbGdEzEeTzhIlKhtsKhJlTshmYnShoСhpJrSvTrTsuPhkhevoF',

			'Arevn ampi tak сhi mnay',
			'Khnjore tsarits herou сhi enknoum',
			'Karmir kove kashin сhi phokhi',
			'Oush lini, (a)noush lini',
		]
		resulting_set = [mg.hy_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_HuEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'aáäbcdeéëfghiíjklmnoóöőpqrsztuúüűvwxyz',
			'AÁÄBCDEÉËFGHIÍJKLMNOÓÖŐPQRSZTUÚÜŰVWXYZ',
			'aÁäBcDeÉëFgHiÍjKlMnOóÖőPqRsZtUúÜűVwXyZ',
			'AáÄbCdEéËfGhIíJkLmNoÓöŐpQrSzTuÚüŰvWxYz',

			'Addig nyújtózkodj, amíg a takaród ér',
			'A fösvény anélkül is szűkölködik, amije van, anélkül is, amije nincs',
			'Ajándék lónak ne nézd a fogát|Ajándék lónak ne nézd a fogát',
			'Ne fesd az ördögöt a falra',
		]
		control_set = [
			'aaabcdeeefghiijklmnoooopqrsztuuuuvwxyz',
			'AAABCDEEEFGHIIJKLMNOOOOPQRSZTUUUUVWXYZ',
			'aAaBcDeEeFgHiIjKlMnOoOoPqRsZtUuUuVwXyZ',
			'AaAbCdEeEfGhIiJkLmNoOoOpQrSzTuUuUvWxYz',

			'Addig nyujtozkodj, amig a takarod er',
			'A fosveny anelkul is szukolkodik, amije van, anelkul is, amije nincs',
			'Ajandek lonak ne nezd a fogat|Ajandek lonak ne nezd a fogat',
			'Ne fesd az ordogot a falra',
		]
		resulting_set = [mg.hu_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_LaEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'abcdefghiklmnopqrstvxyz𐌀𐌁𐌂𐌃𐌄𐌅𐌆𐌇𐌉𐌋𐌌𐌍𐌑𐌏𐌈𐌎𐌐𐌒𐌓𐌔𐌖𐌗𐌘𐌙𐌚𐌞𐌡𐌜𐌢𐌝',
			'ABCDEFGHIKLMNOPQRSTVXYZ𐌀𐌁𐌂𐌃𐌄𐌅𐌆𐌇𐌉𐌋𐌌𐌍𐌑𐌏𐌈𐌎𐌐𐌒𐌓𐌔𐌖𐌗𐌘𐌙𐌚𐌞𐌡𐌜𐌢𐌝',
			'aBcDeFgHiKlMnOpQrStVxYz𐌀𐌁𐌂𐌃𐌄𐌅𐌆𐌇𐌉𐌋𐌌𐌍𐌑𐌏𐌈𐌎𐌐𐌒𐌓𐌔𐌖𐌗𐌘𐌙𐌚𐌞𐌡𐌜𐌢𐌝',
			'AbCdEfGhIkLmNoPqRsTvXyZ𐌀𐌁𐌂𐌃𐌄𐌅𐌆𐌇𐌉𐌋𐌌𐌍𐌑𐌏𐌈𐌎𐌐𐌒𐌓𐌔𐌖𐌗𐌘𐌙𐌚𐌞𐌡𐌜𐌢𐌝',

			'Quis custodiet ipsos custodes?',
			'Tempori parce!',
			'𐌍𐌏𐌍 𐌐𐌄𐌍𐌉𐌔 𐌂𐌀𐌍𐌉𐌍𐌀',
		]
		control_set = [
			'abcdefghiklmnopqrstvxyzabcdevzhilmnshothshpqrsuxphkhfuvchxi',
			'ABCDEFGHIKLMNOPQRSTVXYZabcdevzhilmnshothshpqrsuxphkhfuvchxi',
			'aBcDeFgHiKlMnOpQrStVxYzabcdevzhilmnshothshpqrsuxphkhfuvchxi',
			'AbCdEfGhIkLmNoPqRsTvXyZabcdevzhilmnshothshpqrsuxphkhfuvchxi',

			'Quis custodiet ipsos custodes?',
			'Tempori parce!',
			'non penis canina',
		]
		resulting_set = [mg.la_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_RuEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'абвгдеёжзийклмнопрстуфхцчшщьъэюя',
			'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯ',
			'АбВгДеЁжЗиЙкЛмНоПрСтУфХцЧшЩьЪэЮя',
			'аБвГдЕёЖзИйКлМнОпРсТуФхЦчШщЬъЭюЯ',

			'Щавель ЩАВЕЛЬ щавель',
			'шчастье Шчастье ШЧАСТЬЕ',
			'Юлия Чичерина ЮЛЯ ЧИЧЕРИНА юлия чичерина',
			'Эпос о великой мудрости сакуры, печально роняющей листья на водную гладь.',
		]
		control_set = [
			'abvgdeyozhziyklmnoprstufhcchshscheyuya',
			'ABVGDEYOZHZIYKLMNOPRSTUFHCCHSHSCHEYUYA',
			'AbVgDeYozhZiYkLmNoPrStUfHcChshScheYuya',
			'aBvGdEyoZhzIyKlMnOpRsTuFhCchShschEyuYA',

			'Schavel SCHAVEL schavel',
			'shchaste Shchaste SHCHASTE',
			'Yuliya Chicherina YULYA CHICHERINA yuliya chicherina',
			'Epos o velikoy mudrosti sakury, pechalno ronyayuschey listya na vodnuyu glad.',
		]
		resulting_set = [mg.ru_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	def test_LtEn_Transliteration(self):
		mg = Metagrapher()
		testing_set = [
			'aąbcčdeęėfghiįyjklmnoprsštuųūvzž',
			'AĄBCČDEĘĖFGHIĮYJKLMNOPRSŠTUŲŪVZŽ',
			'AąBcČdEęĖfGhIįYjKlMnOpRsŠtUųŪvZž',
			'aĄbCčDeĘėFgHiĮyJkLmNoPrSšTuŲūVzŽ',

			'Gera pradžia — pusė darbo',
			'Katė glostoma kuprą kelią',
			'Liga raita atjoja, pėščia išeina',
		]
		control_set = [
			'aabtschdeeefghiiijklmnoprsshtuuuvzzh',
			'AABTSCHDEEEFGHIIIJKLMNOPRSSHTUUUVZZH',
			'AaBtsChdEeEfGhIiIjKlMnOpRsShtUuUvZzh',
			'aAbTschDeEeFgHiIiJkLmNoPrSshTuUuVzZH',

			'Gera pradzhia — puse darbo',
			'Kate glostoma kupra kelia',
			'Liga raita atjoja, peshchia isheina',
		]
		resulting_set = [mg.lt_en(item).string for item in testing_set]
		self.assertEqual( control_set, resulting_set )

	# Metagrapher("Oriģināli šis ēdiens ir nācis no Vācijas un arī vārds quiche ir cēlies no vārda “kuchen”, kas patiesībā nozīmē neko citu kā kūka.").lv_en()

	# Metagrapher("Брзата кучка слепи кучиња раѓа. Џабе работи, џабе не седи. Низ sид со глава не бива. Što edna budala će zapletka, iljada mudreci ne možat da otpletkat.").mk_en()

	# Metagrapher("Millî Folklor: Al elmaya taş atan çok olur. Elma kendi ağacından īrak düşmez.").tr_en()


class LangAuto(unittest.TestCase):
	pass

class Symbols(unittest.TestCase):
	pass

class InstantiationAndChaining(unittest.TestCase):
	def test_instantiation_with_text(self):
		m = Metagrapher('а Тест')
		self.assertEqual(
			m.ru_en().get(),
			'a Test'
		)
	def test_instantiation_str(self):
		self.assertIn(
			str(Metagrapher('Just Test')),
			'Just Test'
		)
	def test_instantiation_str_just_upper(self):
		self.assertIn(
			str(Metagrapher('Just Test').upper()),
			'JUST TEST'
		)
	def test_instantiation_str_just_lower(self):
		self.assertIn(
			str(Metagrapher('Just Test').lower()),
			'just test'
		)
	def test_instantiation_get(self):
		self.assertIn(
			Metagrapher('Just Test').get(),
			'Just Test'
		)
	def test_instantiation_string(self):
		self.assertIn(
			Metagrapher('Just Test').string,
			'Just Test'
		)
	def test_instantiation_upper_get(self):
		self.assertEqual(
			Metagrapher('lower case string').upper().get(),
			'LOWER CASE STRING'
		)
	def test_instantiation_lower_alias(self):
		self.assertEqual(
			Metagrapher('UPPER CASE STRING').lower().text(),
			'upper case string'
		)
	def test_instantiation_upper_selfvalue(self):
		self.assertEqual(
			Metagrapher('lower case string').upper().string,
			'LOWER CASE STRING'
		)


if __name__ == "__main__":
	unittest.main()