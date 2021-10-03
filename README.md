# Cryptopals-challenges
Solving cryptopals crypo challenges https://cryptopals.com/ in python.

# What is this ?

This is a write up of my solutions (and POCs) to cryptopals crypto challenges. The challanges are composed of 8 sets, where each set is dedicated to a certain type of skills. The challanges main topics are: symmetric encryption using block ciphers and steam ciphers, hash functions, authentication (MAC - HMAC), public key cryptography, abstract algebra and more. 

# Table of contents

Each set has about 8 challenges, one can find in each table a link to the challenge, code solving the challenge and an explanation of the solution.

## Set 1: Basics

| Challenge | Solution | Explanation |
| :---: | :---: | :---: |
| <a href="https://cryptopals.com/sets/1/challenges/1">Challenge 1</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q11.py">code</a> | [Explanation 1](#challenge-1) |
| <a href="https://cryptopals.com/sets/1/challenges/2">Challenge 2</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q12.py">code</a> | [Explanation 2](#challenge-2) |
| <a href="https://cryptopals.com/sets/1/challenges/3">Challenge 3</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q13.py">code</a> | [Explanation 3](#challenge-3) |
| <a href="https://cryptopals.com/sets/1/challenges/4">Challenge 4</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q14.py">code</a> | [Explanation 4](#challenge-4) |
| <a href="https://cryptopals.com/sets/1/challenges/5">Challenge 5</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q15.py">code</a> | [Explanation 5](#challenge-5) |
| <a href="https://cryptopals.com/sets/1/challenges/6">Challenge 6</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q16.py">code</a> | [Explanation 6](#challenge-6) |
| <a href="https://cryptopals.com/sets/1/challenges/7">Challenge 7</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q17.py">code</a> | [Explanation 7](#challenge-7) |
| <a href="https://cryptopals.com/sets/1/challenges/8">Challenge 8</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q18.py">code</a> | [Explanation 8](#challenge-8) |

## Set 2: Block crypto

| Challenge | Solution | Explanation |
| :---: | :---: | :---: |
| <a href="https://cryptopals.com/sets/2/challenges/9">Challenge 9</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q21.py">code</a> | [Explanation 9](#challenge-9) |
| <a href="https://cryptopals.com/sets/2/challenges/10">Challenge 10</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q22.py">code</a> | [Explanation 10](#challenge-10) |
| <a href="https://cryptopals.com/sets/2/challenges/11">Challenge 11</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q23.py">code</a> | [Explanation 11](#challenge-11) |
| <a href="https://cryptopals.com/sets/2/challenges/12">Challenge 12</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q24.py">code</a> | [Explanation 12](#challenge-12) |
| <a href="https://cryptopals.com/sets/2/challenges/13">Challenge 13</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q25.py">code</a> | [Explanation 13](#challenge-13) |
| <a href="https://cryptopals.com/sets/2/challenges/14">Challenge 14</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q26.py">code</a> | [Explanation 14](#challenge-14) |
| <a href="https://cryptopals.com/sets/2/challenges/15">Challenge 15</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q27.py">code</a> | [Explanation 15](#challenge-15) |
| <a href="https://cryptopals.com/sets/2/challenges/16">Challenge 16</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q28.py">code</a> | [Explanation 16](#challenge-16) |

## Set 3: Block & stream crypto

| Challenge | Solution | Explanation |
| :---: | :---: | :---: |
| <a href="https://cryptopals.com/sets/3/challenges/17">Challenge 17</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q31.py">code</a> | [Explanation 17](#challenge-17) |
| <a href="https://cryptopals.com/sets/3/challenges/18">Challenge 18</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q32.py">code</a> | [Explanation 18](#challenge-18) |
| <a href="https://cryptopals.com/sets/3/challenges/19">Challenge 19</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q33.py">code</a> | [Explanation 19](#challenge-19) |
| <a href="https://cryptopals.com/sets/3/challenges/20">Challenge 20</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q34.py">code</a> | [Explanation 20](#challenge-20) |
| <a href="https://cryptopals.com/sets/3/challenges/21">Challenge 21</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q35.py">code</a> | [Explanation 21](#challenge-21) |
| <a href="https://cryptopals.com/sets/3/challenges/22">Challenge 22</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q36.py">code</a> | [Explanation 22](#challenge-22) |
| <a href="https://cryptopals.com/sets/3/challenges/23">Challenge 23</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q37.py">code</a> | [Explanation 23](#challenge-23) |
| <a href="https://cryptopals.com/sets/3/challenges/24">Challenge 24</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q38.py">code</a> | [Explanation 24](#challenge-24) |

## Set 4: Stream crypto and randomness

| Challenge | Solution | Explanation |
| :---: | :---: | :---: |
| <a href="https://cryptopals.com/sets/4/challenges/25">Challenge 25</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q41.py">code</a> | [Explanation 25](#challenge-25) |
| <a href="https://cryptopals.com/sets/4/challenges/26">Challenge 26</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q42.py">code</a> | [Explanation 26](#challenge-26) |
| <a href="https://cryptopals.com/sets/4/challenges/27">Challenge 27</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q43.py">code</a> | [Explanation 27](#challenge-27) |
| <a href="https://cryptopals.com/sets/4/challenges/28">Challenge 28</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q44.py">code</a> | [Explanation 28](#challenge-28) |
| <a href="https://cryptopals.com/sets/4/challenges/29">Challenge 29</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q45.py">code</a> | [Explanation 29](#challenge-29) |
| <a href="https://cryptopals.com/sets/4/challenges/30">Challenge 30</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q46.py">MD4 version</a> , <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q46MD5.py">MD5 version</a>| [Explanation 30](#challenge-30) |
| <a href="https://cryptopals.com/sets/4/challenges/31">Challenge 31</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q47Utils.py">Utils</a> , <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q47Server.py">Server</a> , <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q47attacker.py">Attacker</a>| [Explanation 31](#challenge-31) |
| <a href="https://cryptopals.com/sets/4/challenges/32">Challenge 32</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q48Server.py">Server</a> , <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q48attacker.py">Attacker</a> | [Explanation 32](#challenge-32), <a href="https://www.youtube.com/watch?v=ra_6jVZ5y1A">video</a> demonstration of the HMAC recovery attack|

## Set 5: Diffie-Hellman and friends

| Challenge | Solution | Explanation |
| :---: | :---: | :---: |
| <a href="https://cryptopals.com/sets/5/challenges/33">Challenge 33</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q51.py">code</a> | [Explanation 33](#challenge-33) |

# Write up

Explanations to all solutions.

## Set 1: Basics

### [Challenge 1](#challenge-1)

Converting <a href="https://en.wikipedia.org/wiki/Hexadecimal">Hex</a> to <a href="https://en.wikipedia.org/wiki/Base64">base64</a>, by first transforming the hex string to a bytes object, afterward transforming it into base64. 


Expected output: 
```python
solved
```

### [Challenge 2](#challenge-2)

Implementation of fixed <a href="https://en.wikipedia.org/wiki/Exclusive_or">xor</a> between two buffers.

Expected output: 
```python
Success
```

### [Challenge 3](#challenge-3)

The solution uses a brute force approach, trying every possible single byte key, choosing the one which results in the highest english score.
Inorder to calculate the english score we use the <a href="https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html">distribution</a>  of letters in the english language.

Expected output: 
```python
Current char: 9 Score: 0.013453899999999998 current deciphered result: b'\x12>>:8?6q\x1c\x12v"q=8:4q0q!>$?5q>7q302>?' 

Current char: 10 Score: 0.3210512 current deciphered result: b'\x11==9;<5r\x1f\x11u!r>;97r3r"=\'<6r=4r031=<' 

Current char: 11 Score: 0.5742098999999999 current deciphered result: b'\x10<<8:=4s\x1e\x10t s?:86s2s#<&=7s<5s120<=' 

Current char: 12 Score: 0.48919019999999996 current deciphered result: b"\x17;;?=:3t\x19\x17s't8=?1t5t$;!:0t;2t657;:" 

Current char: 13 Score: 0.3766549 current deciphered result: b'\x16::><;2u\x18\x16r&u9<>0u4u%: ;1u:3u746:;' 

Current char: 14 Score: 0.050602400000000006 current deciphered result: b'\x1599=?81v\x1b\x15q%v:?=3v7v&9#82v90v47598' 

Current char: 15 Score: 0.11652769999999998 current deciphered result: b'\x1488<>90w\x1a\x14p$w;><2w6w\'8"93w81w56489' 

Current char: 16 Score: 0.35536300000000004 current deciphered result: b"\x0b''#!&/h\x05\x0bo;h$!#-h)h8'=&,h'.h*)+'&" 

Current char: 17 Score: 0.7749441 current deciphered result: b'\n&&" \'.i\x04\nn:i% ",i(i9&<\'-i&/i+(*&\'' 

Current char: 18 Score: 0.025632199999999994 current deciphered result: b'\t%%!#$-j\x07\tm9j&#!/j+j:%?$.j%,j(+)%$' 

Current char: 19 Score: 0.44710280000000013 current deciphered result: b'\x08$$ "%,k\x06\x08l8k\'" .k*k;$>%/k$-k)*($%' 

Current char: 20 Score: 0.3957650999999999 current deciphered result: b'\x0f##\'%"+l\x01\x0fk?l %\')l-l<#9"(l#*l.-/#"' 

Current char: 21 Score: 0.12217769999999997 current deciphered result: b'\x0e""&$#*m\x00\x0ej>m!$&(m,m="8#)m"+m/,."#' 

Current char: 22 Score: 0.9699717999999999 current deciphered result: b'\r!!%\' )n\x03\ri=n"\'%+n/n>!; *n!(n,/-! ' 

Current char: 23 Score: 1.3661609999999997 current deciphered result: b'\x0c  $&!(o\x02\x0ch<o#&$*o.o? :!+o )o-., !' 

Current char: 24 Score: 0.015861 current deciphered result: b'\x03//+).\'`\r\x03g3`,)+%`!`0/5.$`/&`"!#/.' 

Current char: 25 Score: 0.7944673 current deciphered result: b'\x02..*(/&a\x0c\x02f2a-(*$a a1.4/%a.\'a# "./' 

Current char: 26 Score: 0.37051120000000004 current deciphered result: b"\x01--)+,%b\x0f\x01e1b.+)'b#b2-7,&b-$b #!-," 

Current char: 27 Score: 0.3572051 current deciphered result: b'\x00,,(*-$c\x0e\x00d0c/*(&c"c3,6-\'c,%c!" ,-' 

Current char: 28 Score: 0.4234531 current deciphered result: b'\x07++/-*#d\t\x07c7d(-/!d%d4+1* d+"d&%\'+*' 

Current char: 29 Score: 0.8291082000000001 current deciphered result: b'\x06**.,+"e\x08\x06b6e),. e$e5*0+!e*#e\'$&*+' 

Current char: 30 Score: 0.37572059999999996 current deciphered result: b'\x05))-/(!f\x0b\x05a5f*/-#f\'f6)3("f) f$\'%)(' 

Current char: 31 Score: 0.2869842000000001 current deciphered result: b'\x04((,.) g\n\x04`4g+.,"g&g7(2)#g(!g%&$()' 

Current char: 32 Score: 0.0082152 current deciphered result: b';\x17\x17\x13\x11\x16\x1fX5;_\x0bX\x14\x11\x13\x1dX\x19X\x08\x17\r\x16\x1cX\x17\x1eX\x1a\x19\x1b\x17\x16' 

Current char: 33 Score: 0.0875904 current deciphered result: b':\x16\x16\x12\x10\x17\x1eY4:^\nY\x15\x10\x12\x1cY\x18Y\t\x16\x0c\x17\x1dY\x16\x1fY\x1b\x18\x1a\x16\x17' 

Current char: 34 Score: 0.004701599999999999 current deciphered result: b'9\x15\x15\x11\x13\x14\x1dZ79]\tZ\x16\x13\x11\x1fZ\x1bZ\n\x15\x0f\x14\x1eZ\x15\x1cZ\x18\x1b\x19\x15\x14' 

Current char: 35 Score: 0 current deciphered result: b'8\x14\x14\x10\x12\x15\x1c[68\\\x08[\x17\x12\x10\x1e[\x1a[\x0b\x14\x0e\x15\x1f[\x14\x1d[\x19\x1a\x18\x14\x15' 

Current char: 36 Score: 0 current deciphered result: b'?\x13\x13\x17\x15\x12\x1b\\1?[\x0f\\\x10\x15\x17\x19\\\x1d\\\x0c\x13\t\x12\x18\\\x13\x1a\\\x1e\x1d\x1f\x13\x12' 

Current char: 37 Score: 0.0007836 current deciphered result: b'>\x12\x12\x16\x14\x13\x1a]0>Z\x0e]\x11\x14\x16\x18]\x1c]\r\x12\x08\x13\x19]\x12\x1b]\x1f\x1c\x1e\x12\x13' 

Current char: 38 Score: 0.0145984 current deciphered result: b'=\x11\x11\x15\x17\x10\x19^3=Y\r^\x12\x17\x15\x1b^\x1f^\x0e\x11\x0b\x10\x1a^\x11\x18^\x1c\x1f\x1d\x11\x10' 

Current char: 39 Score: 0.0013692 current deciphered result: b'<\x10\x10\x14\x16\x11\x18_2<X\x0c_\x13\x16\x14\x1a_\x1e_\x0f\x10\n\x11\x1b_\x10\x19_\x1d\x1e\x1c\x10\x11' 

Current char: 40 Score: 0.0997142 current deciphered result: b'3\x1f\x1f\x1b\x19\x1e\x17P=3W\x03P\x1c\x19\x1b\x15P\x11P\x00\x1f\x05\x1e\x14P\x1f\x16P\x12\x11\x13\x1f\x1e' 

Current char: 41 Score: 0.013453899999999998 current deciphered result: b'2\x1e\x1e\x1a\x18\x1f\x16Q<2V\x02Q\x1d\x18\x1a\x14Q\x10Q\x01\x1e\x04\x1f\x15Q\x1e\x17Q\x13\x10\x12\x1e\x1f' 

Current char: 42 Score: 0.3210512 current deciphered result: b'1\x1d\x1d\x19\x1b\x1c\x15R?1U\x01R\x1e\x1b\x19\x17R\x13R\x02\x1d\x07\x1c\x16R\x1d\x14R\x10\x13\x11\x1d\x1c' 

Current char: 43 Score: 0.38239170000000006 current deciphered result: b'0\x1c\x1c\x18\x1a\x1d\x14S>0T\x00S\x1f\x1a\x18\x16S\x12S\x03\x1c\x06\x1d\x17S\x1c\x15S\x11\x12\x10\x1c\x1d' 

Current char: 44 Score: 0.48919019999999996 current deciphered result: b'7\x1b\x1b\x1f\x1d\x1a\x13T97S\x07T\x18\x1d\x1f\x11T\x15T\x04\x1b\x01\x1a\x10T\x1b\x12T\x16\x15\x17\x1b\x1a' 

Current char: 45 Score: 0.1848367 current deciphered result: b'6\x1a\x1a\x1e\x1c\x1b\x12U86R\x06U\x19\x1c\x1e\x10U\x14U\x05\x1a\x00\x1b\x11U\x1a\x13U\x17\x14\x16\x1a\x1b' 

Current char: 46 Score: 0.050602400000000006 current deciphered result: b'5\x19\x19\x1d\x1f\x18\x11V;5Q\x05V\x1a\x1f\x1d\x13V\x17V\x06\x19\x03\x18\x12V\x19\x10V\x14\x17\x15\x19\x18' 

Current char: 47 Score: 0.11652769999999998 current deciphered result: b'4\x18\x18\x1c\x1e\x19\x10W:4P\x04W\x1b\x1e\x1c\x12W\x16W\x07\x18\x02\x19\x13W\x18\x11W\x15\x16\x14\x18\x19' 

Current char: 48 Score: 0.35536300000000004 current deciphered result: b'+\x07\x07\x03\x01\x06\x0fH%+O\x1bH\x04\x01\x03\rH\tH\x18\x07\x1d\x06\x0cH\x07\x0eH\n\t\x0b\x07\x06' 

Current char: 49 Score: 0.39130770000000004 current deciphered result: b'*\x06\x06\x02\x00\x07\x0eI$*N\x1aI\x05\x00\x02\x0cI\x08I\x19\x06\x1c\x07\rI\x06\x0fI\x0b\x08\n\x06\x07' 

Current char: 50 Score: 0.025632199999999994 current deciphered result: b")\x05\x05\x01\x03\x04\rJ')M\x19J\x06\x03\x01\x0fJ\x0bJ\x1a\x05\x1f\x04\x0eJ\x05\x0cJ\x08\x0b\t\x05\x04" 

Current char: 51 Score: 0.06346639999999999 current deciphered result: b'(\x04\x04\x00\x02\x05\x0cK&(L\x18K\x07\x02\x00\x0eK\nK\x1b\x04\x1e\x05\x0fK\x04\rK\t\n\x08\x04\x05' 

Current char: 52 Score: 0.2039469 current deciphered result: b'/\x03\x03\x07\x05\x02\x0bL!/K\x1fL\x00\x05\x07\tL\rL\x1c\x03\x19\x02\x08L\x03\nL\x0e\r\x0f\x03\x02' 

Current char: 53 Score: 0.31399590000000005 current deciphered result: b'.\x02\x02\x06\x04\x03\nM .J\x1eM\x01\x04\x06\x08M\x0cM\x1d\x02\x18\x03\tM\x02\x0bM\x0f\x0c\x0e\x02\x03' 

Current char: 54 Score: 0.39451719999999996 current deciphered result: b'-\x01\x01\x05\x07\x00\tN#-I\x1dN\x02\x07\x05\x0bN\x0fN\x1e\x01\x1b\x00\nN\x01\x08N\x0c\x0f\r\x01\x00' 

Current char: 55 Score: 0.40707000000000004 current deciphered result: b',\x00\x00\x04\x06\x01\x08O",H\x1cO\x03\x06\x04\nO\x0eO\x1f\x00\x1a\x01\x0bO\x00\tO\r\x0e\x0c\x00\x01' 

Current char: 56 Score: 0.015861 current deciphered result: b'#\x0f\x0f\x0b\t\x0e\x07@-#G\x13@\x0c\t\x0b\x05@\x01@\x10\x0f\x15\x0e\x04@\x0f\x06@\x02\x01\x03\x0f\x0e' 

Current char: 57 Score: 0.4108309 current deciphered result: b'"\x0e\x0e\n\x08\x0f\x06A,"F\x12A\r\x08\n\x04A\x00A\x11\x0e\x14\x0f\x05A\x0e\x07A\x03\x00\x02\x0e\x0f' 

Current char: 58 Score: 0.17869300000000005 current deciphered result: b'!\r\r\t\x0b\x0c\x05B/!E\x11B\x0e\x0b\t\x07B\x03B\x12\r\x17\x0c\x06B\r\x04B\x00\x03\x01\r\x0c' 

Current char: 59 Score: 0.5490232999999999 current deciphered result: b' \x0c\x0c\x08\n\r\x04C. D\x10C\x0f\n\x08\x06C\x02C\x13\x0c\x16\r\x07C\x0c\x05C\x01\x02\x00\x0c\r' 

Current char: 60 Score: 0.2316349 current deciphered result: b"'\x0b\x0b\x0f\r\n\x03D)'C\x17D\x08\r\x0f\x01D\x05D\x14\x0b\x11\n\x00D\x0b\x02D\x06\x05\x07\x0b\n" 

Current char: 61 Score: 0.63729 current deciphered result: b'&\n\n\x0e\x0c\x0b\x02E(&B\x16E\t\x0c\x0e\x00E\x04E\x15\n\x10\x0b\x01E\n\x03E\x07\x04\x06\n\x0b' 

Current char: 62 Score: 0.18390240000000002 current deciphered result: b'%\t\t\r\x0f\x08\x01F+%A\x15F\n\x0f\r\x03F\x07F\x16\t\x13\x08\x02F\t\x00F\x04\x07\x05\t\x08' 

Current char: 63 Score: 0.095166 current deciphered result: b'$\x08\x08\x0c\x0e\t\x00G*$@\x14G\x0b\x0e\x0c\x02G\x06G\x17\x08\x12\t\x03G\x08\x01G\x05\x06\x04\x08\t' 

Current char: 64 Score: 0.4153637000000001 current deciphered result: b'[wwsqv\x7f8U[?k8tqs}8y8hwmv|8w~8zy{wv' 

Current char: 65 Score: 0.4102747 current deciphered result: b'Zvvrpw~9TZ>j9upr|9x9ivlw}9v\x7f9{xzvw' 

Current char: 66 Score: 0.6231721000000001 current deciphered result: b'Yuuqst}:WY=i:vsq\x7f:{:juot~:u|:x{yut' 

Current char: 67 Score: 0.7157440000000002 current deciphered result: b'Xttpru|;VX<h;wrp~;z;ktnu\x7f;t};yzxtu' 

Current char: 68 Score: 0.6663949999999998 current deciphered result: b'_sswur{<Q_;o<puwy<}<lsirx<sz<~}\x7fsr' 

Current char: 69 Score: 0.7232902999999999 current deciphered result: b'^rrvtsz=P^:n=qtvx=|=mrhsy=r{=\x7f|~rs' 

Current char: 70 Score: 0.3246778 current deciphered result: b']qquwpy>S]9m>rwu{>\x7f>nqkpz>qx>|\x7f}qp' 

Current char: 71 Score: 0.4456223 current deciphered result: b'\\pptvqx?R\\8l?svtz?~?opjq{?py?}~|pq' 

Current char: 72 Score: 0.48214699999999994 current deciphered result: b'S\x7f\x7f{y~w0]S7c0|y{u0q0`\x7fe~t0\x7fv0rqs\x7f~' 

Current char: 73 Score: 0.4661282000000001 current deciphered result: b'R~~zx\x7fv1\\R6b1}xzt1p1a~d\x7fu1~w1spr~\x7f' 

Current char: 74 Score: 0.36302130000000005 current deciphered result: b'Q}}y{|u2_Q5a2~{yw2s2b}g|v2}t2psq}|' 

Current char: 75 Score: 0.3083609 current deciphered result: b'P||xz}t3^P4`3\x7fzxv3r3c|f}w3|u3qrp|}' 

Current char: 76 Score: 0.3549928 current deciphered result: b'W{{\x7f}zs4YW3g4x}\x7fq4u4d{azp4{r4vuw{z' 

Current char: 77 Score: 0.44764480000000006 current deciphered result: b'Vzz~|{r5XV2f5y|~p5t5ez`{q5zs5wtvz{' 

Current char: 78 Score: 0.5142371000000001 current deciphered result: b'Uyy}\x7fxq6[U1e6z\x7f}s6w6fycxr6yp6twuyx' 

Current char: 79 Score: 0.4885526000000001 current deciphered result: b'Txx|~yp7ZT0d7{~|r7v7gxbys7xq7uvtxy' 

Current char: 80 Score: 0.7501053000000001 current deciphered result: b'Kggcafo(EK/{(dacm(i(xg}fl(gn(jikgf' 

Current char: 81 Score: 0.6016661000000001 current deciphered result: b'Jffb`gn)DJ.z)e`bl)h)yf|gm)fo)khjfg' 

Current char: 82 Score: 1.2467837 current deciphered result: b'Ieeacdm*GI-y*fcao*k*ze\x7fdn*el*hkied' 

Current char: 83 Score: 0.9241433 current deciphered result: b'Hdd`bel+FH,x+gb`n+j+{d~eo+dm+ijhde' 

Current char: 84 Score: 0.8525476000000001 current deciphered result: b'Occgebk,AO+\x7f,`egi,m,|cybh,cj,nmocb' 

Current char: 85 Score: 0.7097484 current deciphered result: b'Nbbfdcj-@N*~-adfh-l-}bxci-bk-olnbc' 

Current char: 86 Score: 0.9241391000000001 current deciphered result: b'Maaeg`i.CM)}.bgek.o.~a{`j.ah.loma`' 

Current char: 87 Score: 0.6836232999999998 current deciphered result: b'L``dfah/BL(|/cfdj/n/\x7f`zak/`i/mnl`a' 

Current char: 88 Score: 2.2641049 current deciphered result: b"Cooking MC's like a pound of bacon" 

Current char: 89 Score: 0.9722303999999999 current deciphered result: b'Bnnjhof!LB&r!mhjd!`!qntoe!ng!c`bno' 

Current char: 90 Score: 0.9198252 current deciphered result: b'Ammikle"OA%q"nkig"c"rmwlf"md"`caml' 

Current char: 91 Score: 0.7812789 current deciphered result: b'@llhjmd#N@$p#ojhf#b#slvmg#le#ab`lm' 

Current char: 92 Score: 0.7586733000000003 current deciphered result: b'Gkkomjc$IG#w$hmoa$e$tkqj`$kb$fegkj' 

Current char: 93 Score: 0.5930670000000001 current deciphered result: b'Fjjnlkb%HF"v%iln`%d%ujpka%jc%gdfjk' 

Current char: 94 Score: 1.1534051 current deciphered result: b'Eiimoha&KE!u&jomc&g&vishb&i`&dgeih' 

Current char: 95 Score: 1.2786698 current deciphered result: b"Dhhlni`'JD t'knlb'f'whric'ha'efdhi" 

Current char: 96 Score: 0.4153637000000001 current deciphered result: b'{WWSQV_\x18u{\x1fK\x18TQS]\x18Y\x18HWMV\\\x18W^\x18ZY[WV' 

Current char: 97 Score: 0.4102747 current deciphered result: b'zVVRPW^\x19tz\x1eJ\x19UPR\\\x19X\x19IVLW]\x19V_\x19[XZVW' 

Current char: 98 Score: 0.6231721000000001 current deciphered result: b'yUUQST]\x1awy\x1dI\x1aVSQ_\x1a[\x1aJUOT^\x1aU\\\x1aX[YUT' 

Current char: 99 Score: 0.7157440000000002 current deciphered result: b'xTTPRU\\\x1bvx\x1cH\x1bWRP^\x1bZ\x1bKTNU_\x1bT]\x1bYZXTU' 

Current char: 100 Score: 0.6663949999999998 current deciphered result: b'\x7fSSWUR[\x1cq\x7f\x1bO\x1cPUWY\x1c]\x1cLSIRX\x1cSZ\x1c^]_SR' 

Current char: 101 Score: 0.7232902999999999 current deciphered result: b'~RRVTSZ\x1dp~\x1aN\x1dQTVX\x1d\\\x1dMRHSY\x1dR[\x1d_\\^RS' 

Current char: 102 Score: 0.3246778 current deciphered result: b'}QQUWPY\x1es}\x19M\x1eRWU[\x1e_\x1eNQKPZ\x1eQX\x1e\\_]QP' 

Current char: 103 Score: 0.4456223 current deciphered result: b'|PPTVQX\x1fr|\x18L\x1fSVTZ\x1f^\x1fOPJQ[\x1fPY\x1f]^\\PQ' 

Current char: 104 Score: 0.48214699999999994 current deciphered result: b's__[Y^W\x10}s\x17C\x10\\Y[U\x10Q\x10@_E^T\x10_V\x10RQS_^' 

Current char: 105 Score: 0.4661282000000001 current deciphered result: b'r^^ZX_V\x11|r\x16B\x11]XZT\x11P\x11A^D_U\x11^W\x11SPR^_' 

Current char: 106 Score: 0.36302130000000005 current deciphered result: b'q]]Y[\\U\x12\x7fq\x15A\x12^[YW\x12S\x12B]G\\V\x12]T\x12PSQ]\\' 

Current char: 107 Score: 0.3083609 current deciphered result: b'p\\\\XZ]T\x13~p\x14@\x13_ZXV\x13R\x13C\\F]W\x13\\U\x13QRP\\]' 

Current char: 108 Score: 0.3549928 current deciphered result: b'w[[_]ZS\x14yw\x13G\x14X]_Q\x14U\x14D[AZP\x14[R\x14VUW[Z' 

Current char: 109 Score: 0.44764480000000006 current deciphered result: b'vZZ^\\[R\x15xv\x12F\x15Y\\^P\x15T\x15EZ@[Q\x15ZS\x15WTVZ[' 

Current char: 110 Score: 0.5142371000000001 current deciphered result: b'uYY]_XQ\x16{u\x11E\x16Z_]S\x16W\x16FYCXR\x16YP\x16TWUYX' 

Current char: 111 Score: 0.4885526000000001 current deciphered result: b'tXX\\^YP\x17zt\x10D\x17[^\\R\x17V\x17GXBYS\x17XQ\x17UVTXY' 

Current char: 112 Score: 0.7501053000000001 current deciphered result: b'kGGCAFO\x08ek\x0f[\x08DACM\x08I\x08XG]FL\x08GN\x08JIKGF' 

Current char: 113 Score: 0.6016661000000001 current deciphered result: b'jFFB@GN\tdj\x0eZ\tE@BL\tH\tYF\\GM\tFO\tKHJFG' 

Current char: 114 Score: 1.2467837 current deciphered result: b'iEEACDM\ngi\rY\nFCAO\nK\nZE_DN\nEL\nHKIED' 

Current char: 115 Score: 0.9241433 current deciphered result: b'hDD@BEL\x0bfh\x0cX\x0bGB@N\x0bJ\x0b[D^EO\x0bDM\x0bIJHDE' 

Current char: 116 Score: 0.8525476000000001 current deciphered result: b'oCCGEBK\x0cao\x0b_\x0c@EGI\x0cM\x0c\\CYBH\x0cCJ\x0cNMOCB' 

Current char: 117 Score: 0.7097484 current deciphered result: b'nBBFDCJ\r`n\n^\rADFH\rL\r]BXCI\rBK\rOLNBC' 

Current char: 118 Score: 0.9241391000000001 current deciphered result: b'mAAEG@I\x0ecm\t]\x0eBGEK\x0eO\x0e^A[@J\x0eAH\x0eLOMA@' 

Current char: 119 Score: 0.6836232999999998 current deciphered result: b'l@@DFAH\x0fbl\x08\\\x0fCFDJ\x0fN\x0f_@ZAK\x0f@I\x0fMNL@A' 

Current char: 120 Score: 1.1131957 current deciphered result: b'cOOKING\x00mc\x07S\x00LIKE\x00A\x00POUND\x00OF\x00BACON' 

Current char: 121 Score: 0.9722303999999999 current deciphered result: b'bNNJHOF\x01lb\x06R\x01MHJD\x01@\x01QNTOE\x01NG\x01C@BNO' 

Current char: 122 Score: 0.9198252 current deciphered result: b'aMMIKLE\x02oa\x05Q\x02NKIG\x02C\x02RMWLF\x02MD\x02@CAML' 

Current char: 123 Score: 0.7812789 current deciphered result: b'`LLHJMD\x03n`\x04P\x03OJHF\x03B\x03SLVMG\x03LE\x03AB@LM' 

Current char: 124 Score: 0.7586733000000003 current deciphered result: b'gKKOMJC\x04ig\x03W\x04HMOA\x04E\x04TKQJ@\x04KB\x04FEGKJ' 

Current char: 125 Score: 0.5930670000000001 current deciphered result: b'fJJNLKB\x05hf\x02V\x05ILN@\x05D\x05UJPKA\x05JC\x05GDFJK' 

Current char: 126 Score: 1.1534051 current deciphered result: b'eIIMOHA\x06ke\x01U\x06JOMC\x06G\x06VISHB\x06I@\x06DGEIH' 

Current char: 127 Score: 1.0868516 current deciphered result: b'dHHLNI@\x07jd\x00T\x07KNLB\x07F\x07WHRIC\x07HA\x07EFDHI' 

Current char: 128 Score: 0 current deciphered result: b'\x9b\xb7\xb7\xb3\xb1\xb6\xbf\xf8\x95\x9b\xff\xab\xf8\xb4\xb1\xb3\xbd\xf8\xb9\xf8\xa8\xb7\xad\xb6\xbc\xf8\xb7\xbe\xf8\xba\xb9\xbb\xb7\xb6' 

Current char: 129 Score: 0 current deciphered result: b'\x9a\xb6\xb6\xb2\xb0\xb7\xbe\xf9\x94\x9a\xfe\xaa\xf9\xb5\xb0\xb2\xbc\xf9\xb8\xf9\xa9\xb6\xac\xb7\xbd\xf9\xb6\xbf\xf9\xbb\xb8\xba\xb6\xb7' 

Current char: 130 Score: 0 current deciphered result: b'\x99\xb5\xb5\xb1\xb3\xb4\xbd\xfa\x97\x99\xfd\xa9\xfa\xb6\xb3\xb1\xbf\xfa\xbb\xfa\xaa\xb5\xaf\xb4\xbe\xfa\xb5\xbc\xfa\xb8\xbb\xb9\xb5\xb4' 

Current char: 131 Score: 0 current deciphered result: b'\x98\xb4\xb4\xb0\xb2\xb5\xbc\xfb\x96\x98\xfc\xa8\xfb\xb7\xb2\xb0\xbe\xfb\xba\xfb\xab\xb4\xae\xb5\xbf\xfb\xb4\xbd\xfb\xb9\xba\xb8\xb4\xb5' 

Current char: 132 Score: 0 current deciphered result: b'\x9f\xb3\xb3\xb7\xb5\xb2\xbb\xfc\x91\x9f\xfb\xaf\xfc\xb0\xb5\xb7\xb9\xfc\xbd\xfc\xac\xb3\xa9\xb2\xb8\xfc\xb3\xba\xfc\xbe\xbd\xbf\xb3\xb2' 

Current char: 133 Score: 0 current deciphered result: b'\x9e\xb2\xb2\xb6\xb4\xb3\xba\xfd\x90\x9e\xfa\xae\xfd\xb1\xb4\xb6\xb8\xfd\xbc\xfd\xad\xb2\xa8\xb3\xb9\xfd\xb2\xbb\xfd\xbf\xbc\xbe\xb2\xb3' 

Current char: 134 Score: 0 current deciphered result: b'\x9d\xb1\xb1\xb5\xb7\xb0\xb9\xfe\x93\x9d\xf9\xad\xfe\xb2\xb7\xb5\xbb\xfe\xbf\xfe\xae\xb1\xab\xb0\xba\xfe\xb1\xb8\xfe\xbc\xbf\xbd\xb1\xb0' 

Current char: 135 Score: 0 current deciphered result: b'\x9c\xb0\xb0\xb4\xb6\xb1\xb8\xff\x92\x9c\xf8\xac\xff\xb3\xb6\xb4\xba\xff\xbe\xff\xaf\xb0\xaa\xb1\xbb\xff\xb0\xb9\xff\xbd\xbe\xbc\xb0\xb1' 

Current char: 136 Score: 0 current deciphered result: b'\x93\xbf\xbf\xbb\xb9\xbe\xb7\xf0\x9d\x93\xf7\xa3\xf0\xbc\xb9\xbb\xb5\xf0\xb1\xf0\xa0\xbf\xa5\xbe\xb4\xf0\xbf\xb6\xf0\xb2\xb1\xb3\xbf\xbe' 

Current char: 137 Score: 0 current deciphered result: b'\x92\xbe\xbe\xba\xb8\xbf\xb6\xf1\x9c\x92\xf6\xa2\xf1\xbd\xb8\xba\xb4\xf1\xb0\xf1\xa1\xbe\xa4\xbf\xb5\xf1\xbe\xb7\xf1\xb3\xb0\xb2\xbe\xbf' 

Current char: 138 Score: 0 current deciphered result: b'\x91\xbd\xbd\xb9\xbb\xbc\xb5\xf2\x9f\x91\xf5\xa1\xf2\xbe\xbb\xb9\xb7\xf2\xb3\xf2\xa2\xbd\xa7\xbc\xb6\xf2\xbd\xb4\xf2\xb0\xb3\xb1\xbd\xbc' 

Current char: 139 Score: 0 current deciphered result: b'\x90\xbc\xbc\xb8\xba\xbd\xb4\xf3\x9e\x90\xf4\xa0\xf3\xbf\xba\xb8\xb6\xf3\xb2\xf3\xa3\xbc\xa6\xbd\xb7\xf3\xbc\xb5\xf3\xb1\xb2\xb0\xbc\xbd' 

Current char: 140 Score: 0 current deciphered result: b'\x97\xbb\xbb\xbf\xbd\xba\xb3\xf4\x99\x97\xf3\xa7\xf4\xb8\xbd\xbf\xb1\xf4\xb5\xf4\xa4\xbb\xa1\xba\xb0\xf4\xbb\xb2\xf4\xb6\xb5\xb7\xbb\xba' 

Current char: 141 Score: 0 current deciphered result: b'\x96\xba\xba\xbe\xbc\xbb\xb2\xf5\x98\x96\xf2\xa6\xf5\xb9\xbc\xbe\xb0\xf5\xb4\xf5\xa5\xba\xa0\xbb\xb1\xf5\xba\xb3\xf5\xb7\xb4\xb6\xba\xbb' 

Current char: 142 Score: 0 current deciphered result: b'\x95\xb9\xb9\xbd\xbf\xb8\xb1\xf6\x9b\x95\xf1\xa5\xf6\xba\xbf\xbd\xb3\xf6\xb7\xf6\xa6\xb9\xa3\xb8\xb2\xf6\xb9\xb0\xf6\xb4\xb7\xb5\xb9\xb8' 

Current char: 143 Score: 0 current deciphered result: b'\x94\xb8\xb8\xbc\xbe\xb9\xb0\xf7\x9a\x94\xf0\xa4\xf7\xbb\xbe\xbc\xb2\xf7\xb6\xf7\xa7\xb8\xa2\xb9\xb3\xf7\xb8\xb1\xf7\xb5\xb6\xb4\xb8\xb9' 

Current char: 144 Score: 0 current deciphered result: b'\x8b\xa7\xa7\xa3\xa1\xa6\xaf\xe8\x85\x8b\xef\xbb\xe8\xa4\xa1\xa3\xad\xe8\xa9\xe8\xb8\xa7\xbd\xa6\xac\xe8\xa7\xae\xe8\xaa\xa9\xab\xa7\xa6' 

Current char: 145 Score: 0 current deciphered result: b'\x8a\xa6\xa6\xa2\xa0\xa7\xae\xe9\x84\x8a\xee\xba\xe9\xa5\xa0\xa2\xac\xe9\xa8\xe9\xb9\xa6\xbc\xa7\xad\xe9\xa6\xaf\xe9\xab\xa8\xaa\xa6\xa7' 

Current char: 146 Score: 0 current deciphered result: b'\x89\xa5\xa5\xa1\xa3\xa4\xad\xea\x87\x89\xed\xb9\xea\xa6\xa3\xa1\xaf\xea\xab\xea\xba\xa5\xbf\xa4\xae\xea\xa5\xac\xea\xa8\xab\xa9\xa5\xa4' 

Current char: 147 Score: 0 current deciphered result: b'\x88\xa4\xa4\xa0\xa2\xa5\xac\xeb\x86\x88\xec\xb8\xeb\xa7\xa2\xa0\xae\xeb\xaa\xeb\xbb\xa4\xbe\xa5\xaf\xeb\xa4\xad\xeb\xa9\xaa\xa8\xa4\xa5' 

Current char: 148 Score: 0 current deciphered result: b'\x8f\xa3\xa3\xa7\xa5\xa2\xab\xec\x81\x8f\xeb\xbf\xec\xa0\xa5\xa7\xa9\xec\xad\xec\xbc\xa3\xb9\xa2\xa8\xec\xa3\xaa\xec\xae\xad\xaf\xa3\xa2' 

Current char: 149 Score: 0 current deciphered result: b'\x8e\xa2\xa2\xa6\xa4\xa3\xaa\xed\x80\x8e\xea\xbe\xed\xa1\xa4\xa6\xa8\xed\xac\xed\xbd\xa2\xb8\xa3\xa9\xed\xa2\xab\xed\xaf\xac\xae\xa2\xa3' 

Current char: 150 Score: 0 current deciphered result: b'\x8d\xa1\xa1\xa5\xa7\xa0\xa9\xee\x83\x8d\xe9\xbd\xee\xa2\xa7\xa5\xab\xee\xaf\xee\xbe\xa1\xbb\xa0\xaa\xee\xa1\xa8\xee\xac\xaf\xad\xa1\xa0' 

Current char: 151 Score: 0 current deciphered result: b'\x8c\xa0\xa0\xa4\xa6\xa1\xa8\xef\x82\x8c\xe8\xbc\xef\xa3\xa6\xa4\xaa\xef\xae\xef\xbf\xa0\xba\xa1\xab\xef\xa0\xa9\xef\xad\xae\xac\xa0\xa1' 

Current char: 152 Score: 0 current deciphered result: b'\x83\xaf\xaf\xab\xa9\xae\xa7\xe0\x8d\x83\xe7\xb3\xe0\xac\xa9\xab\xa5\xe0\xa1\xe0\xb0\xaf\xb5\xae\xa4\xe0\xaf\xa6\xe0\xa2\xa1\xa3\xaf\xae' 

Current char: 153 Score: 0 current deciphered result: b'\x82\xae\xae\xaa\xa8\xaf\xa6\xe1\x8c\x82\xe6\xb2\xe1\xad\xa8\xaa\xa4\xe1\xa0\xe1\xb1\xae\xb4\xaf\xa5\xe1\xae\xa7\xe1\xa3\xa0\xa2\xae\xaf' 

Current char: 154 Score: 0 current deciphered result: b'\x81\xad\xad\xa9\xab\xac\xa5\xe2\x8f\x81\xe5\xb1\xe2\xae\xab\xa9\xa7\xe2\xa3\xe2\xb2\xad\xb7\xac\xa6\xe2\xad\xa4\xe2\xa0\xa3\xa1\xad\xac' 

Current char: 155 Score: 0 current deciphered result: b'\x80\xac\xac\xa8\xaa\xad\xa4\xe3\x8e\x80\xe4\xb0\xe3\xaf\xaa\xa8\xa6\xe3\xa2\xe3\xb3\xac\xb6\xad\xa7\xe3\xac\xa5\xe3\xa1\xa2\xa0\xac\xad' 

Current char: 156 Score: 0 current deciphered result: b'\x87\xab\xab\xaf\xad\xaa\xa3\xe4\x89\x87\xe3\xb7\xe4\xa8\xad\xaf\xa1\xe4\xa5\xe4\xb4\xab\xb1\xaa\xa0\xe4\xab\xa2\xe4\xa6\xa5\xa7\xab\xaa' 

Current char: 157 Score: 0 current deciphered result: b'\x86\xaa\xaa\xae\xac\xab\xa2\xe5\x88\x86\xe2\xb6\xe5\xa9\xac\xae\xa0\xe5\xa4\xe5\xb5\xaa\xb0\xab\xa1\xe5\xaa\xa3\xe5\xa7\xa4\xa6\xaa\xab' 

Current char: 158 Score: 0 current deciphered result: b'\x85\xa9\xa9\xad\xaf\xa8\xa1\xe6\x8b\x85\xe1\xb5\xe6\xaa\xaf\xad\xa3\xe6\xa7\xe6\xb6\xa9\xb3\xa8\xa2\xe6\xa9\xa0\xe6\xa4\xa7\xa5\xa9\xa8' 

Current char: 159 Score: 0 current deciphered result: b'\x84\xa8\xa8\xac\xae\xa9\xa0\xe7\x8a\x84\xe0\xb4\xe7\xab\xae\xac\xa2\xe7\xa6\xe7\xb7\xa8\xb2\xa9\xa3\xe7\xa8\xa1\xe7\xa5\xa6\xa4\xa8\xa9' 

Current char: 160 Score: 0 current deciphered result: b'\xbb\x97\x97\x93\x91\x96\x9f\xd8\xb5\xbb\xdf\x8b\xd8\x94\x91\x93\x9d\xd8\x99\xd8\x88\x97\x8d\x96\x9c\xd8\x97\x9e\xd8\x9a\x99\x9b\x97\x96' 

Current char: 161 Score: 0 current deciphered result: b'\xba\x96\x96\x92\x90\x97\x9e\xd9\xb4\xba\xde\x8a\xd9\x95\x90\x92\x9c\xd9\x98\xd9\x89\x96\x8c\x97\x9d\xd9\x96\x9f\xd9\x9b\x98\x9a\x96\x97' 

Current char: 162 Score: 0 current deciphered result: b'\xb9\x95\x95\x91\x93\x94\x9d\xda\xb7\xb9\xdd\x89\xda\x96\x93\x91\x9f\xda\x9b\xda\x8a\x95\x8f\x94\x9e\xda\x95\x9c\xda\x98\x9b\x99\x95\x94' 

Current char: 163 Score: 0 current deciphered result: b'\xb8\x94\x94\x90\x92\x95\x9c\xdb\xb6\xb8\xdc\x88\xdb\x97\x92\x90\x9e\xdb\x9a\xdb\x8b\x94\x8e\x95\x9f\xdb\x94\x9d\xdb\x99\x9a\x98\x94\x95' 

Current char: 164 Score: 0 current deciphered result: b'\xbf\x93\x93\x97\x95\x92\x9b\xdc\xb1\xbf\xdb\x8f\xdc\x90\x95\x97\x99\xdc\x9d\xdc\x8c\x93\x89\x92\x98\xdc\x93\x9a\xdc\x9e\x9d\x9f\x93\x92' 

Current char: 165 Score: 0 current deciphered result: b'\xbe\x92\x92\x96\x94\x93\x9a\xdd\xb0\xbe\xda\x8e\xdd\x91\x94\x96\x98\xdd\x9c\xdd\x8d\x92\x88\x93\x99\xdd\x92\x9b\xdd\x9f\x9c\x9e\x92\x93' 

Current char: 166 Score: 0 current deciphered result: b'\xbd\x91\x91\x95\x97\x90\x99\xde\xb3\xbd\xd9\x8d\xde\x92\x97\x95\x9b\xde\x9f\xde\x8e\x91\x8b\x90\x9a\xde\x91\x98\xde\x9c\x9f\x9d\x91\x90' 

Current char: 167 Score: 0 current deciphered result: b'\xbc\x90\x90\x94\x96\x91\x98\xdf\xb2\xbc\xd8\x8c\xdf\x93\x96\x94\x9a\xdf\x9e\xdf\x8f\x90\x8a\x91\x9b\xdf\x90\x99\xdf\x9d\x9e\x9c\x90\x91' 

Current char: 168 Score: 0 current deciphered result: b'\xb3\x9f\x9f\x9b\x99\x9e\x97\xd0\xbd\xb3\xd7\x83\xd0\x9c\x99\x9b\x95\xd0\x91\xd0\x80\x9f\x85\x9e\x94\xd0\x9f\x96\xd0\x92\x91\x93\x9f\x9e' 

Current char: 169 Score: 0 current deciphered result: b'\xb2\x9e\x9e\x9a\x98\x9f\x96\xd1\xbc\xb2\xd6\x82\xd1\x9d\x98\x9a\x94\xd1\x90\xd1\x81\x9e\x84\x9f\x95\xd1\x9e\x97\xd1\x93\x90\x92\x9e\x9f' 

Current char: 170 Score: 0 current deciphered result: b'\xb1\x9d\x9d\x99\x9b\x9c\x95\xd2\xbf\xb1\xd5\x81\xd2\x9e\x9b\x99\x97\xd2\x93\xd2\x82\x9d\x87\x9c\x96\xd2\x9d\x94\xd2\x90\x93\x91\x9d\x9c' 

Current char: 171 Score: 0 current deciphered result: b'\xb0\x9c\x9c\x98\x9a\x9d\x94\xd3\xbe\xb0\xd4\x80\xd3\x9f\x9a\x98\x96\xd3\x92\xd3\x83\x9c\x86\x9d\x97\xd3\x9c\x95\xd3\x91\x92\x90\x9c\x9d' 

Current char: 172 Score: 0 current deciphered result: b'\xb7\x9b\x9b\x9f\x9d\x9a\x93\xd4\xb9\xb7\xd3\x87\xd4\x98\x9d\x9f\x91\xd4\x95\xd4\x84\x9b\x81\x9a\x90\xd4\x9b\x92\xd4\x96\x95\x97\x9b\x9a' 

Current char: 173 Score: 0 current deciphered result: b'\xb6\x9a\x9a\x9e\x9c\x9b\x92\xd5\xb8\xb6\xd2\x86\xd5\x99\x9c\x9e\x90\xd5\x94\xd5\x85\x9a\x80\x9b\x91\xd5\x9a\x93\xd5\x97\x94\x96\x9a\x9b' 

Current char: 174 Score: 0 current deciphered result: b'\xb5\x99\x99\x9d\x9f\x98\x91\xd6\xbb\xb5\xd1\x85\xd6\x9a\x9f\x9d\x93\xd6\x97\xd6\x86\x99\x83\x98\x92\xd6\x99\x90\xd6\x94\x97\x95\x99\x98' 

Current char: 175 Score: 0 current deciphered result: b'\xb4\x98\x98\x9c\x9e\x99\x90\xd7\xba\xb4\xd0\x84\xd7\x9b\x9e\x9c\x92\xd7\x96\xd7\x87\x98\x82\x99\x93\xd7\x98\x91\xd7\x95\x96\x94\x98\x99' 

Current char: 176 Score: 0 current deciphered result: b'\xab\x87\x87\x83\x81\x86\x8f\xc8\xa5\xab\xcf\x9b\xc8\x84\x81\x83\x8d\xc8\x89\xc8\x98\x87\x9d\x86\x8c\xc8\x87\x8e\xc8\x8a\x89\x8b\x87\x86' 

Current char: 177 Score: 0 current deciphered result: b'\xaa\x86\x86\x82\x80\x87\x8e\xc9\xa4\xaa\xce\x9a\xc9\x85\x80\x82\x8c\xc9\x88\xc9\x99\x86\x9c\x87\x8d\xc9\x86\x8f\xc9\x8b\x88\x8a\x86\x87' 

Current char: 178 Score: 0 current deciphered result: b'\xa9\x85\x85\x81\x83\x84\x8d\xca\xa7\xa9\xcd\x99\xca\x86\x83\x81\x8f\xca\x8b\xca\x9a\x85\x9f\x84\x8e\xca\x85\x8c\xca\x88\x8b\x89\x85\x84' 

Current char: 179 Score: 0 current deciphered result: b'\xa8\x84\x84\x80\x82\x85\x8c\xcb\xa6\xa8\xcc\x98\xcb\x87\x82\x80\x8e\xcb\x8a\xcb\x9b\x84\x9e\x85\x8f\xcb\x84\x8d\xcb\x89\x8a\x88\x84\x85' 

Current char: 180 Score: 0 current deciphered result: b'\xaf\x83\x83\x87\x85\x82\x8b\xcc\xa1\xaf\xcb\x9f\xcc\x80\x85\x87\x89\xcc\x8d\xcc\x9c\x83\x99\x82\x88\xcc\x83\x8a\xcc\x8e\x8d\x8f\x83\x82' 

Current char: 181 Score: 0 current deciphered result: b'\xae\x82\x82\x86\x84\x83\x8a\xcd\xa0\xae\xca\x9e\xcd\x81\x84\x86\x88\xcd\x8c\xcd\x9d\x82\x98\x83\x89\xcd\x82\x8b\xcd\x8f\x8c\x8e\x82\x83' 

Current char: 182 Score: 0 current deciphered result: b'\xad\x81\x81\x85\x87\x80\x89\xce\xa3\xad\xc9\x9d\xce\x82\x87\x85\x8b\xce\x8f\xce\x9e\x81\x9b\x80\x8a\xce\x81\x88\xce\x8c\x8f\x8d\x81\x80' 

Current char: 183 Score: 0 current deciphered result: b'\xac\x80\x80\x84\x86\x81\x88\xcf\xa2\xac\xc8\x9c\xcf\x83\x86\x84\x8a\xcf\x8e\xcf\x9f\x80\x9a\x81\x8b\xcf\x80\x89\xcf\x8d\x8e\x8c\x80\x81' 

Current char: 184 Score: 0 current deciphered result: b'\xa3\x8f\x8f\x8b\x89\x8e\x87\xc0\xad\xa3\xc7\x93\xc0\x8c\x89\x8b\x85\xc0\x81\xc0\x90\x8f\x95\x8e\x84\xc0\x8f\x86\xc0\x82\x81\x83\x8f\x8e' 

Current char: 185 Score: 0 current deciphered result: b'\xa2\x8e\x8e\x8a\x88\x8f\x86\xc1\xac\xa2\xc6\x92\xc1\x8d\x88\x8a\x84\xc1\x80\xc1\x91\x8e\x94\x8f\x85\xc1\x8e\x87\xc1\x83\x80\x82\x8e\x8f' 

Current char: 186 Score: 0 current deciphered result: b'\xa1\x8d\x8d\x89\x8b\x8c\x85\xc2\xaf\xa1\xc5\x91\xc2\x8e\x8b\x89\x87\xc2\x83\xc2\x92\x8d\x97\x8c\x86\xc2\x8d\x84\xc2\x80\x83\x81\x8d\x8c' 

Current char: 187 Score: 0 current deciphered result: b'\xa0\x8c\x8c\x88\x8a\x8d\x84\xc3\xae\xa0\xc4\x90\xc3\x8f\x8a\x88\x86\xc3\x82\xc3\x93\x8c\x96\x8d\x87\xc3\x8c\x85\xc3\x81\x82\x80\x8c\x8d' 

Current char: 188 Score: 0 current deciphered result: b'\xa7\x8b\x8b\x8f\x8d\x8a\x83\xc4\xa9\xa7\xc3\x97\xc4\x88\x8d\x8f\x81\xc4\x85\xc4\x94\x8b\x91\x8a\x80\xc4\x8b\x82\xc4\x86\x85\x87\x8b\x8a' 

Current char: 189 Score: 0 current deciphered result: b'\xa6\x8a\x8a\x8e\x8c\x8b\x82\xc5\xa8\xa6\xc2\x96\xc5\x89\x8c\x8e\x80\xc5\x84\xc5\x95\x8a\x90\x8b\x81\xc5\x8a\x83\xc5\x87\x84\x86\x8a\x8b' 

Current char: 190 Score: 0 current deciphered result: b'\xa5\x89\x89\x8d\x8f\x88\x81\xc6\xab\xa5\xc1\x95\xc6\x8a\x8f\x8d\x83\xc6\x87\xc6\x96\x89\x93\x88\x82\xc6\x89\x80\xc6\x84\x87\x85\x89\x88' 

Current char: 191 Score: 0 current deciphered result: b'\xa4\x88\x88\x8c\x8e\x89\x80\xc7\xaa\xa4\xc0\x94\xc7\x8b\x8e\x8c\x82\xc7\x86\xc7\x97\x88\x92\x89\x83\xc7\x88\x81\xc7\x85\x86\x84\x88\x89' 

Current char: 192 Score: 0 current deciphered result: b'\xdb\xf7\xf7\xf3\xf1\xf6\xff\xb8\xd5\xdb\xbf\xeb\xb8\xf4\xf1\xf3\xfd\xb8\xf9\xb8\xe8\xf7\xed\xf6\xfc\xb8\xf7\xfe\xb8\xfa\xf9\xfb\xf7\xf6' 

Current char: 193 Score: 0 current deciphered result: b'\xda\xf6\xf6\xf2\xf0\xf7\xfe\xb9\xd4\xda\xbe\xea\xb9\xf5\xf0\xf2\xfc\xb9\xf8\xb9\xe9\xf6\xec\xf7\xfd\xb9\xf6\xff\xb9\xfb\xf8\xfa\xf6\xf7' 

Current char: 194 Score: 0 current deciphered result: b'\xd9\xf5\xf5\xf1\xf3\xf4\xfd\xba\xd7\xd9\xbd\xe9\xba\xf6\xf3\xf1\xff\xba\xfb\xba\xea\xf5\xef\xf4\xfe\xba\xf5\xfc\xba\xf8\xfb\xf9\xf5\xf4' 

Current char: 195 Score: 0 current deciphered result: b'\xd8\xf4\xf4\xf0\xf2\xf5\xfc\xbb\xd6\xd8\xbc\xe8\xbb\xf7\xf2\xf0\xfe\xbb\xfa\xbb\xeb\xf4\xee\xf5\xff\xbb\xf4\xfd\xbb\xf9\xfa\xf8\xf4\xf5' 

Current char: 196 Score: 0 current deciphered result: b'\xdf\xf3\xf3\xf7\xf5\xf2\xfb\xbc\xd1\xdf\xbb\xef\xbc\xf0\xf5\xf7\xf9\xbc\xfd\xbc\xec\xf3\xe9\xf2\xf8\xbc\xf3\xfa\xbc\xfe\xfd\xff\xf3\xf2' 

Current char: 197 Score: 0 current deciphered result: b'\xde\xf2\xf2\xf6\xf4\xf3\xfa\xbd\xd0\xde\xba\xee\xbd\xf1\xf4\xf6\xf8\xbd\xfc\xbd\xed\xf2\xe8\xf3\xf9\xbd\xf2\xfb\xbd\xff\xfc\xfe\xf2\xf3' 

Current char: 198 Score: 0 current deciphered result: b'\xdd\xf1\xf1\xf5\xf7\xf0\xf9\xbe\xd3\xdd\xb9\xed\xbe\xf2\xf7\xf5\xfb\xbe\xff\xbe\xee\xf1\xeb\xf0\xfa\xbe\xf1\xf8\xbe\xfc\xff\xfd\xf1\xf0' 

Current char: 199 Score: 0 current deciphered result: b'\xdc\xf0\xf0\xf4\xf6\xf1\xf8\xbf\xd2\xdc\xb8\xec\xbf\xf3\xf6\xf4\xfa\xbf\xfe\xbf\xef\xf0\xea\xf1\xfb\xbf\xf0\xf9\xbf\xfd\xfe\xfc\xf0\xf1' 

Current char: 200 Score: 0 current deciphered result: b'\xd3\xff\xff\xfb\xf9\xfe\xf7\xb0\xdd\xd3\xb7\xe3\xb0\xfc\xf9\xfb\xf5\xb0\xf1\xb0\xe0\xff\xe5\xfe\xf4\xb0\xff\xf6\xb0\xf2\xf1\xf3\xff\xfe' 

Current char: 201 Score: 0 current deciphered result: b'\xd2\xfe\xfe\xfa\xf8\xff\xf6\xb1\xdc\xd2\xb6\xe2\xb1\xfd\xf8\xfa\xf4\xb1\xf0\xb1\xe1\xfe\xe4\xff\xf5\xb1\xfe\xf7\xb1\xf3\xf0\xf2\xfe\xff' 

Current char: 202 Score: 0 current deciphered result: b'\xd1\xfd\xfd\xf9\xfb\xfc\xf5\xb2\xdf\xd1\xb5\xe1\xb2\xfe\xfb\xf9\xf7\xb2\xf3\xb2\xe2\xfd\xe7\xfc\xf6\xb2\xfd\xf4\xb2\xf0\xf3\xf1\xfd\xfc' 

Current char: 203 Score: 0 current deciphered result: b'\xd0\xfc\xfc\xf8\xfa\xfd\xf4\xb3\xde\xd0\xb4\xe0\xb3\xff\xfa\xf8\xf6\xb3\xf2\xb3\xe3\xfc\xe6\xfd\xf7\xb3\xfc\xf5\xb3\xf1\xf2\xf0\xfc\xfd' 

Current char: 204 Score: 0 current deciphered result: b'\xd7\xfb\xfb\xff\xfd\xfa\xf3\xb4\xd9\xd7\xb3\xe7\xb4\xf8\xfd\xff\xf1\xb4\xf5\xb4\xe4\xfb\xe1\xfa\xf0\xb4\xfb\xf2\xb4\xf6\xf5\xf7\xfb\xfa' 

Current char: 205 Score: 0 current deciphered result: b'\xd6\xfa\xfa\xfe\xfc\xfb\xf2\xb5\xd8\xd6\xb2\xe6\xb5\xf9\xfc\xfe\xf0\xb5\xf4\xb5\xe5\xfa\xe0\xfb\xf1\xb5\xfa\xf3\xb5\xf7\xf4\xf6\xfa\xfb' 

Current char: 206 Score: 0 current deciphered result: b'\xd5\xf9\xf9\xfd\xff\xf8\xf1\xb6\xdb\xd5\xb1\xe5\xb6\xfa\xff\xfd\xf3\xb6\xf7\xb6\xe6\xf9\xe3\xf8\xf2\xb6\xf9\xf0\xb6\xf4\xf7\xf5\xf9\xf8' 

Current char: 207 Score: 0 current deciphered result: b'\xd4\xf8\xf8\xfc\xfe\xf9\xf0\xb7\xda\xd4\xb0\xe4\xb7\xfb\xfe\xfc\xf2\xb7\xf6\xb7\xe7\xf8\xe2\xf9\xf3\xb7\xf8\xf1\xb7\xf5\xf6\xf4\xf8\xf9' 

Current char: 208 Score: 0 current deciphered result: b'\xcb\xe7\xe7\xe3\xe1\xe6\xef\xa8\xc5\xcb\xaf\xfb\xa8\xe4\xe1\xe3\xed\xa8\xe9\xa8\xf8\xe7\xfd\xe6\xec\xa8\xe7\xee\xa8\xea\xe9\xeb\xe7\xe6' 

Current char: 209 Score: 0 current deciphered result: b'\xca\xe6\xe6\xe2\xe0\xe7\xee\xa9\xc4\xca\xae\xfa\xa9\xe5\xe0\xe2\xec\xa9\xe8\xa9\xf9\xe6\xfc\xe7\xed\xa9\xe6\xef\xa9\xeb\xe8\xea\xe6\xe7' 

Current char: 210 Score: 0 current deciphered result: b'\xc9\xe5\xe5\xe1\xe3\xe4\xed\xaa\xc7\xc9\xad\xf9\xaa\xe6\xe3\xe1\xef\xaa\xeb\xaa\xfa\xe5\xff\xe4\xee\xaa\xe5\xec\xaa\xe8\xeb\xe9\xe5\xe4' 

Current char: 211 Score: 0 current deciphered result: b'\xc8\xe4\xe4\xe0\xe2\xe5\xec\xab\xc6\xc8\xac\xf8\xab\xe7\xe2\xe0\xee\xab\xea\xab\xfb\xe4\xfe\xe5\xef\xab\xe4\xed\xab\xe9\xea\xe8\xe4\xe5' 

Current char: 212 Score: 0 current deciphered result: b'\xcf\xe3\xe3\xe7\xe5\xe2\xeb\xac\xc1\xcf\xab\xff\xac\xe0\xe5\xe7\xe9\xac\xed\xac\xfc\xe3\xf9\xe2\xe8\xac\xe3\xea\xac\xee\xed\xef\xe3\xe2' 

Current char: 213 Score: 0 current deciphered result: b'\xce\xe2\xe2\xe6\xe4\xe3\xea\xad\xc0\xce\xaa\xfe\xad\xe1\xe4\xe6\xe8\xad\xec\xad\xfd\xe2\xf8\xe3\xe9\xad\xe2\xeb\xad\xef\xec\xee\xe2\xe3' 

Current char: 214 Score: 0 current deciphered result: b'\xcd\xe1\xe1\xe5\xe7\xe0\xe9\xae\xc3\xcd\xa9\xfd\xae\xe2\xe7\xe5\xeb\xae\xef\xae\xfe\xe1\xfb\xe0\xea\xae\xe1\xe8\xae\xec\xef\xed\xe1\xe0' 

Current char: 215 Score: 0 current deciphered result: b'\xcc\xe0\xe0\xe4\xe6\xe1\xe8\xaf\xc2\xcc\xa8\xfc\xaf\xe3\xe6\xe4\xea\xaf\xee\xaf\xff\xe0\xfa\xe1\xeb\xaf\xe0\xe9\xaf\xed\xee\xec\xe0\xe1' 

Current char: 216 Score: 0 current deciphered result: b'\xc3\xef\xef\xeb\xe9\xee\xe7\xa0\xcd\xc3\xa7\xf3\xa0\xec\xe9\xeb\xe5\xa0\xe1\xa0\xf0\xef\xf5\xee\xe4\xa0\xef\xe6\xa0\xe2\xe1\xe3\xef\xee' 

Current char: 217 Score: 0 current deciphered result: b'\xc2\xee\xee\xea\xe8\xef\xe6\xa1\xcc\xc2\xa6\xf2\xa1\xed\xe8\xea\xe4\xa1\xe0\xa1\xf1\xee\xf4\xef\xe5\xa1\xee\xe7\xa1\xe3\xe0\xe2\xee\xef' 

Current char: 218 Score: 0 current deciphered result: b'\xc1\xed\xed\xe9\xeb\xec\xe5\xa2\xcf\xc1\xa5\xf1\xa2\xee\xeb\xe9\xe7\xa2\xe3\xa2\xf2\xed\xf7\xec\xe6\xa2\xed\xe4\xa2\xe0\xe3\xe1\xed\xec' 

Current char: 219 Score: 0 current deciphered result: b'\xc0\xec\xec\xe8\xea\xed\xe4\xa3\xce\xc0\xa4\xf0\xa3\xef\xea\xe8\xe6\xa3\xe2\xa3\xf3\xec\xf6\xed\xe7\xa3\xec\xe5\xa3\xe1\xe2\xe0\xec\xed' 

Current char: 220 Score: 0 current deciphered result: b'\xc7\xeb\xeb\xef\xed\xea\xe3\xa4\xc9\xc7\xa3\xf7\xa4\xe8\xed\xef\xe1\xa4\xe5\xa4\xf4\xeb\xf1\xea\xe0\xa4\xeb\xe2\xa4\xe6\xe5\xe7\xeb\xea' 

Current char: 221 Score: 0 current deciphered result: b'\xc6\xea\xea\xee\xec\xeb\xe2\xa5\xc8\xc6\xa2\xf6\xa5\xe9\xec\xee\xe0\xa5\xe4\xa5\xf5\xea\xf0\xeb\xe1\xa5\xea\xe3\xa5\xe7\xe4\xe6\xea\xeb' 

Current char: 222 Score: 0 current deciphered result: b'\xc5\xe9\xe9\xed\xef\xe8\xe1\xa6\xcb\xc5\xa1\xf5\xa6\xea\xef\xed\xe3\xa6\xe7\xa6\xf6\xe9\xf3\xe8\xe2\xa6\xe9\xe0\xa6\xe4\xe7\xe5\xe9\xe8' 

Current char: 223 Score: 0 current deciphered result: b'\xc4\xe8\xe8\xec\xee\xe9\xe0\xa7\xca\xc4\xa0\xf4\xa7\xeb\xee\xec\xe2\xa7\xe6\xa7\xf7\xe8\xf2\xe9\xe3\xa7\xe8\xe1\xa7\xe5\xe6\xe4\xe8\xe9' 

Current char: 224 Score: 0 current deciphered result: b'\xfb\xd7\xd7\xd3\xd1\xd6\xdf\x98\xf5\xfb\x9f\xcb\x98\xd4\xd1\xd3\xdd\x98\xd9\x98\xc8\xd7\xcd\xd6\xdc\x98\xd7\xde\x98\xda\xd9\xdb\xd7\xd6' 

Current char: 225 Score: 0 current deciphered result: b'\xfa\xd6\xd6\xd2\xd0\xd7\xde\x99\xf4\xfa\x9e\xca\x99\xd5\xd0\xd2\xdc\x99\xd8\x99\xc9\xd6\xcc\xd7\xdd\x99\xd6\xdf\x99\xdb\xd8\xda\xd6\xd7' 

Current char: 226 Score: 0 current deciphered result: b'\xf9\xd5\xd5\xd1\xd3\xd4\xdd\x9a\xf7\xf9\x9d\xc9\x9a\xd6\xd3\xd1\xdf\x9a\xdb\x9a\xca\xd5\xcf\xd4\xde\x9a\xd5\xdc\x9a\xd8\xdb\xd9\xd5\xd4' 

Current char: 227 Score: 0 current deciphered result: b'\xf8\xd4\xd4\xd0\xd2\xd5\xdc\x9b\xf6\xf8\x9c\xc8\x9b\xd7\xd2\xd0\xde\x9b\xda\x9b\xcb\xd4\xce\xd5\xdf\x9b\xd4\xdd\x9b\xd9\xda\xd8\xd4\xd5' 

Current char: 228 Score: 0 current deciphered result: b'\xff\xd3\xd3\xd7\xd5\xd2\xdb\x9c\xf1\xff\x9b\xcf\x9c\xd0\xd5\xd7\xd9\x9c\xdd\x9c\xcc\xd3\xc9\xd2\xd8\x9c\xd3\xda\x9c\xde\xdd\xdf\xd3\xd2' 

Current char: 229 Score: 0 current deciphered result: b'\xfe\xd2\xd2\xd6\xd4\xd3\xda\x9d\xf0\xfe\x9a\xce\x9d\xd1\xd4\xd6\xd8\x9d\xdc\x9d\xcd\xd2\xc8\xd3\xd9\x9d\xd2\xdb\x9d\xdf\xdc\xde\xd2\xd3' 

Current char: 230 Score: 0 current deciphered result: b'\xfd\xd1\xd1\xd5\xd7\xd0\xd9\x9e\xf3\xfd\x99\xcd\x9e\xd2\xd7\xd5\xdb\x9e\xdf\x9e\xce\xd1\xcb\xd0\xda\x9e\xd1\xd8\x9e\xdc\xdf\xdd\xd1\xd0' 

Current char: 231 Score: 0 current deciphered result: b'\xfc\xd0\xd0\xd4\xd6\xd1\xd8\x9f\xf2\xfc\x98\xcc\x9f\xd3\xd6\xd4\xda\x9f\xde\x9f\xcf\xd0\xca\xd1\xdb\x9f\xd0\xd9\x9f\xdd\xde\xdc\xd0\xd1' 

Current char: 232 Score: 0 current deciphered result: b'\xf3\xdf\xdf\xdb\xd9\xde\xd7\x90\xfd\xf3\x97\xc3\x90\xdc\xd9\xdb\xd5\x90\xd1\x90\xc0\xdf\xc5\xde\xd4\x90\xdf\xd6\x90\xd2\xd1\xd3\xdf\xde' 

Current char: 233 Score: 0 current deciphered result: b'\xf2\xde\xde\xda\xd8\xdf\xd6\x91\xfc\xf2\x96\xc2\x91\xdd\xd8\xda\xd4\x91\xd0\x91\xc1\xde\xc4\xdf\xd5\x91\xde\xd7\x91\xd3\xd0\xd2\xde\xdf' 

Current char: 234 Score: 0 current deciphered result: b'\xf1\xdd\xdd\xd9\xdb\xdc\xd5\x92\xff\xf1\x95\xc1\x92\xde\xdb\xd9\xd7\x92\xd3\x92\xc2\xdd\xc7\xdc\xd6\x92\xdd\xd4\x92\xd0\xd3\xd1\xdd\xdc' 

Current char: 235 Score: 0 current deciphered result: b'\xf0\xdc\xdc\xd8\xda\xdd\xd4\x93\xfe\xf0\x94\xc0\x93\xdf\xda\xd8\xd6\x93\xd2\x93\xc3\xdc\xc6\xdd\xd7\x93\xdc\xd5\x93\xd1\xd2\xd0\xdc\xdd' 

Current char: 236 Score: 0 current deciphered result: b'\xf7\xdb\xdb\xdf\xdd\xda\xd3\x94\xf9\xf7\x93\xc7\x94\xd8\xdd\xdf\xd1\x94\xd5\x94\xc4\xdb\xc1\xda\xd0\x94\xdb\xd2\x94\xd6\xd5\xd7\xdb\xda' 

Current char: 237 Score: 0 current deciphered result: b'\xf6\xda\xda\xde\xdc\xdb\xd2\x95\xf8\xf6\x92\xc6\x95\xd9\xdc\xde\xd0\x95\xd4\x95\xc5\xda\xc0\xdb\xd1\x95\xda\xd3\x95\xd7\xd4\xd6\xda\xdb' 

Current char: 238 Score: 0 current deciphered result: b'\xf5\xd9\xd9\xdd\xdf\xd8\xd1\x96\xfb\xf5\x91\xc5\x96\xda\xdf\xdd\xd3\x96\xd7\x96\xc6\xd9\xc3\xd8\xd2\x96\xd9\xd0\x96\xd4\xd7\xd5\xd9\xd8' 

Current char: 239 Score: 0 current deciphered result: b'\xf4\xd8\xd8\xdc\xde\xd9\xd0\x97\xfa\xf4\x90\xc4\x97\xdb\xde\xdc\xd2\x97\xd6\x97\xc7\xd8\xc2\xd9\xd3\x97\xd8\xd1\x97\xd5\xd6\xd4\xd8\xd9' 

Current char: 240 Score: 0 current deciphered result: b'\xeb\xc7\xc7\xc3\xc1\xc6\xcf\x88\xe5\xeb\x8f\xdb\x88\xc4\xc1\xc3\xcd\x88\xc9\x88\xd8\xc7\xdd\xc6\xcc\x88\xc7\xce\x88\xca\xc9\xcb\xc7\xc6' 

Current char: 241 Score: 0 current deciphered result: b'\xea\xc6\xc6\xc2\xc0\xc7\xce\x89\xe4\xea\x8e\xda\x89\xc5\xc0\xc2\xcc\x89\xc8\x89\xd9\xc6\xdc\xc7\xcd\x89\xc6\xcf\x89\xcb\xc8\xca\xc6\xc7' 

Current char: 242 Score: 0 current deciphered result: b'\xe9\xc5\xc5\xc1\xc3\xc4\xcd\x8a\xe7\xe9\x8d\xd9\x8a\xc6\xc3\xc1\xcf\x8a\xcb\x8a\xda\xc5\xdf\xc4\xce\x8a\xc5\xcc\x8a\xc8\xcb\xc9\xc5\xc4' 

Current char: 243 Score: 0 current deciphered result: b'\xe8\xc4\xc4\xc0\xc2\xc5\xcc\x8b\xe6\xe8\x8c\xd8\x8b\xc7\xc2\xc0\xce\x8b\xca\x8b\xdb\xc4\xde\xc5\xcf\x8b\xc4\xcd\x8b\xc9\xca\xc8\xc4\xc5' 

Current char: 244 Score: 0 current deciphered result: b'\xef\xc3\xc3\xc7\xc5\xc2\xcb\x8c\xe1\xef\x8b\xdf\x8c\xc0\xc5\xc7\xc9\x8c\xcd\x8c\xdc\xc3\xd9\xc2\xc8\x8c\xc3\xca\x8c\xce\xcd\xcf\xc3\xc2' 

Current char: 245 Score: 0 current deciphered result: b'\xee\xc2\xc2\xc6\xc4\xc3\xca\x8d\xe0\xee\x8a\xde\x8d\xc1\xc4\xc6\xc8\x8d\xcc\x8d\xdd\xc2\xd8\xc3\xc9\x8d\xc2\xcb\x8d\xcf\xcc\xce\xc2\xc3' 

Current char: 246 Score: 0 current deciphered result: b'\xed\xc1\xc1\xc5\xc7\xc0\xc9\x8e\xe3\xed\x89\xdd\x8e\xc2\xc7\xc5\xcb\x8e\xcf\x8e\xde\xc1\xdb\xc0\xca\x8e\xc1\xc8\x8e\xcc\xcf\xcd\xc1\xc0' 

Current char: 247 Score: 0 current deciphered result: b'\xec\xc0\xc0\xc4\xc6\xc1\xc8\x8f\xe2\xec\x88\xdc\x8f\xc3\xc6\xc4\xca\x8f\xce\x8f\xdf\xc0\xda\xc1\xcb\x8f\xc0\xc9\x8f\xcd\xce\xcc\xc0\xc1' 

Current char: 248 Score: 0 current deciphered result: b'\xe3\xcf\xcf\xcb\xc9\xce\xc7\x80\xed\xe3\x87\xd3\x80\xcc\xc9\xcb\xc5\x80\xc1\x80\xd0\xcf\xd5\xce\xc4\x80\xcf\xc6\x80\xc2\xc1\xc3\xcf\xce' 

Current char: 249 Score: 0 current deciphered result: b'\xe2\xce\xce\xca\xc8\xcf\xc6\x81\xec\xe2\x86\xd2\x81\xcd\xc8\xca\xc4\x81\xc0\x81\xd1\xce\xd4\xcf\xc5\x81\xce\xc7\x81\xc3\xc0\xc2\xce\xcf' 

Current char: 250 Score: 0 current deciphered result: b'\xe1\xcd\xcd\xc9\xcb\xcc\xc5\x82\xef\xe1\x85\xd1\x82\xce\xcb\xc9\xc7\x82\xc3\x82\xd2\xcd\xd7\xcc\xc6\x82\xcd\xc4\x82\xc0\xc3\xc1\xcd\xcc' 

Current char: 251 Score: 0 current deciphered result: b'\xe0\xcc\xcc\xc8\xca\xcd\xc4\x83\xee\xe0\x84\xd0\x83\xcf\xca\xc8\xc6\x83\xc2\x83\xd3\xcc\xd6\xcd\xc7\x83\xcc\xc5\x83\xc1\xc2\xc0\xcc\xcd' 

Current char: 252 Score: 0 current deciphered result: b'\xe7\xcb\xcb\xcf\xcd\xca\xc3\x84\xe9\xe7\x83\xd7\x84\xc8\xcd\xcf\xc1\x84\xc5\x84\xd4\xcb\xd1\xca\xc0\x84\xcb\xc2\x84\xc6\xc5\xc7\xcb\xca' 

Current char: 253 Score: 0 current deciphered result: b'\xe6\xca\xca\xce\xcc\xcb\xc2\x85\xe8\xe6\x82\xd6\x85\xc9\xcc\xce\xc0\x85\xc4\x85\xd5\xca\xd0\xcb\xc1\x85\xca\xc3\x85\xc7\xc4\xc6\xca\xcb' 

Current char: 254 Score: 0 current deciphered result: b'\xe5\xc9\xc9\xcd\xcf\xc8\xc1\x86\xeb\xe5\x81\xd5\x86\xca\xcf\xcd\xc3\x86\xc7\x86\xd6\xc9\xd3\xc8\xc2\x86\xc9\xc0\x86\xc4\xc7\xc5\xc9\xc8' 

Current char: 255 Score: 0 current deciphered result: b'\xe4\xc8\xc8\xcc\xce\xc9\xc0\x87\xea\xe4\x80\xd4\x87\xcb\xce\xcc\xc2\x87\xc6\x87\xd7\xc8\xd2\xc9\xc3\x87\xc8\xc1\x87\xc5\xc6\xc4\xc8\xc9' 

Decyphered text with key: 88 and score: 2.2641049 

b"Cooking MC's like a pound of bacon"
```

### [Challenge 4](#challenge-4)

Using the same approach used in [challenge 3](#challenge-3), where now we use the english score to find the most likely sequence to be encrypted by a single byte xor cipher, therefore both detecting and decrypting using the english score metric.

Expected output: 
```python
Decyphered text with key: 53 and score: 2.0881317999999998 Cur line: 170 

b'Now that the party is jumping\n'
```

### [Challenge 5](#challenge-5)

Implemenating a simple repeating-key <a href="https://en.wikipedia.org/wiki/XOR_cipher">XOR cipher</a>, the implementation is very straight forward using a cyclic loop over the key characters.

Expected output: 
```python
sucess
```

### [Challenge 6](#challenge-6)

In this challenge we break a reapeating xor key also known as <a href="https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher">Vigenère cipher</a>. To do so we start by estimating the key length, to do so we break the cipher text into part of the size of key length. By measuring the normalized <a href="https://en.wikipedia.org/wiki/Hamming_distance">Hamming distance</a> of sequential sub part of the cipher text, we can create a ranking of the most likely key sizes. Now we transpose the cipher text with respect to blocks of key length size, and solve each block like a single character xor cipher as we have done before, using english text similarity ranking.

Expected output: 
```python
100%|██████████| 5/5 [00:02<00:00,  2.44it/s]

Key: b'Terminator X: Bring the noise' 

Key size: 29 

Plain text: b"I'm back and I'm ringin' the bell \nA rockin' on the mike while the fly girls yell \nIn ecstasy in the back of me \nWell that's my DJ Deshay cuttin' all them Z's \nHittin' hard and the girlies goin' crazy \nVanilla's on the mike, man I'm not lazy. \n\nI'm lettin' my drug kick in \nIt controls my mouth and I begin \nTo just let it flow, let my concepts go \nMy posse's to the side yellin', Go Vanilla Go! \n\nSmooth 'cause that's the way I will be \nAnd if you don't give a damn, then \nWhy you starin' at me \nSo get off 'cause I control the stage \nThere's no dissin' allowed \nI'm in my own phase \nThe girlies sa y they love me and that is ok \nAnd I can dance better than any kid n' play \n\nStage 2 -- Yea the one ya' wanna listen to \nIt's off my head so let the beat play through \nSo I can funk it up and make it sound good \n1-2-3 Yo -- Knock on some wood \nFor good luck, I like my rhymes atrocious \nSupercalafragilisticexpialidocious \nI'm an effect and that you can bet \nI can take a fly girl and make her wet. \n\nI'm like Samson -- Samson to Delilah \nThere's no denyin', You can try to hang \nBut you'll keep tryin' to get my style \nOver and over, practice makes perfect \nBut not if you're a loafer. \n\nYou'll get nowhere, no place, no time, no girls \nSoon -- Oh my God, homebody, you probably eat \nSpaghetti with a spoon! Come on and say it! \n\nVIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino \nIntoxicating so you stagger like a wino \nSo punks stop trying and girl stop cryin' \nVanilla Ice is sellin' and you people are buyin' \n'Cause why the freaks are jockin' like Crazy Glue \nMovin' and groovin' trying to sing along \nAll through the ghetto groovin' this here song \nNow you're amazed by the VIP posse. \n\nSteppin' so hard like a German Nazi \nStartled by the bases hittin' ground \nThere's no trippin' on mine, I'm just gettin' down \nSparkamatic, I'm hangin' tight like a fanatic \nYou trapped me once and I thought that \nYou might have it \nSo step down and lend me your ear \n'89 in my time! You, '90 is my year. \n\nYou're weakenin' fast, YO! and I can tell it \nYour body's gettin' hot, so, so I can smell it \nSo don't be mad and don't be sad \n'Cause the lyrics belong to ICE, You can call me Dad \nYou're pitchin' a fit, so step back and endure \nLet the witch doctor, Ice, do the dance to cure \nSo come up close and don't be square \nYou wanna battle me -- Anytime, anywhere \n\nYou thought that I was weak, Boy, you're dead wrong \nSo come on, everybody and sing this song \n\nSay -- Play that funky music Say, go white boy, go white boy go \nplay that funky music Go white boy, go white boy, go \nLay down and boogie and play that funky music till you die. \n\nPlay that funky music Come on, Come on, let me hear \nPlay that funky music white boy you say it, say it \nPlay that funky music A little louder now \nPlay that funky music, white boy Come on, Come on, Come on \nPlay that funky music \n" 
```

### [Challenge 7](#challenge-7)

### [Challenge 8](#challenge-8)

## Set 2: Block crypto

### [Challenge 9](#challenge-9)

### [Challenge 10](#challenge-10)

### [Challenge 11](#challenge-11)

### [Challenge 12](#challenge-12)

### [Challenge 13](#challenge-13)

### [Challenge 14](#challenge-14)

### [Challenge 15](#challenge-15)

### [Challenge 16](#challenge-16)

## Set 3: Block & stream crypto

### [Challenge 17](#challenge-17)

### [Challenge 18](#challenge-18)

### [Challenge 19](#challenge-19)

### [Challenge 20](#challenge-20)

### [Challenge 21](#challenge-21)

### [Challenge 22](#challenge-22)

### [Challenge 23](#challenge-23)

### [Challenge 24](#challenge-24)

## Set 4: Stream crypto and randomness

### [Challenge 25](#challenge-25)

### [Challenge 26](#challenge-26)

### [Challenge 27](#challenge-27)

### [Challenge 28](#challenge-28)

### [Challenge 29](#challenge-29)

### [Challenge 30](#challenge-30)

### [Challenge 31](#challenge-31)

### [Challenge 32](#challenge-32)

## Set 5: Diffie-Hellman and friends

### [Challenge 33](#challenge-33)

### [Challenge 34](#challenge-34)

### [Challenge 35](#challenge-35)

### [Challenge 36](#challenge-36)

### [Challenge 37](#challenge-37)

### [Challenge 38](#challenge-38)

### [Challenge 39](#challenge-39)

### [Challenge 40](#challenge-40)



# License

Everything in this repository is distributed under the terms of the MIT License. See file "LICENSE" for further reference.



