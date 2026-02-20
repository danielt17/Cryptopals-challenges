# Challenge Index

This index maps each challenge to its scripts, writeup, and data files.
Use `python scripts/run_challenge.py <num>` to run with the default sequence.

## Set 1: Basics

| Challenge | Title | Code | Writeup | Data | Run |
| --- | --- | --- | --- | --- | --- |
| 1 | Convert hex to base64 | src/sets/set_01_basics/challenge_01_hex_to_base64/hex_to_base64.py | src/sets/set_01_basics/challenge_01_hex_to_base64/writeup.md | - | python scripts/run_challenge.py 1 |
| 2 | Fixed XOR | src/sets/set_01_basics/challenge_02_fixed_xor/fixed_xor.py | src/sets/set_01_basics/challenge_02_fixed_xor/writeup.md | - | python scripts/run_challenge.py 2 |
| 3 | Single-byte XOR cipher | src/sets/set_01_basics/challenge_03_single_byte_xor_cipher/single_byte_xor_cipher.py | src/sets/set_01_basics/challenge_03_single_byte_xor_cipher/writeup.md | - | python scripts/run_challenge.py 3 |
| 4 | Detect single-character XOR | src/sets/set_01_basics/challenge_04_detect_single_character_xor/detect_single_character_xor.py | src/sets/set_01_basics/challenge_04_detect_single_character_xor/writeup.md | src/sets/set_01_basics/challenge_04_detect_single_character_xor/14.txt | python scripts/run_challenge.py 4 |
| 5 | Implement repeating-key XOR | src/sets/set_01_basics/challenge_05_repeating_key_xor/repeating_key_xor.py | src/sets/set_01_basics/challenge_05_repeating_key_xor/writeup.md | - | python scripts/run_challenge.py 5 |
| 6 | Break repeating-key XOR | src/sets/set_01_basics/challenge_06_break_repeating_key_xor/break_repeating_key_xor.py | src/sets/set_01_basics/challenge_06_break_repeating_key_xor/writeup.md | src/sets/set_01_basics/challenge_06_break_repeating_key_xor/16.txt | python scripts/run_challenge.py 6 |
| 7 | AES in ECB mode | src/sets/set_01_basics/challenge_07_aes_ecb_mode/aes_ecb_mode.py | src/sets/set_01_basics/challenge_07_aes_ecb_mode/writeup.md | src/sets/set_01_basics/challenge_07_aes_ecb_mode/17.txt | python scripts/run_challenge.py 7 |
| 8 | Detect AES in ECB mode | src/sets/set_01_basics/challenge_08_detect_aes_ecb_mode/detect_aes_ecb_mode.py | src/sets/set_01_basics/challenge_08_detect_aes_ecb_mode/writeup.md | src/sets/set_01_basics/challenge_08_detect_aes_ecb_mode/18.txt | python scripts/run_challenge.py 8 |

## Set 2: Block crypto

| Challenge | Title | Code | Writeup | Data | Run |
| --- | --- | --- | --- | --- | --- |
| 9 | Implement PKCS#7 padding | src/sets/set_02_block_crypto/challenge_09_pkcs7_padding/pkcs7_padding.py | src/sets/set_02_block_crypto/challenge_09_pkcs7_padding/writeup.md | - | python scripts/run_challenge.py 9 |
| 10 | Implement CBC mode | src/sets/set_02_block_crypto/challenge_10_cbc_mode/cbc_mode.py | src/sets/set_02_block_crypto/challenge_10_cbc_mode/writeup.md | src/sets/set_02_block_crypto/challenge_10_cbc_mode/22.txt | python scripts/run_challenge.py 10 |
| 11 | An ECB/CBC detection oracle | src/sets/set_02_block_crypto/challenge_11_ecb_cbc_detection_oracle/ecb_cbc_detection_oracle.py | src/sets/set_02_block_crypto/challenge_11_ecb_cbc_detection_oracle/writeup.md | - | python scripts/run_challenge.py 11 |
| 12 | Byte-at-a-time ECB decryption (simple) | src/sets/set_02_block_crypto/challenge_12_byte_at_a_time_ecb_simple/byte_at_a_time_ecb_simple.py | src/sets/set_02_block_crypto/challenge_12_byte_at_a_time_ecb_simple/writeup.md | - | python scripts/run_challenge.py 12 |
| 13 | ECB cut-and-paste | src/sets/set_02_block_crypto/challenge_13_ecb_cut_and_paste/ecb_cut_and_paste.py | src/sets/set_02_block_crypto/challenge_13_ecb_cut_and_paste/writeup.md | - | python scripts/run_challenge.py 13 |
| 14 | Byte-at-a-time ECB decryption (harder) | src/sets/set_02_block_crypto/challenge_14_byte_at_a_time_ecb_harder/byte_at_a_time_ecb_harder.py | src/sets/set_02_block_crypto/challenge_14_byte_at_a_time_ecb_harder/writeup.md | - | python scripts/run_challenge.py 14 |
| 15 | PKCS#7 padding validation | src/sets/set_02_block_crypto/challenge_15_pkcs7_padding_validation/pkcs7_padding_validation.py | src/sets/set_02_block_crypto/challenge_15_pkcs7_padding_validation/writeup.md | - | python scripts/run_challenge.py 15 |
| 16 | CBC bitflipping attacks | src/sets/set_02_block_crypto/challenge_16_cbc_bitflipping/cbc_bitflipping.py | src/sets/set_02_block_crypto/challenge_16_cbc_bitflipping/writeup.md | - | python scripts/run_challenge.py 16 |

## Set 3: Block and stream crypto

| Challenge | Title | Code | Writeup | Data | Run |
| --- | --- | --- | --- | --- | --- |
| 17 | The CBC padding oracle | src/sets/set_03_block_and_stream_crypto/challenge_17_cbc_padding_oracle/cbc_padding_oracle.py | src/sets/set_03_block_and_stream_crypto/challenge_17_cbc_padding_oracle/writeup.md | - | python scripts/run_challenge.py 17 |
| 18 | Implement CTR mode | src/sets/set_03_block_and_stream_crypto/challenge_18_aes_ctr_mode/aes_ctr_mode.py | src/sets/set_03_block_and_stream_crypto/challenge_18_aes_ctr_mode/writeup.md | - | python scripts/run_challenge.py 18 |
| 19 | Break fixed-nonce CTR mode using substitutions | src/sets/set_03_block_and_stream_crypto/challenge_19_break_fixed_nonce_ctr/break_fixed_nonce_ctr.py | src/sets/set_03_block_and_stream_crypto/challenge_19_break_fixed_nonce_ctr/writeup.md | src/sets/set_03_block_and_stream_crypto/challenge_19_break_fixed_nonce_ctr/33.txt | python scripts/run_challenge.py 19 |
| 20 | Break fixed-nonce CTR statistically | src/sets/set_03_block_and_stream_crypto/challenge_20_break_fixed_nonce_ctr_statistical/break_fixed_nonce_ctr_statistical.py | src/sets/set_03_block_and_stream_crypto/challenge_20_break_fixed_nonce_ctr_statistical/writeup.md | src/sets/set_03_block_and_stream_crypto/challenge_20_break_fixed_nonce_ctr_statistical/34.txt | python scripts/run_challenge.py 20 |
| 21 | Implement the MT19937 Mersenne Twister RNG | src/sets/set_03_block_and_stream_crypto/challenge_21_mt19937_rng/mt19937_rng.py | src/sets/set_03_block_and_stream_crypto/challenge_21_mt19937_rng/writeup.md | - | python scripts/run_challenge.py 21 |
| 22 | Crack an MT19937 seed | src/sets/set_03_block_and_stream_crypto/challenge_22_crack_mt19937_seed/crack_mt19937_seed.py | src/sets/set_03_block_and_stream_crypto/challenge_22_crack_mt19937_seed/writeup.md | - | python scripts/run_challenge.py 22 |
| 23 | Clone an MT19937 RNG from its output | src/sets/set_03_block_and_stream_crypto/challenge_23_clone_mt19937/clone_mt19937.py | src/sets/set_03_block_and_stream_crypto/challenge_23_clone_mt19937/writeup.md | - | python scripts/run_challenge.py 23 |
| 24 | Create the MT19937 stream cipher and break it | src/sets/set_03_block_and_stream_crypto/challenge_24_mt19937_stream_cipher/mt19937_stream_cipher.py | src/sets/set_03_block_and_stream_crypto/challenge_24_mt19937_stream_cipher/writeup.md | - | python scripts/run_challenge.py 24 |

## Set 4: Stream crypto and randomness

| Challenge | Title | Code | Writeup | Data | Run |
| --- | --- | --- | --- | --- | --- |
| 25 | Break random-access read/write AES CTR | src/sets/set_04_stream_crypto_and_randomness/challenge_25_break_random_access_aes_ctr/break_random_access_aes_ctr.py | src/sets/set_04_stream_crypto_and_randomness/challenge_25_break_random_access_aes_ctr/writeup.md | src/sets/set_04_stream_crypto_and_randomness/challenge_25_break_random_access_aes_ctr/41.txt | python scripts/run_challenge.py 25 |
| 26 | CTR bitflipping | src/sets/set_04_stream_crypto_and_randomness/challenge_26_ctr_bitflipping/ctr_bitflipping.py | src/sets/set_04_stream_crypto_and_randomness/challenge_26_ctr_bitflipping/writeup.md | - | python scripts/run_challenge.py 26 |
| 27 | Recover the key from CBC with IV=Key | src/sets/set_04_stream_crypto_and_randomness/challenge_27_recover_key_from_iv_equal_key/recover_key_from_iv_equal_key.py | src/sets/set_04_stream_crypto_and_randomness/challenge_27_recover_key_from_iv_equal_key/writeup.md | - | python scripts/run_challenge.py 27 |
| 28 | Implement a SHA-1 keyed MAC | src/sets/set_04_stream_crypto_and_randomness/challenge_28_sha1_keyed_mac/sha1_keyed_mac.py | src/sets/set_04_stream_crypto_and_randomness/challenge_28_sha1_keyed_mac/writeup.md | - | python scripts/run_challenge.py 28 |
| 29 | Break a SHA-1 keyed MAC using length extension | src/sets/set_04_stream_crypto_and_randomness/challenge_29_sha1_length_extension/sha1_length_extension.py | src/sets/set_04_stream_crypto_and_randomness/challenge_29_sha1_length_extension/writeup.md | - | python scripts/run_challenge.py 29 |
| 30 | Break an MD4 keyed MAC using length extension | src/sets/set_04_stream_crypto_and_randomness/challenge_30_md4_length_extension/md4_length_extension.py, src/sets/set_04_stream_crypto_and_randomness/challenge_30_md4_length_extension/md5_length_extension.py | src/sets/set_04_stream_crypto_and_randomness/challenge_30_md4_length_extension/writeup.md | - | auto: run md4_length_extension.py -> run md5_length_extension.py |
| 31 | Implement and break HMAC-SHA1 with an artificial timing leak | src/sets/set_04_stream_crypto_and_randomness/challenge_31_hmac_sha1_timing_leak_artificial/utils.py, src/sets/set_04_stream_crypto_and_randomness/challenge_31_hmac_sha1_timing_leak_artificial/server.py, src/sets/set_04_stream_crypto_and_randomness/challenge_31_hmac_sha1_timing_leak_artificial/attacker.py | src/sets/set_04_stream_crypto_and_randomness/challenge_31_hmac_sha1_timing_leak_artificial/writeup.md | - | auto: start server.py -> run attacker.py |
| 32 | Break HMAC-SHA1 with a slightly less artificial timing leak | src/sets/set_04_stream_crypto_and_randomness/challenge_32_hmac_sha1_timing_leak_less_artificial/server.py, src/sets/set_04_stream_crypto_and_randomness/challenge_32_hmac_sha1_timing_leak_less_artificial/attacker.py | src/sets/set_04_stream_crypto_and_randomness/challenge_32_hmac_sha1_timing_leak_less_artificial/writeup.md | - | auto: start server.py -> run attacker.py |

## Set 5: Diffie-Hellman and friends

| Challenge | Title | Code | Writeup | Data | Run |
| --- | --- | --- | --- | --- | --- |
| 33 | Implement Diffie-Hellman | src/sets/set_05_diffie_hellman_and_friends/challenge_33_diffie_hellman/diffie_hellman.py | src/sets/set_05_diffie_hellman_and_friends/challenge_33_diffie_hellman/writeup.md | - | python scripts/run_challenge.py 33 |
| 34 | MITM key-fixing attack on Diffie-Hellman with parameter injection | src/sets/set_05_diffie_hellman_and_friends/challenge_34_dh_mitm_key_fixing/server.py, src/sets/set_05_diffie_hellman_and_friends/challenge_34_dh_mitm_key_fixing/attacker.py, src/sets/set_05_diffie_hellman_and_friends/challenge_34_dh_mitm_key_fixing/client.py | src/sets/set_05_diffie_hellman_and_friends/challenge_34_dh_mitm_key_fixing/writeup.md | - | auto: start server.py -> start attacker.py -> run client.py |
| 35 | DH with negotiated groups, malicious g | src/sets/set_05_diffie_hellman_and_friends/challenge_35_dh_malicious_g/server.py, src/sets/set_05_diffie_hellman_and_friends/challenge_35_dh_malicious_g/attacker.py, src/sets/set_05_diffie_hellman_and_friends/challenge_35_dh_malicious_g/client.py | src/sets/set_05_diffie_hellman_and_friends/challenge_35_dh_malicious_g/writeup.md | - | auto: start server.py -> start attacker.py -> run client.py |
| 36 | Implement Secure Remote Password (SRP) | src/sets/set_05_diffie_hellman_and_friends/challenge_36_srp/server.py, src/sets/set_05_diffie_hellman_and_friends/challenge_36_srp/client.py, src/sets/set_05_diffie_hellman_and_friends/challenge_36_srp/utils.py | src/sets/set_05_diffie_hellman_and_friends/challenge_36_srp/writeup.md | - | auto: start server.py -> run client.py |
| 37 | Break SRP with a zero key | src/sets/set_05_diffie_hellman_and_friends/challenge_37_srp_zero_key/server.py, src/sets/set_05_diffie_hellman_and_friends/challenge_37_srp_zero_key/client_setup_then_attack.py | src/sets/set_05_diffie_hellman_and_friends/challenge_37_srp_zero_key/writeup.md | - | auto: start server.py -> run client_setup_then_attack.py |
| 38 | Offline dictionary attack on simplified SRP | src/sets/set_05_diffie_hellman_and_friends/challenge_38_srp_offline_dictionary/fake_server.py, src/sets/set_05_diffie_hellman_and_friends/challenge_38_srp_offline_dictionary/client.py, src/sets/set_05_diffie_hellman_and_friends/challenge_38_srp_offline_dictionary/server.py | src/sets/set_05_diffie_hellman_and_friends/challenge_38_srp_offline_dictionary/writeup.md | - | auto: start fake_server.py -> run client.py |
| 39 | Implement RSA | src/sets/set_05_diffie_hellman_and_friends/challenge_39_rsa_implementation/rsa_implementation.py | src/sets/set_05_diffie_hellman_and_friends/challenge_39_rsa_implementation/writeup.md | - | python scripts/run_challenge.py 39 |
| 40 | RSA broadcast attack (e=3) | src/sets/set_05_diffie_hellman_and_friends/challenge_40_rsa_broadcast_attack/rsa_broadcast_attack.py | src/sets/set_05_diffie_hellman_and_friends/challenge_40_rsa_broadcast_attack/writeup.md | - | python scripts/run_challenge.py 40 |

## Set 6: RSA and DSA

| Challenge | Title | Code | Writeup | Data | Run |
| --- | --- | --- | --- | --- | --- |
| 41 | Unpadded message recovery oracle | src/sets/set_06_rsa_and_dsa/challenge_41_unpadded_rsa_message_recovery/unpadded_rsa_message_recovery.py | src/sets/set_06_rsa_and_dsa/challenge_41_unpadded_rsa_message_recovery/writeup.md | - | python scripts/run_challenge.py 41 |
| 42 | Bleichenbacher's e=3 RSA signature forgery | src/sets/set_06_rsa_and_dsa/challenge_42_rsa_signature_forgery/rsa_signature_forgery.py | src/sets/set_06_rsa_and_dsa/challenge_42_rsa_signature_forgery/writeup.md | - | python scripts/run_challenge.py 42 |
| 43 | DSA key recovery from nonce | src/sets/set_06_rsa_and_dsa/challenge_43_dsa_key_recovery_from_nonce/dsa_key_recovery_from_nonce.py | src/sets/set_06_rsa_and_dsa/challenge_43_dsa_key_recovery_from_nonce/writeup.md | - | python scripts/run_challenge.py 43 |
| 44 | DSA nonce reuse | src/sets/set_06_rsa_and_dsa/challenge_44_dsa_nonce_reuse/dsa_nonce_reuse.py | src/sets/set_06_rsa_and_dsa/challenge_44_dsa_nonce_reuse/writeup.md | src/sets/set_06_rsa_and_dsa/challenge_44_dsa_nonce_reuse/64.txt | python scripts/run_challenge.py 44 |
| 45 | DSA parameter tampering | src/sets/set_06_rsa_and_dsa/challenge_45_dsa_parameter_tampering/dsa_parameter_tampering.py | src/sets/set_06_rsa_and_dsa/challenge_45_dsa_parameter_tampering/writeup.md | - | python scripts/run_challenge.py 45 |
| 46 | RSA parity oracle | src/sets/set_06_rsa_and_dsa/challenge_46_rsa_parity_oracle/rsa_parity_oracle.py | src/sets/set_06_rsa_and_dsa/challenge_46_rsa_parity_oracle/writeup.md | - | python scripts/run_challenge.py 46 |
| 47 | Bleichenbacher's PKCS 1.5 padding oracle | src/sets/set_06_rsa_and_dsa/challenge_47_pkcs1_v1_5_padding_oracle/pkcs1_v1_5_padding_oracle_rsa256.py, src/sets/set_06_rsa_and_dsa/challenge_47_pkcs1_v1_5_padding_oracle/pkcs1_v1_5_padding_oracle_rsa2048.py | src/sets/set_06_rsa_and_dsa/challenge_47_pkcs1_v1_5_padding_oracle/writeup.md | - | auto: run pkcs1_v1_5_padding_oracle_rsa256.py -> run pkcs1_v1_5_padding_oracle_rsa2048.py |
| 48 | Bleichenbacher 98 attack (TLS) | src/sets/set_06_rsa_and_dsa/challenge_48_bleichenbacher_98/server.py, src/sets/set_06_rsa_and_dsa/challenge_48_bleichenbacher_98/attacker.py, src/sets/set_06_rsa_and_dsa/challenge_48_bleichenbacher_98/client.py | src/sets/set_06_rsa_and_dsa/challenge_48_bleichenbacher_98/writeup.md | - | auto: start server.py -> start attacker.py -> run client.py |

## Set 7: Hashes

| Challenge | Title | Code | Writeup | Data | Run |
| --- | --- | --- | --- | --- | --- |
| 49 | CBC-MAC message forgery | src/sets/set_07_hashes/challenge_49_cbc_mac_message_forgery/iv_control.py, src/sets/set_07_hashes/challenge_49_cbc_mac_message_forgery/no_iv_control.py | src/sets/set_07_hashes/challenge_49_cbc_mac_message_forgery/writeup.md | - | auto: run iv_control.py -> run no_iv_control.py |
| 50 | Hashing with CBC-MAC | src/sets/set_07_hashes/challenge_50_hashing_with_cbc_mac/hashing_with_cbc_mac.py | src/sets/set_07_hashes/challenge_50_hashing_with_cbc_mac/writeup.md | - | python scripts/run_challenge.py 50 |
| 51 | Compression ratio side-channel attacks | src/sets/set_07_hashes/challenge_51_compression_ratio_side_channel/compression_ratio_side_channel.py | src/sets/set_07_hashes/challenge_51_compression_ratio_side_channel/writeup.md | - | python scripts/run_challenge.py 51 |
| 52 | Iterated hash function multicollisions | src/sets/set_07_hashes/challenge_52_iterated_hash_multicollisions/iterated_hash_multicollisions.py | src/sets/set_07_hashes/challenge_52_iterated_hash_multicollisions/writeup.md | - | python scripts/run_challenge.py 52 |
| 53 | Kelsey and Schneier's expandable messages | src/sets/set_07_hashes/challenge_53_expandable_messages/expandable_messages.py | src/sets/set_07_hashes/challenge_53_expandable_messages/writeup.md | - | python scripts/run_challenge.py 53 |
| 54 | Kelsey and Kohno's Nostradamus attack | src/sets/set_07_hashes/challenge_54_nostradamus_attack/nostradamus_attack.py | src/sets/set_07_hashes/challenge_54_nostradamus_attack/writeup.md | - | python scripts/run_challenge.py 54 |
| 55 | MD4 collisions | - | src/sets/set_07_hashes/challenge_55_md4_collisions/writeup.md | - | - |
| 56 | RC4 single-byte biases | - | src/sets/set_07_hashes/challenge_56_rc4_single_byte_biases/writeup.md | - | - |

## Set 8: Abstract Algebra

| Challenge | Title | Code | Writeup | Data | Run |
| --- | --- | --- | --- | --- | --- |
| 57 | Diffie-Hellman Revisited: Subgroup-Confinement Attacks | - | src/sets/set_08_abstract_algebra/challenge_57_diffie_hellman_revisited_subgroup_confinement/writeup.md | - | - |
| 58 | Pollard's Method for Catching Kangaroos | - | src/sets/set_08_abstract_algebra/challenge_58_pollards_method_catching_kangaroos/writeup.md | - | - |
| 59 | Elliptic Curve Diffie-Hellman and Invalid-Curve Attacks | - | src/sets/set_08_abstract_algebra/challenge_59_ecdh_invalid_curve_attacks/writeup.md | - | - |
| 60 | Single-Coordinate Ladders and Insecure Twists | - | src/sets/set_08_abstract_algebra/challenge_60_single_coordinate_ladders_insecure_twists/writeup.md | - | - |
| 61 | Duplicate-Signature Key Selection in ECDSA (and RSA) | - | src/sets/set_08_abstract_algebra/challenge_61_duplicate_signature_key_selection/writeup.md | - | - |
| 62 | Key-Recovery Attacks on ECDSA with Biased Nonces | - | src/sets/set_08_abstract_algebra/challenge_62_ecdsa_biased_nonce_key_recovery/writeup.md | - | - |
| 63 | Key-Recovery Attacks on GCM with Repeated Nonces | - | src/sets/set_08_abstract_algebra/challenge_63_gcm_repeated_nonces_key_recovery/writeup.md | - | - |
| 64 | Key-Recovery Attacks on GCM with a Truncated MAC | - | src/sets/set_08_abstract_algebra/challenge_64_gcm_truncated_mac_key_recovery/writeup.md | - | - |
| 65 | Truncated-MAC GCM Revisited: Improving the Key-Recovery Attack | - | src/sets/set_08_abstract_algebra/challenge_65_gcm_truncated_mac_improved_key_recovery/writeup.md | - | - |
| 66 | Exploiting Implementation Errors in Diffie-Hellman | - | src/sets/set_08_abstract_algebra/challenge_66_dh_implementation_errors/writeup.md | - | - |

