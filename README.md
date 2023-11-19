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
| <a href="https://cryptopals.com/sets/5/challenges/34">Challenge 34</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q52Client.py">Client</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q52Server.py">Server</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q52Attacker.py">Attacker</a> | [Explanation 34](#challenge-34) |
| <a href="https://cryptopals.com/sets/5/challenges/35">Challenge 35</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q53Client.py">Client</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q53Server.py">Server</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q53Attacker.py">Attacker</a> | [Explanation 35](#challenge-35) |
| <a href="https://cryptopals.com/sets/5/challenges/36">Challenge 36</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q54Client.py">Client</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q54Server.py">Server</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q54Utils.py">Utils</a> | [Explanation 36](#challenge-36) |
| <a href="https://cryptopals.com/sets/5/challenges/37">Challenge 37</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q55ClientSetupThanAttacker.py">Client setup than attack</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q55Server.py">Server</a> | [Explanation 37](#challenge-37) |
| <a href="https://cryptopals.com/sets/5/challenges/38">Challenge 38</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q56Client.py">Client</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q56Server.py">Server</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q56FakeServer.py">Fake server</a> | [Explanation 38](#challenge-38) |
| <a href="https://cryptopals.com/sets/5/challenges/39">Challenge 39</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q57.py">code</a> | [Explanation 39](#challenge-39) |
| <a href="https://cryptopals.com/sets/5/challenges/40">Challenge 40</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q58.py">code</a> | [Explanation 40](#challenge-40) |

## Set 6: RSA and DSA

| Challenge | Solution | Explanation |
| :---: | :---: | :---: |
| <a href="https://cryptopals.com/sets/6/challenges/41">Challenge 41</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q61.py">code</a> | [Explanation 41](#challenge-41) |
| <a href="https://cryptopals.com/sets/6/challenges/42">Challenge 42</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q62.py">code</a> | [Explanation 42](#challenge-42) |
| <a href="https://cryptopals.com/sets/6/challenges/43">Challenge 43</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q63.py">code</a> | [Explanation 43](#challenge-43) |
| <a href="https://cryptopals.com/sets/6/challenges/44">Challenge 44</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q64.py">code</a> | [Explanation 44](#challenge-44) |
| <a href="https://cryptopals.com/sets/6/challenges/45">Challenge 45</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q65.py">code</a> | [Explanation 45](#challenge-45) |
| <a href="https://cryptopals.com/sets/6/challenges/46">Challenge 46</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q66.py">code</a> | [Explanation 46](#challenge-46), <a href="https://youtu.be/xk4yorWfdIg">video</a> demonstration of the RSA parity oracle attack |
| <a href="https://cryptopals.com/sets/6/challenges/47">Challenge 47</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q67.py">code RSA-256</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q67BiggerRSA.py">code RSA-2048</a> | [Explanation 47](#challenge-47) |
| <a href="https://cryptopals.com/sets/6/challenges/48">Challenge 48</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q68Client.py">Client</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q68Server.py">Server</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q68Attacker.py">Attacker</a> | [Explanation 48](#challenge-48), <a href="https://www.youtube.com/watch?v=P7zTI4iIXl4">video</a> demonstration of the Bleichnbcher 98 attack on an old version of TLS |

## Set 7: Hashes

| Challenge | Solution | Explanation |
| :---: | :---: | :---: |
| <a href="https://cryptopals.com/sets/7/challenges/49">Challenge 49</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q71IVcontrol.py">code (Attacker controlled IV)</a>, <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q71Nocontrol.py">code (Attacker has no control of IV)</a> | [Explanation 49](#challenge-49) |
| <a href="https://cryptopals.com/sets/7/challenges/50">Challenge 50</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q72.py">code</a> | [Explanation 50](#challenge-50) |
| <a href="https://cryptopals.com/sets/7/challenges/51">Challenge 51</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q73.py">code</a> | [Explanation 51](#challenge-51) |
| <a href="https://cryptopals.com/sets/7/challenges/52">Challenge 52</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q74.py">code</a> | [Explanation 52](#challenge-52) |
| <a href="https://cryptopals.com/sets/7/challenges/53">Challenge 53</a> | <a href="https://github.com/danielt17/Cryptopals-challenges/blob/main/Q75.py">code</a> | [Explanation 53](#challenge-53) |
| <a href="https://cryptopals.com/sets/7/challenges/54">Challenge 54</a> | | [Explanation 54](#challenge-54) |
| <a href="https://cryptopals.com/sets/7/challenges/55">Challenge 55</a> | | [Explanation 55](#challenge-55) |
| <a href="https://cryptopals.com/sets/7/challenges/56">Challenge 56</a> | | [Explanation 56](#challenge-56) |

## Set 8: Abstract Algebra

| Challenge | Solution | Explanation |
| :---: | :---: | :---: |
| <a href="https://toadstyle.org/cryptopals/513b590b41d19eff3a0aa028023349fd.txt">Challenge 57</a> | | [Explanation 57](#challenge-57) |
| <a href="https://toadstyle.org/cryptopals/3e17c7b35fcf491d08c989081ed18c9a.txt">Challenge 58</a> | | [Explanation 58](#challenge-58) |
| <a href="https://toadstyle.org/cryptopals/a0833e607878a80fdc0808f889c721b1.txt">Challenge 59</a> | | [Explanation 59](#challenge-59) |
| <a href="https://toadstyle.org/cryptopals/c53b90a3e9e753ddad56edbbd33838aa.txt">Challenge 60</a> | | [Explanation 60](#challenge-60) |
| <a href="https://toadstyle.org/cryptopals/809dccecda0e94ea588d66c12a1cf593.txt">Challenge 61</a> | | [Explanation 61](#challenge-61) |
| <a href="https://toadstyle.org/cryptopals/76f2e314809b2a34ce9ff0d2a08f7a7f.txt">Challenge 62</a> | | [Explanation 62](#challenge-62) |
| <a href="https://toadstyle.org/cryptopals/2dfbf7e58fd43c140b62485f8d90bebe.txt">Challenge 63</a> | | [Explanation 63](#challenge-63) |
| <a href="https://toadstyle.org/cryptopals/1d79ee513b73e1e0367eae2297e9f234.txt">Challenge 64</a> | | [Explanation 64](#challenge-64) |
| <a href="https://toadstyle.org/cryptopals/a1a2e7311ec5f2535ec46eaebd4588f0.txt">Challenge 65</a> | | [Explanation 65](#challenge-65) |
| <a href="https://toadstyle.org/cryptopals/66.txt">Challenge 66</a> | | [Explanation 66](#challenge-66) |

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

Using <a href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">AES-128</a> in <a href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)">ECB mode</a> to decrypt the cipher text. AES-128 is a block cipher, meaning it works on blocks of size 128 bits. ECB mode is a mode of operation of a block cipher, a 128 bit block from the plain text is encrypted in the same way no matter where it is in text. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/60748408/135771177-229ff8fa-581e-4052-a905-35249ecfd9eb.png" />
</p>

This mode operation should not be used for encryption as we will see later, an image descrbing the problematic ECB mode operation can be seen below.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60748408/135771122-5163eac1-ce9d-4e47-8b13-c286a906c729.png" />
</p>

Expected output: 
```python
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
The girlies sa y they love me and that is ok 
And I can dance better than any kid n' play 

Stage 2 -- Yea the one ya' wanna listen to 
It's off my head so let the beat play through 
So I can funk it up and make it sound good 
1-2-3 Yo -- Knock on some wood 
For good luck, I like my rhymes atrocious 
Supercalafragilisticexpialidocious 
I'm an effect and that you can bet 
I can take a fly girl and make her wet. 

I'm like Samson -- Samson to Delilah 
There's no denyin', You can try to hang 
But you'll keep tryin' to get my style 
Over and over, practice makes perfect 
But not if you're a loafer. 

You'll get nowhere, no place, no time, no girls 
Soon -- Oh my God, homebody, you probably eat 
Spaghetti with a spoon! Come on and say it! 

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino 
Intoxicating so you stagger like a wino 
So punks stop trying and girl stop cryin' 
Vanilla Ice is sellin' and you people are buyin' 
'Cause why the freaks are jockin' like Crazy Glue 
Movin' and groovin' trying to sing along 
All through the ghetto groovin' this here song 
Now you're amazed by the VIP posse. 

Steppin' so hard like a German Nazi 
Startled by the bases hittin' ground 
There's no trippin' on mine, I'm just gettin' down 
Sparkamatic, I'm hangin' tight like a fanatic 
You trapped me once and I thought that 
You might have it 
So step down and lend me your ear 
'89 in my time! You, '90 is my year. 

You're weakenin' fast, YO! and I can tell it 
Your body's gettin' hot, so, so I can smell it 
So don't be mad and don't be sad 
'Cause the lyrics belong to ICE, You can call me Dad 
You're pitchin' a fit, so step back and endure 
Let the witch doctor, Ice, do the dance to cure 
So come up close and don't be square 
You wanna battle me -- Anytime, anywhere 

You thought that I was weak, Boy, you're dead wrong 
So come on, everybody and sing this song 

Say -- Play that funky music Say, go white boy, go white boy go 
play that funky music Go white boy, go white boy, go 
Lay down and boogie and play that funky music till you die. 

Play that funky music Come on, Come on, let me hear 
Play that funky music white boy you say it, say it 
Play that funky music A little louder now 
Play that funky music, white boy Come on, Come on, Come on 
Play that funky music 

```

### [Challenge 8](#challenge-8)

Inorder to detect which file has been encrypted by AES in ECB mode, we need to search for repeating 16 bytes blocks, as its very unlikely (2^-64 unlikely) that a repeating block will happeen for any other mode operation of AES.

Expected output: 
```python
AES ECB encrypted file: 165
```

## Set 2: Block crypto

### [Challenge 9](#challenge-9)

In this challange we are asked to implement the PKCS#7 padding scheme described <a href="https://datatracker.ietf.org/doc/html/rfc5652">here</a>, the idea behind this padding scheme is very simple. Let's say we have a text of size m, and the block cipher block size is n where n>m, we need a padding scheme which will make our text of length m tranform into length n so we can apply are block cipher. This is done in the following way: we have a block length of size n bytes and text of m bytes size (where n>m) therefore we append to the end of the text n-m bytes of the value n-m. 

Expected output: 
```python
Correct solution 

Original text: b'YELLOW SUBMARINE'. Padded text: b'YELLOW SUBMARINE\x04\x04\x04\x04' 

Unpadded text: b'YELLOW SUBMARINE'
```

### [Challenge 10](#challenge-10)

Implementing <a href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)">CBC mode</a> is a straight forward proces but one should first understand the need for it. In ECB mode we could only encrypt regular sized messages, although padding allows us to deal with variable length message. This isn't the main problem CBC comes to deal with, we want the same blocks to be encrypted into different ciphertexts, this negates frequency analysis techniques on single blocks. This allows us to make collisions (two encryption process have the same result) extremely unlikely around 2^-64 unlikely. This is achieved using the following construction, where each encryption dependents on the previous encryption process, to start the process we have to use a unique initializaion vector (IV) which is sent over a public channel (as it is for single use, otherwise we can exploit this). The mathmatical operation and diagrams describing the mode of opeartion can be seen below.

![image](https://user-images.githubusercontent.com/60748408/154333638-8bf15ec7-8e2a-421e-9b4d-edd3b0a5d448.png)

![image](https://user-images.githubusercontent.com/60748408/154333947-4b242f9a-c435-4d61-90de-153638a97284.png)
![image](https://user-images.githubusercontent.com/60748408/154334006-c65c2ffa-6050-4e1a-ab70-6ad5d1b1d6fe.png)

In the following image which we have used before, we can see the difference between encrypting using ECB mode and CBC (or other modes) of encryption.

![image](https://user-images.githubusercontent.com/60748408/154333678-1b6ab661-26e7-4712-a3e4-ed0a56382620.png)


Expected output: 
```python
Decrypted text: 

I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell 
In ecstasy in the back of me 
Well that's my DJ Deshay cuttin' all them Z's 
Hittin' hard and the girlies goin' crazy 
Vanilla's on the mike, man I'm not lazy. 

I'm lettin' my drug kick in 
It controls my mouth and I begin 
To just let it flow, let my concepts go 
My posse's to the side yellin', Go Vanilla Go! 

Smooth 'cause that's the way I will be 
And if you don't give a damn, then 
Why you starin' at me 
So get off 'cause I control the stage 
There's no dissin' allowed 
I'm in my own phase 
The girlies sa y they love me and that is ok 
And I can dance better than any kid n' play 

Stage 2 -- Yea the one ya' wanna listen to 
It's off my head so let the beat play through 
So I can funk it up and make it sound good 
1-2-3 Yo -- Knock on some wood 
For good luck, I like my rhymes atrocious 
Supercalafragilisticexpialidocious 
I'm an effect and that you can bet 
I can take a fly girl and make her wet. 

I'm like Samson -- Samson to Delilah 
There's no denyin', You can try to hang 
But you'll keep tryin' to get my style 
Over and over, practice makes perfect 
But not if you're a loafer. 

You'll get nowhere, no place, no time, no girls 
Soon -- Oh my God, homebody, you probably eat 
Spaghetti with a spoon! Come on and say it! 

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino 
Intoxicating so you stagger like a wino 
So punks stop trying and girl stop cryin' 
Vanilla Ice is sellin' and you people are buyin' 
'Cause why the freaks are jockin' like Crazy Glue 
Movin' and groovin' trying to sing along 
All through the ghetto groovin' this here song 
Now you're amazed by the VIP posse. 

Steppin' so hard like a German Nazi 
Startled by the bases hittin' ground 
There's no trippin' on mine, I'm just gettin' down 
Sparkamatic, I'm hangin' tight like a fanatic 
You trapped me once and I thought that 
You might have it 
So step down and lend me your ear 
'89 in my time! You, '90 is my year. 

You're weakenin' fast, YO! and I can tell it 
Your body's gettin' hot, so, so I can smell it 
So don't be mad and don't be sad 
'Cause the lyrics belong to ICE, You can call me Dad 
You're pitchin' a fit, so step back and endure 
Let the witch doctor, Ice, do the dance to cure 
So come up close and don't be square 
You wanna battle me -- Anytime, anywhere 

You thought that I was weak, Boy, you're dead wrong 
So come on, everybody and sing this song 

Say -- Play that funky music Say, go white boy, go white boy go 
play that funky music Go white boy, go white boy, go 
Lay down and boogie and play that funky music till you die. 

Play that funky music Come on, Come on, let me hear 
Play that funky music white boy you say it, say it 
Play that funky music A little louder now 
Play that funky music, white boy Come on, Come on, Come on 
Play that funky music 



Encrypt decrypt chain was successfully built. 
```

### [Challenge 11](#challenge-11)

Developing an algorithm to detect the use of ECB or CBC mode is simple. In ECB mode we expect the exact same block to go to the same ciphertext output, while in CBC under different IVs we expect the ciphertext blocks to be different (its 2^-64 unlikely to get a collision), developing such an algorithm is trivial from this observation. 

Expected output: 
```python
Experiments: 1000. Successful: 1000
```

### [Challenge 12](#challenge-12)

This challenge gives us our first modern cryptanalysis challenge, in which we do a Byte-at-a-time ECB decryption. The challange teaches us how to carry out a full attack from start to finish. In the challange we have an Oracle (A Complicated way of saying we have a function which described an interaction with the encryption/decryption algorithm) where we can input a string of our own which will be concatenated by an unknown string to the user and than encrypted using AES-ECB mode, or in a more formal languge: AES-128-ECB(your-string || unknown-string, random-key) which we call from now on O('your-string').

1. We start by figuring out the block size of our encryption function. We start by calling the oracle in the following way Oracle(''), we get the current out length of the ciphertext, which we call initial length (n). Now we start querying the oracle in the following way Oracle('A'* i) we search for the first value of i for which the length of the cipher text changes, we call this value current length (m). By subtracting m-m we get the block size of the cipher.
2. Now we detect the mode of operation, as we have done in Challenge 11 (we input constant '0'* 128 so we will find repeating blocks).
3. Finally we get into constructing our query method, we will look at the simple case of zero known bytes as it is easy to generalise the procedure from here. Lets query the Oracle using the following method O('A'* ((blockSize-1) % blockSize)) (adding lenDecryptedText generalizes the method), we get that the first byte of the unknown string eneters a block of (blockSize-1) known bytes. We can exploit this by taking this resulting cipher text and define an oracle O('A'* ((blockSize-1) % blockSize) + i) such that we go over 256 possible values for i, and when we find i such that the new ciphertext equals the previous ciphertext we have hit jackpot. This procdure can be generalized to any length we want, and we have recovered the unknown string in linear time.

Expected output: 
```python
What we expect to get at the end: 
 
Rollin' in my 5.0
With my rag-top down so my hair can blow
The girlies on standby waving just to say hi
Did you stop? No, I just drove by




Analysing cipher: 

Detected block size of: 16

Detected mode of operation: ECB

Iteration: 1. b'R' 

Iteration: 2. b'Ro' 

Iteration: 3. b'Rol' 

Iteration: 4. b'Roll' 

Iteration: 5. b'Rolli' 

Iteration: 6. b'Rollin' 

Iteration: 7. b"Rollin'" 

Iteration: 8. b"Rollin' " 

Iteration: 9. b"Rollin' i" 

Iteration: 10. b"Rollin' in" 

Iteration: 11. b"Rollin' in " 

Iteration: 12. b"Rollin' in m" 

Iteration: 13. b"Rollin' in my" 

Iteration: 14. b"Rollin' in my " 

Iteration: 15. b"Rollin' in my 5" 

Iteration: 16. b"Rollin' in my 5." 

Iteration: 17. b"Rollin' in my 5.0" 

Iteration: 18. b"Rollin' in my 5.0\n" 

Iteration: 19. b"Rollin' in my 5.0\nW" 

Iteration: 20. b"Rollin' in my 5.0\nWi" 

Iteration: 21. b"Rollin' in my 5.0\nWit" 

Iteration: 22. b"Rollin' in my 5.0\nWith" 

Iteration: 23. b"Rollin' in my 5.0\nWith " 

Iteration: 24. b"Rollin' in my 5.0\nWith m" 

Iteration: 25. b"Rollin' in my 5.0\nWith my" 

Iteration: 26. b"Rollin' in my 5.0\nWith my " 

Iteration: 27. b"Rollin' in my 5.0\nWith my r" 

Iteration: 28. b"Rollin' in my 5.0\nWith my ra" 

Iteration: 29. b"Rollin' in my 5.0\nWith my rag" 

Iteration: 30. b"Rollin' in my 5.0\nWith my rag-" 

Iteration: 31. b"Rollin' in my 5.0\nWith my rag-t" 

Iteration: 32. b"Rollin' in my 5.0\nWith my rag-to" 

Iteration: 33. b"Rollin' in my 5.0\nWith my rag-top" 

Iteration: 34. b"Rollin' in my 5.0\nWith my rag-top " 

Iteration: 35. b"Rollin' in my 5.0\nWith my rag-top d" 

Iteration: 36. b"Rollin' in my 5.0\nWith my rag-top do" 

Iteration: 37. b"Rollin' in my 5.0\nWith my rag-top dow" 

Iteration: 38. b"Rollin' in my 5.0\nWith my rag-top down" 

Iteration: 39. b"Rollin' in my 5.0\nWith my rag-top down " 

Iteration: 40. b"Rollin' in my 5.0\nWith my rag-top down s" 

Iteration: 41. b"Rollin' in my 5.0\nWith my rag-top down so" 

Iteration: 42. b"Rollin' in my 5.0\nWith my rag-top down so " 

Iteration: 43. b"Rollin' in my 5.0\nWith my rag-top down so m" 

Iteration: 44. b"Rollin' in my 5.0\nWith my rag-top down so my" 

Iteration: 45. b"Rollin' in my 5.0\nWith my rag-top down so my " 

Iteration: 46. b"Rollin' in my 5.0\nWith my rag-top down so my h" 

Iteration: 47. b"Rollin' in my 5.0\nWith my rag-top down so my ha" 

Iteration: 48. b"Rollin' in my 5.0\nWith my rag-top down so my hai" 

Iteration: 49. b"Rollin' in my 5.0\nWith my rag-top down so my hair" 

Iteration: 50. b"Rollin' in my 5.0\nWith my rag-top down so my hair " 

Iteration: 51. b"Rollin' in my 5.0\nWith my rag-top down so my hair c" 

Iteration: 52. b"Rollin' in my 5.0\nWith my rag-top down so my hair ca" 

Iteration: 53. b"Rollin' in my 5.0\nWith my rag-top down so my hair can" 

Iteration: 54. b"Rollin' in my 5.0\nWith my rag-top down so my hair can " 

Iteration: 55. b"Rollin' in my 5.0\nWith my rag-top down so my hair can b" 

Iteration: 56. b"Rollin' in my 5.0\nWith my rag-top down so my hair can bl" 

Iteration: 57. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blo" 

Iteration: 58. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow" 

Iteration: 59. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\n" 

Iteration: 60. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nT" 

Iteration: 61. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nTh" 

Iteration: 62. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe" 

Iteration: 63. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe " 

Iteration: 64. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe g" 

Iteration: 65. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe gi" 

Iteration: 66. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe gir" 

Iteration: 67. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girl" 

Iteration: 68. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girli" 

Iteration: 69. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlie" 

Iteration: 70. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies" 

Iteration: 71. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies " 

Iteration: 72. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies o" 

Iteration: 73. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on" 

Iteration: 74. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on " 

Iteration: 75. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on s" 

Iteration: 76. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on st" 

Iteration: 77. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on sta" 

Iteration: 78. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on stan" 

Iteration: 79. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on stand" 

Iteration: 80. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standb" 

Iteration: 81. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby" 

Iteration: 82. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby " 

Iteration: 83. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby w" 

Iteration: 84. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby wa" 

Iteration: 85. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby wav" 

Iteration: 86. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby wavi" 

Iteration: 87. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby wavin" 

Iteration: 88. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving" 

Iteration: 89. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving " 

Iteration: 90. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving j" 

Iteration: 91. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving ju" 

Iteration: 92. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving jus" 

Iteration: 93. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just" 

Iteration: 94. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just " 

Iteration: 95. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just t" 

Iteration: 96. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to" 

Iteration: 97. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to " 

Iteration: 98. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to s" 

Iteration: 99. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to sa" 

Iteration: 100. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say" 

Iteration: 101. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say " 

Iteration: 102. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say h" 

Iteration: 103. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi" 

Iteration: 104. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\n" 

Iteration: 105. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nD" 

Iteration: 106. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDi" 

Iteration: 107. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid" 

Iteration: 108. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid " 

Iteration: 109. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid y" 

Iteration: 110. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid yo" 

Iteration: 111. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you" 

Iteration: 112. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you " 

Iteration: 113. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you s" 

Iteration: 114. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you st" 

Iteration: 115. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you sto" 

Iteration: 116. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop" 

Iteration: 117. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop?" 

Iteration: 118. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? " 

Iteration: 119. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? N" 

Iteration: 120. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No" 

Iteration: 121. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No," 

Iteration: 122. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, " 

Iteration: 123. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I" 

Iteration: 124. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I " 

Iteration: 125. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I j" 

Iteration: 126. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I ju" 

Iteration: 127. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I jus" 

Iteration: 128. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just" 

Iteration: 129. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just " 

Iteration: 130. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just d" 

Iteration: 131. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just dr" 

Iteration: 132. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just dro" 

Iteration: 133. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drov" 

Iteration: 134. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove" 

Iteration: 135. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove " 

Iteration: 136. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove b" 

Iteration: 137. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by" 

Iteration: 138. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n" 

Iteration: 139. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n\x01" 

Iteration: 140. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n\x01" 

Iteration: 141. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n\x01" 

Iteration: 142. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n\x01" 

Iteration: 143. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n\x01" 

Iteration: 144. b"Rollin' in my 5.0\nWith my rag-top down so my hair can blow\nThe girlies on standby waving just to say hi\nDid you stop? No, I just drove by\n\x01" 

Decrypted text: Rollin' in my 5.0
With my rag-top down so my hair can blow
The girlies on standby waving just to say hi
Did you stop? No, I just drove by
```

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

## Set 6: RSA and DSA

### [Challenge 41](#challenge-41)

### [Challenge 42](#challenge-42)

### [Challenge 43](#challenge-43)

### [Challenge 44](#challenge-44)

### [Challenge 45](#challenge-45)

### [Challenge 46](#challenge-46)

### [Challenge 47](#challenge-47)

### [Challenge 48](#challenge-48)

## Set 7: Hashes

### [Challenge 49](#challenge-49)

### [Challenge 50](#challenge-50)

### [Challenge 51](#challenge-51)

### [Challenge 52](#challenge-52)

### [Challenge 53](#challenge-53)

### [Challenge 54](#challenge-54)

### [Challenge 55](#challenge-55)

### [Challenge 56](#challenge-56)

## Set 8: Abstract Algebra

### [Challenge 57](#challenge-57)

### [Challenge 58](#challenge-58)

### [Challenge 59](#challenge-59)

### [Challenge 60](#challenge-60)

### [Challenge 61](#challenge-61)

### [Challenge 62](#challenge-62)

### [Challenge 63](#challenge-63)

### [Challenge 64](#challenge-64)

### [Challenge 65](#challenge-65)

### [Challenge 66](#challenge-66)


# License

Everything in this repository is distributed under the terms of the MIT License. See file "LICENSE" for further reference.



