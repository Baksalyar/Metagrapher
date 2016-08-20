![Metagrapher Logotype](https://raw.githubusercontent.com/Baksalyar/Metagrapher/master/imgs/logo.png)

_Metagrapher — a convenient Python library for obtaining readable English language identifiers (eg, URLs), generated from the strings, written in different languages, using non-standard characters and UTF-8 symbols. Also, this technique is called **transliteration** or **romanization**._

### Installation

Coming soon...

```bash
pip3 install metagrapher
```

### Supported Languages

![Metagrapher Supported Languages](https://raw.githubusercontent.com/Baksalyar/Metagrapher/master/imgs/langs_small.png)

At the moment Metagrapher supports the following language pairs (in alphabetic order):

* Arabic			→ English (*ar_en*) [draft]
* Armenian		→ English (*hy_en*)
* Azerbaijani	→ English (*az_en*)
* Burmese		→ English (*br_en*) [draft]
* Chinese		→ English (*zh_en*)
* Czech			→ English (*cz_en*)
* Deutsch		→ English (*de_en*)
* Divehi			→ English (*dv_en*)
* English		→ Russian (*en_ru*)
* Finnish		→ English (*fi_en*)
* French			→ English (*fr_en*)
* Greek			→ English (*el_en*)
* Hungarian		→ English (*hu_en*)
* Japanese		→ English (*jp_en*)
* Lithuanian	→ English (*lt_en*)
* Latin 			→ English (*la_en*)
* Latvian		→ English (*lv_en*)
* Makedonian	→ English (*mk_en*)
* Polish			→ English (*pl_en*)
* Portuguese	→ English (*pt_en*)
* Romanian		→ English (*ro_en*)
* Russian		→ English (*ru_en*)
* Serbian		→ English (*sr_en*)
* Slovak			→ English (*sk_en*)
* Thai 			→ English (*th_en*) [draft]
* Turkish		→ English (*tr_en*)
* Turkmen		→ English (*tk_en*)
* Ukrainian		→ English (*uk_en*)
* Vietnamese	→ English (*vi_en*)
* *Unicode Symbols*	→ English* ('symbols_en')

### Why Metagrapher?

![Leela Reads Alien Manuscript](https://raw.githubusercontent.com/Baksalyar/Metagrapher/master/imgs/leela.jpg)

A primary target of this library is to create readable identifiers for any items, mostly — so called [semantic URLs](https://en.wikipedia.org/wiki/Semantic_URL), which is more readable to live users and to search engines.

Library will assistly generate the readable identifier from the any string with «non-standard» (for English alphabet) characters, as well as from the string written in another language. I bet, if your primary (and only) language is English, following URL will be absolutely unreadable for you: `http://goodi.es/волшебство/الرغبات السرية/`, furthermore, this URL cannot be readen for some legacy software and hardware. Metagrapher will kindly convert above mentioned URL to user- and machine-readable: `http://goodi.es/volshebstvo/alrghbat-alsryh`.

### Examples

* Language-specific conversion (if you want to convert only from one language to English consciously):

```python
import Metagrapher

print( Metagrapher('матрёшка водка бабушка балалайка').ru_en() )
```
Will output: *matryoshka vodka babushka balalayka*

* If you want to convert only additional UTF-characters like ♥ or ☣, for instance, you can use `symbols_en()` method:

```python
Metagrapher('I ♥ NY and want a cup of ☕ right now!').symbols_en().lower().slugify('_')
```
Will generate: *i_love_ny_and_want_a_cup_of_coffee_right_now*

Oh, by the way, slugify() will remove any non-readable characters and provide you with ready-to-use string. As an argument, method `slugify()` will accept any string for delimiting words, `-` will be used by default.

And, as you can possibly think, a `lower()` method will lower-case all upper-cased characters.

One of the strong sides of Metagrapher is delicate case conversion. For instance, Metagrapher will keep right case for transliterated 'ШАПКА Юлии' by default: 'SHAPKA Yulii', other libraries will convert this string to 'ShAPKA Yulii' or even to 'SHAPKA YUlii', and 'ШАШКА ЧАПАЯ' to 'ShAShKA ChAPAYa'.

* If you intend to translate only currencies signs, like $ or €, or £, etc. to readable text, you can use `currencies_en()` method:

```python
Metagrapher('new t-shirts for only € 3,60').currencies().slugify()
```
Will generate: *New-t-shirts-for-only-EUR-360*

* Finally, you can chain methods (and languages, accordingly) elegant and logical way:

```python
Metagrapher('Здравствуйте, ♥ Labą dieną! ∞ teşekkür 100 ₺ için')
	.ru_en().pl_en().tr_en().symbols_en().currencies_en().upper().slugify()
```
Will output: *ZDRAVSTVUYTE-LOVE-LABA-DIENA-INFINITY-TESHEKKUR-100-TRY-ICHIN*

* To use *Chinese*, *Japanese* and/or *Korean* languages, please, instantiate the Metagrapher with an argument `take_from_cjk='c, j, k'`, where 'c' — Chinese, 'j' — Japanese, and 'k' — appropriately — Korean. This flag will allow you to load a relatively “heavy” dictionaries at the library startup (this procedure will add ~0.02 s. for Chinese, ~0.1 s. for Japanese, and ~0.05 s. for Korean, on the initialization stage). Also you have an option to load these languages any time later — just use `load_cjk()` method with the same keyword argument `take_from_cjk`, or as first positional argument:

```python
# 'j' loads a Japanese dicts:
Metagrapher('ワウ', take_from_cjk='j').jp_en().get()

# 'c' will load a Chinese dictionaries:
Metagrapher().load_cjk('c').zh_en('哇').get()

# 'k,c' will hook up Chinese and Korean languages:
Metagrapher("好运").load_cjk(take_from_cjk='k,c').zh_en().get()

# You can freely combine markers 'c' (Chinese), 'j' (Japanese) and 'k' (Korean)
# in the positional argument, or keyword argument take_from_cjk():
Metagrapher(take_from_cjk='j,k').jp_en('できます').load_cjk('c').zh_en('改变语言').get()

```

* Completely automatic language non-specific conversion available by methods with `any_` at the beginning of name. For example, transliteration of all characters from all languages to *English* can be done with magic method `any_en()`. Generally usable for programmatically slugifying of any headers or user names:

```python
transliteration = Metagrapher('嚜鮙گرอาพέρ', 'cjk').any_en()
print(transliteration)
```
Output: *metagrapher*

*P.S. Don't forget to use the `take_from_cjk=True` or `load_cjk()` method for Chinese, Japanese and Korean ideographs!*

* You can customize substitutions manually and override language pairs this way:

```python
Metagrapher('My ♥ is beating').symbols_en(override={'♥': 'heart'})
```
Output without overriding: *My love is beating*

With overriding: *My heart is beating*

Or you can even make own set of substitutions from the ground up:
```python
print( Metagrapher('Making bad things again')
	.custom({'bad': 'good', 'again': 'as always', ' ': ' ♥ '}) )
```
Result: *Making ♥ good ♥ things ♥ as ♥ always*


P.S. Useful resources, that you can borrow from Metagrapher:

* [Chinese Pinyin Dictionary (Diactrical signs was removed!) — 26 653 ideographs](https://raw.githubusercontent.com/Baksalyar/Metagrapher/master/zh_dict.json)
* [Chinese Frequency Dictionary — 24 204 words](https://raw.githubusercontent.com/Baksalyar/Metagrapher/master/zh_freq_words.dict)
* [Japanese Frequency Dictionary — 25 574 words](https://raw.githubusercontent.com/Baksalyar/Metagrapher/master/jp_freq_words.dict)
* [Japanese Kakasi Kanji Decomposition Dictionary — 110 508 words](https://raw.githubusercontent.com/Baksalyar/Metagrapher/master/jp_kakasi_decomposition.json)