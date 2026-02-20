# Cryptopals Challenges (Python)

Refactored and organized solutions for the Cryptopals crypto challenges.

## Project layout

- src/sets/ : per-set, per-challenge folders
  - Each challenge folder contains its script(s), data files, and writeup.md
- docs/challenges.md : index of challenges, paths, and run order
- scripts/run_challenge.py : launcher that runs challenges by number
- scripts/verify_project.py : structural and syntax checks
- requirements.txt : Python dependencies
- LICENSE.md

## Setup

Python 3.9+ recommended.

Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

List challenges:
```powershell
python scripts/run_challenge.py --list
```

Run a challenge by number:
```powershell
python scripts/run_challenge.py 1
python scripts/run_challenge.py 34
```

Run a single script within a multi-script challenge:
```powershell
python scripts/run_challenge.py 34 --script server.py
```

The runner launches multi-process challenges in the correct order (server -> attacker -> client where applicable). Some scripts bind to localhost ports (often 8820/8821), so run them one at a time.

If you want to run a script directly, set `PYTHONPATH=src` or use `python -m` with the module path.

## Writeups

Each challenge folder includes a `writeup.md` following a consistent scheme (Goal, Cryptographic Insight, Method, Implementation Notes, Verification).
The master index is in `docs/challenges.md`.

## Challenge Table

| Challenge | Cryptopals Link | Code | Writeup |
| --- | --- | --- | --- |
| 1 | [Challenge 1](https://cryptopals.com/sets/1/challenges/1) | [hex_to_base64.py](src/sets/set_01_basics/challenge_01_hex_to_base64/hex_to_base64.py) | [writeup](src/sets/set_01_basics/challenge_01_hex_to_base64/writeup.md) |
| 2 | [Challenge 2](https://cryptopals.com/sets/1/challenges/2) | [fixed_xor.py](src/sets/set_01_basics/challenge_02_fixed_xor/fixed_xor.py) | [writeup](src/sets/set_01_basics/challenge_02_fixed_xor/writeup.md) |
| 3 | [Challenge 3](https://cryptopals.com/sets/1/challenges/3) | [single_byte_xor_cipher.py](src/sets/set_01_basics/challenge_03_single_byte_xor_cipher/single_byte_xor_cipher.py) | [writeup](src/sets/set_01_basics/challenge_03_single_byte_xor_cipher/writeup.md) |
| 4 | [Challenge 4](https://cryptopals.com/sets/1/challenges/4) | [detect_single_character_xor.py](src/sets/set_01_basics/challenge_04_detect_single_character_xor/detect_single_character_xor.py) | [writeup](src/sets/set_01_basics/challenge_04_detect_single_character_xor/writeup.md) |
| 5 | [Challenge 5](https://cryptopals.com/sets/1/challenges/5) | [repeating_key_xor.py](src/sets/set_01_basics/challenge_05_repeating_key_xor/repeating_key_xor.py) | [writeup](src/sets/set_01_basics/challenge_05_repeating_key_xor/writeup.md) |
| 6 | [Challenge 6](https://cryptopals.com/sets/1/challenges/6) | [break_repeating_key_xor.py](src/sets/set_01_basics/challenge_06_break_repeating_key_xor/break_repeating_key_xor.py) | [writeup](src/sets/set_01_basics/challenge_06_break_repeating_key_xor/writeup.md) |
| 7 | [Challenge 7](https://cryptopals.com/sets/1/challenges/7) | [aes_ecb_mode.py](src/sets/set_01_basics/challenge_07_aes_ecb_mode/aes_ecb_mode.py) | [writeup](src/sets/set_01_basics/challenge_07_aes_ecb_mode/writeup.md) |
| 8 | [Challenge 8](https://cryptopals.com/sets/1/challenges/8) | [detect_aes_ecb_mode.py](src/sets/set_01_basics/challenge_08_detect_aes_ecb_mode/detect_aes_ecb_mode.py) | [writeup](src/sets/set_01_basics/challenge_08_detect_aes_ecb_mode/writeup.md) |
| 9 | [Challenge 9](https://cryptopals.com/sets/2/challenges/9) | [pkcs7_padding.py](src/sets/set_02_block_crypto/challenge_09_pkcs7_padding/pkcs7_padding.py) | [writeup](src/sets/set_02_block_crypto/challenge_09_pkcs7_padding/writeup.md) |
| 10 | [Challenge 10](https://cryptopals.com/sets/2/challenges/10) | [cbc_mode.py](src/sets/set_02_block_crypto/challenge_10_cbc_mode/cbc_mode.py) | [writeup](src/sets/set_02_block_crypto/challenge_10_cbc_mode/writeup.md) |
| 11 | [Challenge 11](https://cryptopals.com/sets/2/challenges/11) | [ecb_cbc_detection_oracle.py](src/sets/set_02_block_crypto/challenge_11_ecb_cbc_detection_oracle/ecb_cbc_detection_oracle.py) | [writeup](src/sets/set_02_block_crypto/challenge_11_ecb_cbc_detection_oracle/writeup.md) |
| 12 | [Challenge 12](https://cryptopals.com/sets/2/challenges/12) | [byte_at_a_time_ecb_simple.py](src/sets/set_02_block_crypto/challenge_12_byte_at_a_time_ecb_simple/byte_at_a_time_ecb_simple.py) | [writeup](src/sets/set_02_block_crypto/challenge_12_byte_at_a_time_ecb_simple/writeup.md) |
| 13 | [Challenge 13](https://cryptopals.com/sets/2/challenges/13) | [ecb_cut_and_paste.py](src/sets/set_02_block_crypto/challenge_13_ecb_cut_and_paste/ecb_cut_and_paste.py) | [writeup](src/sets/set_02_block_crypto/challenge_13_ecb_cut_and_paste/writeup.md) |
| 14 | [Challenge 14](https://cryptopals.com/sets/2/challenges/14) | [byte_at_a_time_ecb_harder.py](src/sets/set_02_block_crypto/challenge_14_byte_at_a_time_ecb_harder/byte_at_a_time_ecb_harder.py) | [writeup](src/sets/set_02_block_crypto/challenge_14_byte_at_a_time_ecb_harder/writeup.md) |
| 15 | [Challenge 15](https://cryptopals.com/sets/2/challenges/15) | [pkcs7_padding_validation.py](src/sets/set_02_block_crypto/challenge_15_pkcs7_padding_validation/pkcs7_padding_validation.py) | [writeup](src/sets/set_02_block_crypto/challenge_15_pkcs7_padding_validation/writeup.md) |
| 16 | [Challenge 16](https://cryptopals.com/sets/2/challenges/16) | [cbc_bitflipping.py](src/sets/set_02_block_crypto/challenge_16_cbc_bitflipping/cbc_bitflipping.py) | [writeup](src/sets/set_02_block_crypto/challenge_16_cbc_bitflipping/writeup.md) |
| 17 | [Challenge 17](https://cryptopals.com/sets/3/challenges/17) | [cbc_padding_oracle.py](src/sets/set_03_block_and_stream_crypto/challenge_17_cbc_padding_oracle/cbc_padding_oracle.py) | [writeup](src/sets/set_03_block_and_stream_crypto/challenge_17_cbc_padding_oracle/writeup.md) |
| 18 | [Challenge 18](https://cryptopals.com/sets/3/challenges/18) | [aes_ctr_mode.py](src/sets/set_03_block_and_stream_crypto/challenge_18_aes_ctr_mode/aes_ctr_mode.py) | [writeup](src/sets/set_03_block_and_stream_crypto/challenge_18_aes_ctr_mode/writeup.md) |
| 19 | [Challenge 19](https://cryptopals.com/sets/3/challenges/19) | [break_fixed_nonce_ctr.py](src/sets/set_03_block_and_stream_crypto/challenge_19_break_fixed_nonce_ctr/break_fixed_nonce_ctr.py) | [writeup](src/sets/set_03_block_and_stream_crypto/challenge_19_break_fixed_nonce_ctr/writeup.md) |
| 20 | [Challenge 20](https://cryptopals.com/sets/3/challenges/20) | [break_fixed_nonce_ctr_statistical.py](src/sets/set_03_block_and_stream_crypto/challenge_20_break_fixed_nonce_ctr_statistical/break_fixed_nonce_ctr_statistical.py) | [writeup](src/sets/set_03_block_and_stream_crypto/challenge_20_break_fixed_nonce_ctr_statistical/writeup.md) |
| 21 | [Challenge 21](https://cryptopals.com/sets/3/challenges/21) | [mt19937_rng.py](src/sets/set_03_block_and_stream_crypto/challenge_21_mt19937_rng/mt19937_rng.py) | [writeup](src/sets/set_03_block_and_stream_crypto/challenge_21_mt19937_rng/writeup.md) |
| 22 | [Challenge 22](https://cryptopals.com/sets/3/challenges/22) | [crack_mt19937_seed.py](src/sets/set_03_block_and_stream_crypto/challenge_22_crack_mt19937_seed/crack_mt19937_seed.py) | [writeup](src/sets/set_03_block_and_stream_crypto/challenge_22_crack_mt19937_seed/writeup.md) |
| 23 | [Challenge 23](https://cryptopals.com/sets/3/challenges/23) | [clone_mt19937.py](src/sets/set_03_block_and_stream_crypto/challenge_23_clone_mt19937/clone_mt19937.py) | [writeup](src/sets/set_03_block_and_stream_crypto/challenge_23_clone_mt19937/writeup.md) |
| 24 | [Challenge 24](https://cryptopals.com/sets/3/challenges/24) | [mt19937_stream_cipher.py](src/sets/set_03_block_and_stream_crypto/challenge_24_mt19937_stream_cipher/mt19937_stream_cipher.py) | [writeup](src/sets/set_03_block_and_stream_crypto/challenge_24_mt19937_stream_cipher/writeup.md) |
| 25 | [Challenge 25](https://cryptopals.com/sets/4/challenges/25) | [break_random_access_aes_ctr.py](src/sets/set_04_stream_crypto_and_randomness/challenge_25_break_random_access_aes_ctr/break_random_access_aes_ctr.py) | [writeup](src/sets/set_04_stream_crypto_and_randomness/challenge_25_break_random_access_aes_ctr/writeup.md) |
| 26 | [Challenge 26](https://cryptopals.com/sets/4/challenges/26) | [ctr_bitflipping.py](src/sets/set_04_stream_crypto_and_randomness/challenge_26_ctr_bitflipping/ctr_bitflipping.py) | [writeup](src/sets/set_04_stream_crypto_and_randomness/challenge_26_ctr_bitflipping/writeup.md) |
| 27 | [Challenge 27](https://cryptopals.com/sets/4/challenges/27) | [recover_key_from_iv_equal_key.py](src/sets/set_04_stream_crypto_and_randomness/challenge_27_recover_key_from_iv_equal_key/recover_key_from_iv_equal_key.py) | [writeup](src/sets/set_04_stream_crypto_and_randomness/challenge_27_recover_key_from_iv_equal_key/writeup.md) |
| 28 | [Challenge 28](https://cryptopals.com/sets/4/challenges/28) | [sha1_keyed_mac.py](src/sets/set_04_stream_crypto_and_randomness/challenge_28_sha1_keyed_mac/sha1_keyed_mac.py) | [writeup](src/sets/set_04_stream_crypto_and_randomness/challenge_28_sha1_keyed_mac/writeup.md) |
| 29 | [Challenge 29](https://cryptopals.com/sets/4/challenges/29) | [sha1_length_extension.py](src/sets/set_04_stream_crypto_and_randomness/challenge_29_sha1_length_extension/sha1_length_extension.py) | [writeup](src/sets/set_04_stream_crypto_and_randomness/challenge_29_sha1_length_extension/writeup.md) |
| 30 | [Challenge 30](https://cryptopals.com/sets/4/challenges/30) | [md4_length_extension.py](src/sets/set_04_stream_crypto_and_randomness/challenge_30_md4_length_extension/md4_length_extension.py)<br>[md5_length_extension.py](src/sets/set_04_stream_crypto_and_randomness/challenge_30_md4_length_extension/md5_length_extension.py) | [writeup](src/sets/set_04_stream_crypto_and_randomness/challenge_30_md4_length_extension/writeup.md) |
| 31 | [Challenge 31](https://cryptopals.com/sets/4/challenges/31) | [utils.py](src/sets/set_04_stream_crypto_and_randomness/challenge_31_hmac_sha1_timing_leak_artificial/utils.py)<br>[server.py](src/sets/set_04_stream_crypto_and_randomness/challenge_31_hmac_sha1_timing_leak_artificial/server.py)<br>[attacker.py](src/sets/set_04_stream_crypto_and_randomness/challenge_31_hmac_sha1_timing_leak_artificial/attacker.py) | [writeup](src/sets/set_04_stream_crypto_and_randomness/challenge_31_hmac_sha1_timing_leak_artificial/writeup.md) |
| 32 | [Challenge 32](https://cryptopals.com/sets/4/challenges/32) | [server.py](src/sets/set_04_stream_crypto_and_randomness/challenge_32_hmac_sha1_timing_leak_less_artificial/server.py)<br>[attacker.py](src/sets/set_04_stream_crypto_and_randomness/challenge_32_hmac_sha1_timing_leak_less_artificial/attacker.py) | [writeup](src/sets/set_04_stream_crypto_and_randomness/challenge_32_hmac_sha1_timing_leak_less_artificial/writeup.md) |
| 33 | [Challenge 33](https://cryptopals.com/sets/5/challenges/33) | [diffie_hellman.py](src/sets/set_05_diffie_hellman_and_friends/challenge_33_diffie_hellman/diffie_hellman.py) | [writeup](src/sets/set_05_diffie_hellman_and_friends/challenge_33_diffie_hellman/writeup.md) |
| 34 | [Challenge 34](https://cryptopals.com/sets/5/challenges/34) | [server.py](src/sets/set_05_diffie_hellman_and_friends/challenge_34_dh_mitm_key_fixing/server.py)<br>[attacker.py](src/sets/set_05_diffie_hellman_and_friends/challenge_34_dh_mitm_key_fixing/attacker.py)<br>[client.py](src/sets/set_05_diffie_hellman_and_friends/challenge_34_dh_mitm_key_fixing/client.py) | [writeup](src/sets/set_05_diffie_hellman_and_friends/challenge_34_dh_mitm_key_fixing/writeup.md) |
| 35 | [Challenge 35](https://cryptopals.com/sets/5/challenges/35) | [server.py](src/sets/set_05_diffie_hellman_and_friends/challenge_35_dh_malicious_g/server.py)<br>[attacker.py](src/sets/set_05_diffie_hellman_and_friends/challenge_35_dh_malicious_g/attacker.py)<br>[client.py](src/sets/set_05_diffie_hellman_and_friends/challenge_35_dh_malicious_g/client.py) | [writeup](src/sets/set_05_diffie_hellman_and_friends/challenge_35_dh_malicious_g/writeup.md) |
| 36 | [Challenge 36](https://cryptopals.com/sets/5/challenges/36) | [server.py](src/sets/set_05_diffie_hellman_and_friends/challenge_36_srp/server.py)<br>[client.py](src/sets/set_05_diffie_hellman_and_friends/challenge_36_srp/client.py)<br>[utils.py](src/sets/set_05_diffie_hellman_and_friends/challenge_36_srp/utils.py) | [writeup](src/sets/set_05_diffie_hellman_and_friends/challenge_36_srp/writeup.md) |
| 37 | [Challenge 37](https://cryptopals.com/sets/5/challenges/37) | [server.py](src/sets/set_05_diffie_hellman_and_friends/challenge_37_srp_zero_key/server.py)<br>[client_setup_then_attack.py](src/sets/set_05_diffie_hellman_and_friends/challenge_37_srp_zero_key/client_setup_then_attack.py) | [writeup](src/sets/set_05_diffie_hellman_and_friends/challenge_37_srp_zero_key/writeup.md) |
| 38 | [Challenge 38](https://cryptopals.com/sets/5/challenges/38) | [fake_server.py](src/sets/set_05_diffie_hellman_and_friends/challenge_38_srp_offline_dictionary/fake_server.py)<br>[client.py](src/sets/set_05_diffie_hellman_and_friends/challenge_38_srp_offline_dictionary/client.py)<br>[server.py](src/sets/set_05_diffie_hellman_and_friends/challenge_38_srp_offline_dictionary/server.py) | [writeup](src/sets/set_05_diffie_hellman_and_friends/challenge_38_srp_offline_dictionary/writeup.md) |
| 39 | [Challenge 39](https://cryptopals.com/sets/5/challenges/39) | [rsa_implementation.py](src/sets/set_05_diffie_hellman_and_friends/challenge_39_rsa_implementation/rsa_implementation.py) | [writeup](src/sets/set_05_diffie_hellman_and_friends/challenge_39_rsa_implementation/writeup.md) |
| 40 | [Challenge 40](https://cryptopals.com/sets/5/challenges/40) | [rsa_broadcast_attack.py](src/sets/set_05_diffie_hellman_and_friends/challenge_40_rsa_broadcast_attack/rsa_broadcast_attack.py) | [writeup](src/sets/set_05_diffie_hellman_and_friends/challenge_40_rsa_broadcast_attack/writeup.md) |
| 41 | [Challenge 41](https://cryptopals.com/sets/6/challenges/41) | [unpadded_rsa_message_recovery.py](src/sets/set_06_rsa_and_dsa/challenge_41_unpadded_rsa_message_recovery/unpadded_rsa_message_recovery.py) | [writeup](src/sets/set_06_rsa_and_dsa/challenge_41_unpadded_rsa_message_recovery/writeup.md) |
| 42 | [Challenge 42](https://cryptopals.com/sets/6/challenges/42) | [rsa_signature_forgery.py](src/sets/set_06_rsa_and_dsa/challenge_42_rsa_signature_forgery/rsa_signature_forgery.py) | [writeup](src/sets/set_06_rsa_and_dsa/challenge_42_rsa_signature_forgery/writeup.md) |
| 43 | [Challenge 43](https://cryptopals.com/sets/6/challenges/43) | [dsa_key_recovery_from_nonce.py](src/sets/set_06_rsa_and_dsa/challenge_43_dsa_key_recovery_from_nonce/dsa_key_recovery_from_nonce.py) | [writeup](src/sets/set_06_rsa_and_dsa/challenge_43_dsa_key_recovery_from_nonce/writeup.md) |
| 44 | [Challenge 44](https://cryptopals.com/sets/6/challenges/44) | [dsa_nonce_reuse.py](src/sets/set_06_rsa_and_dsa/challenge_44_dsa_nonce_reuse/dsa_nonce_reuse.py) | [writeup](src/sets/set_06_rsa_and_dsa/challenge_44_dsa_nonce_reuse/writeup.md) |
| 45 | [Challenge 45](https://cryptopals.com/sets/6/challenges/45) | [dsa_parameter_tampering.py](src/sets/set_06_rsa_and_dsa/challenge_45_dsa_parameter_tampering/dsa_parameter_tampering.py) | [writeup](src/sets/set_06_rsa_and_dsa/challenge_45_dsa_parameter_tampering/writeup.md) |
| 46 | [Challenge 46](https://cryptopals.com/sets/6/challenges/46) | [rsa_parity_oracle.py](src/sets/set_06_rsa_and_dsa/challenge_46_rsa_parity_oracle/rsa_parity_oracle.py) | [writeup](src/sets/set_06_rsa_and_dsa/challenge_46_rsa_parity_oracle/writeup.md) |
| 47 | [Challenge 47](https://cryptopals.com/sets/6/challenges/47) | [pkcs1_v1_5_padding_oracle_rsa256.py](src/sets/set_06_rsa_and_dsa/challenge_47_pkcs1_v1_5_padding_oracle/pkcs1_v1_5_padding_oracle_rsa256.py)<br>[pkcs1_v1_5_padding_oracle_rsa2048.py](src/sets/set_06_rsa_and_dsa/challenge_47_pkcs1_v1_5_padding_oracle/pkcs1_v1_5_padding_oracle_rsa2048.py) | [writeup](src/sets/set_06_rsa_and_dsa/challenge_47_pkcs1_v1_5_padding_oracle/writeup.md) |
| 48 | [Challenge 48](https://cryptopals.com/sets/6/challenges/48) | [server.py](src/sets/set_06_rsa_and_dsa/challenge_48_bleichenbacher_98/server.py)<br>[attacker.py](src/sets/set_06_rsa_and_dsa/challenge_48_bleichenbacher_98/attacker.py)<br>[client.py](src/sets/set_06_rsa_and_dsa/challenge_48_bleichenbacher_98/client.py) | [writeup](src/sets/set_06_rsa_and_dsa/challenge_48_bleichenbacher_98/writeup.md) |
| 49 | [Challenge 49](https://cryptopals.com/sets/7/challenges/49) | [iv_control.py](src/sets/set_07_hashes/challenge_49_cbc_mac_message_forgery/iv_control.py)<br>[no_iv_control.py](src/sets/set_07_hashes/challenge_49_cbc_mac_message_forgery/no_iv_control.py) | [writeup](src/sets/set_07_hashes/challenge_49_cbc_mac_message_forgery/writeup.md) |
| 50 | [Challenge 50](https://cryptopals.com/sets/7/challenges/50) | [hashing_with_cbc_mac.py](src/sets/set_07_hashes/challenge_50_hashing_with_cbc_mac/hashing_with_cbc_mac.py) | [writeup](src/sets/set_07_hashes/challenge_50_hashing_with_cbc_mac/writeup.md) |
| 51 | [Challenge 51](https://cryptopals.com/sets/7/challenges/51) | [compression_ratio_side_channel.py](src/sets/set_07_hashes/challenge_51_compression_ratio_side_channel/compression_ratio_side_channel.py) | [writeup](src/sets/set_07_hashes/challenge_51_compression_ratio_side_channel/writeup.md) |
| 52 | [Challenge 52](https://cryptopals.com/sets/7/challenges/52) | [iterated_hash_multicollisions.py](src/sets/set_07_hashes/challenge_52_iterated_hash_multicollisions/iterated_hash_multicollisions.py) | [writeup](src/sets/set_07_hashes/challenge_52_iterated_hash_multicollisions/writeup.md) |
| 53 | [Challenge 53](https://cryptopals.com/sets/7/challenges/53) | [expandable_messages.py](src/sets/set_07_hashes/challenge_53_expandable_messages/expandable_messages.py) | [writeup](src/sets/set_07_hashes/challenge_53_expandable_messages/writeup.md) |
| 54 | [Challenge 54](https://cryptopals.com/sets/7/challenges/54) | [nostradamus_attack.py](src/sets/set_07_hashes/challenge_54_nostradamus_attack/nostradamus_attack.py) | [writeup](src/sets/set_07_hashes/challenge_54_nostradamus_attack/writeup.md) |
| 55 | [Challenge 55](https://cryptopals.com/sets/7/challenges/55) | not implemented | [writeup](src/sets/set_07_hashes/challenge_55_md4_collisions/writeup.md) |
| 56 | [Challenge 56](https://cryptopals.com/sets/7/challenges/56) | not implemented | [writeup](src/sets/set_07_hashes/challenge_56_rc4_single_byte_biases/writeup.md) |
| 57 | [Challenge 57](https://toadstyle.org/cryptopals/513b590b41d19eff3a0aa028023349fd.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_57_diffie_hellman_revisited_subgroup_confinement/writeup.md) |
| 58 | [Challenge 58](https://toadstyle.org/cryptopals/3e17c7b35fcf491d08c989081ed18c9a.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_58_pollards_method_catching_kangaroos/writeup.md) |
| 59 | [Challenge 59](https://toadstyle.org/cryptopals/a0833e607878a80fdc0808f889c721b1.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_59_ecdh_invalid_curve_attacks/writeup.md) |
| 60 | [Challenge 60](https://toadstyle.org/cryptopals/c53b90a3e9e753ddad56edbbd33838aa.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_60_single_coordinate_ladders_insecure_twists/writeup.md) |
| 61 | [Challenge 61](https://toadstyle.org/cryptopals/809dccecda0e94ea588d66c12a1cf593.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_61_duplicate_signature_key_selection/writeup.md) |
| 62 | [Challenge 62](https://toadstyle.org/cryptopals/76f2e314809b2a34ce9ff0d2a08f7a7f.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_62_ecdsa_biased_nonce_key_recovery/writeup.md) |
| 63 | [Challenge 63](https://toadstyle.org/cryptopals/2dfbf7e58fd43c140b62485f8d90bebe.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_63_gcm_repeated_nonces_key_recovery/writeup.md) |
| 64 | [Challenge 64](https://toadstyle.org/cryptopals/1d79ee513b73e1e0367eae2297e9f234.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_64_gcm_truncated_mac_key_recovery/writeup.md) |
| 65 | [Challenge 65](https://toadstyle.org/cryptopals/a1a2e7311ec5f2535ec46eaebd4588f0.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_65_gcm_truncated_mac_improved_key_recovery/writeup.md) |
| 66 | [Challenge 66](https://toadstyle.org/cryptopals/66.txt) | not implemented | [writeup](src/sets/set_08_abstract_algebra/challenge_66_dh_implementation_errors/writeup.md) |

## Testing / Verification

Run the project checks:
```powershell
python scripts/verify_project.py
```

This validates folder structure, writeups, data files, and Python syntax.

## License

MIT License. See `LICENSE.md`.
