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

```python
Expected output: 

solved
```

### [Challenge 2](#challenge-2)

Implementation of fixed <a href="https://en.wikipedia.org/wiki/Exclusive_or">xor</a> between two buffers.

Expected output: 

Success

### [Challenge 3](#challenge-3)

The solution uses a brute force approach, trying every possible single byte key, choosing the one which results in the highest english score.
Inorder to calculate the english score we use the <a href="https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html">distribution</a>  of letters in the english language.

Expected output: 

Decyphered text with key: 88 and score: 2.2641049 

b"Cooking MC's like a pound of bacon"

### [Challenge 4](#challenge-4)

Using the same approach used in [challenge 3](#challenge-3), where now we use the english score to find the most likely sequence to be encrypted by a single byte xor cipher, therefore both detecting and decrypting using the english score metric.

Expected output: 

Decyphered text with key: 53 and score: 2.0881317999999998 Cur line: 170 

b'Now that the party is jumping\n'

### [Challenge 5](#challenge-5)

### [Challenge 6](#challenge-6)

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



