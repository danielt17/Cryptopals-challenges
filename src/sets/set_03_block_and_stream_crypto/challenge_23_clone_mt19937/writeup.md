# Challenge 23: Clone an MT19937 RNG from its output
Set: 03 - Block and stream crypto
Cryptopals: https://cryptopals.com/sets/3/challenges/23
Run: `python scripts/run_challenge.py 23`

## Goal
Clone an MT19937 RNG from its output.

## Cryptographic Insight
The tempering function is invertible. Given 624 consecutive outputs, you can invert the tempering to recover the entire internal state and then predict all future outputs.

## Method
- Collect 624 outputs from the RNG.
- Invert the tempering function to recover each internal state value.
- Initialize a new MT19937 instance with the recovered state and predict outputs.

## Detailed Walkthrough
Cloning MT19937 uses the fact that its output is a tempered version of the internal state. By inverting the tempering step on 624 consecutive outputs, you can reconstruct the full state.

Once the state is known, the cloned RNG produces the same outputs as the original.

- Collect 624 consecutive outputs.
- Invert the tempering function for each output.
- Set the recovered state in a new RNG instance.

## Implementation Notes
Scripts: clone_mt19937.py
Data files: none
Run: python scripts/run_challenge.py 23

## Verification
The script verifies that the cloned RNG matches future outputs.
