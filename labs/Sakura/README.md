# “Sakura” – TryHackMe Room Write-Up  
By [Anmol] 

---

## Task 1: INTRODUCTION  
I launched the room and got the introductory prompt. My mission: to track down the attacker “Aiko”, and piece together her online footprint.  
With nothing but the starting image and a few clues, I initiated my OSINT workflow.

---

## Task 2: TIP-OFF  
**What username does the attacker go by?**

I opened the provided image and downloaded it to inspect metadata and embedded clues.

![Screenshot](img1.png)  
I viewed the SVG source and noticed a background filled with binary digits—when translated they pointed me to look at the metadata.  

![username](usr1.png)

Within the file metadata I found a username reference **SakuraSnowAngelAiko** which became my pivot.

---

## Task 3: RECONNAISSANCE  
**What is the full email address used by the attacker?**  
**What is her real name?**

From the username I carried out Google searches and found her GitHub profile and Twitter/X account.

![Screenshot](img2.png)
![Screenshot](twitter.png)
I located her under handle **@AikoAbe3** and her display name **Aiko Abe**.  
I then found her public PGP key repository.

Using:

```
gpg pubkey
```

![[gpg_key.png]](gpg.png)

I extracted an email address: **SakuraSnowAngel83@protonmail.com**.

---

## Task 4: UNVEIL  
**What cryptocurrency does the attacker own a wallet for?**  
**What is the wallet address?**  
**What mining pool did she receive payments from on January 23 2021?**  
**What other crypto asset did she exchange?**

Within her GitHub “ETH” repository I found a mining script:

![Screenshot](pgp.png)

![Screenshot](img3.png)
![Screenshot](pass.png)
It contained:
```
stratum://0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef.Aiko:pswd@eu1.ethermine.org:4444
```

From the embedded wallet I traced transactions via Etherscan:

![Screenshot](img4.png)  
This confirmed payments from **Ethermine** and revealed ERC-20 token swaps.

---

## Task 5: TAUNT  
**What is the attacker’s current Twitter handle?**  
**What is the URL where she stored her WiFi SSIDs and passwords?**  
**What is the BSSID for her home WiFi?**

On her X profile I reviewed older posts, finding a URL hint to a paste-site containing WiFi SSIDs:

![Screenshot](img5.png)  
Using the SSID I queried Wigle.net and found the BSSID corresponding to Tokyo.

---

## Task 6: HOMEBOUND  
**What airport is closest to the photo location she shared before her flight?**  
**What lake can be seen in the map she posted?**  
**What city does she likely consider home?**

One tweet showed cherry blossoms and the Washington Monument in the background:

![Screenshot](img6.png) 
![Screenshot](lounge.png)
This led to airport code **DCA** (Washington D.C.).  
Later I found another map image showing a large lake in Japan:

![Screenshot](img7.png)  
Using metadata and geolocation I concluded her home city is **Tokyo**.

---

## Lessons Learned  
- SVG files can hide metadata and embedded messages.  
- PGP key repositories reveal valid email addresses.  
- GitHub commit history may leak real credentials.  
- Public blockchain data links identities and addresses.  
- OSINT is about piecing small clues into a coherent picture.

---

## Conclusion  
This room walks you through the full chain: from an innocuous image, to social profiles, crypto wallets, and finally location data.  
By following the breadcrumbs, I mapped out the attacker’s digital persona, tracked financial flows, and identified the physical context of her operations.

I found the final flag and completed the room successfully — this write-up documents the path.

