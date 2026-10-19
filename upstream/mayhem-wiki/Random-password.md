![image](https://github.com/user-attachments/assets/2a477229-c556-484e-b6e0-0af17be4e72b)

This is an [external app](External-apps-informations) (`.ppma` file on the SD card).

This app use AFSK demodulated data as random seeds for each char, use LCG + one more random layer as PRNG algorithms to generate passwords.

In theory if the quality of seeds (which is from mostly radio noise) is good enough, then the password randomization would be good enough. But usually they are not, or we don’t know, or they do but not stable. So even if this is more secure than many other PRNG generators, in the best case it even can be considered as TRNG generators, don’t use this at high security scenes, for example money-related things.

All the “send” button/checkbox in this app means send via serial async messages, check serial page in this wiki for more details. 

Flood mode is from streaming generated code, this will always streaming into serial, alternatively you can check the savin checkbox to save generated codes and seeds. Keep in mind that with seeds, you can generated same code with proper PRNG, so they are same level of security, don’t leak them.

# Each shuffle algo and what it can bring you

There are two dimensions of password safety: 
- Entropy: When you generate mass of password, it should split evenly in the possible space, that controls password quality. In this app, the only entropy provider is the demodulated AFSK data. the LCG/ sha-512/ shuffle algo won't bring more entropy.
- Randomness: It controls how many total possibilities can be generated. In this app, the only randomness provider is the "each digits using different seed in the buffer" algorithm, which spread the total possible combination into the max value of possibility: (CHARNUMBER)^{DIGITS}.

| Algo / Source                                                            | Bring Entropy ? | Bring Randomization ? | Bring difficult to reverse calculation ? | Made it harder to Brute-Force ? | Time Complexity and Space Complexity    |
| -------------------------------------------------------------------------- | ----------------- | ----------------------- | ------------------------------------------ | --------------------------------- | ----------------------------------------- |
| Use time as seeds to pick a random frequency with LCG to fetch AFSK data | 🚫              | ✅                    | 🚫                                       | 🚫                              | O(1) - O(1)                             |
| The original demodulated AFSK data as seeds                              | ✅              | 🚫                    | 🚫                                       | 🚫                              | O(1) - O(1)                             |
| Each digits using different seed in the buffer                           | ✅              | 🚫                    | 🚫                                       | ✅                              | O(n^DITIGS_NUMBER) - O(n^DITIGS_NUMBER) |
| The LCG PRNG algo inside of cpp STL                                      | 🚫              | ✅                    | 🚫                                       | 🚫                              | O(n) - O(1)                             |
| Shuffle with two groups of seeds                                         | 🚫              | ✅                    | 🚫                                       | ✅                              | O(n) - O(n)                             |
| The SHA-512 hash algo                                                    | 🚫              | ✅                    | ✅                                       | 🚫                              | O(n) - O(1)                             |
| Result                                                                   | ✅ x 2          | ✅ * 4                | ✅ * 1                                   | ✅ * 2                          |                                         |