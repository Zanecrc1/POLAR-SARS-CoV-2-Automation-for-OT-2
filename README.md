# POLAR-SARS-CoV-2-Automation-for-OT-2
## Description
This protocol automates the Pathogen-Oriented Low-Cost Assembly &amp; Re-Sequencing (POLAR) diagnostic SARS-CoV-2 test on the Opentrons OT-2 liquid handling platform
<br>
## Hardware
This protocol utilizes the following hardware:  
<br>
(1x) [Opentrons OT-2 liquid handling robot](https://shop.opentrons.com/products/ot-2)   
<br>
(1x) [Opentrons Gen 2 temperature module](https://shop.opentrons.com/products/tempdeck)  
<br>
(1x) [Opentrons Gen 2 magnetic module](https://shop.opentrons.com/products/magdeck)  
<br>
(1x) [Opentrons Gen2 P20 8-channel pipettor](https://shop.opentrons.com/collections/ot-2-robot/products/8-channel-electronic-pipette)  
<br>
(1x) [Gen 1 Opentrons thermocycler module](https://shop.opentrons.com/products/thermocycler-module)  
<br>
(5x per run) [Opentrons p10/p20 filtered pipette tips](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-10ul-tips)  
<br>
(1x per run) [Opentrons thermocycler rubber seals](https://shop.opentrons.com/products/thermocycler-seals)   
<br>
(3x per run) [Bio Rad Hard-Shell® 96-Well PCR Plates, low profile, thin wall, skirted, catalog #HSP9601](https://www.bio-rad.com/en-us/sku/hsp9601-hard-shell-96-well-pcr-plates-low-profile-thin-wall-skirted-white-clear?ID=hsp9601)  
<br>
## Reagents
a
<br>
b
<br>
c
<br>

## Setup
Be sure to clean the OT-s robot before setting up any run. See the Opentrons guide on how to do this [here](https://support.opentrons.com/en/articles/1795522-cleaning-your-ot-2)
### Deck Layout 
![Screen Shot 2020-08-03 at 2](https://user-images.githubusercontent.com/43655550/89315974-1c0c2e00-d641-11ea-8775-24df214e9456.png)
<br>
#### Temperature Module Reagents
Column 1: RT-PCR mastermix for pool 1 (6ul)
<br>
Column 2: RT-PCR mastermix for pool 2 (6ul) 
<br>
Column 3: Hackflex reagent (10ul)
<br>
Column 4: Final PCR master mix (10ul)
<br>
Columns 7-12: Library indexes (10ul)
### Thermocycler reagents
All samples in thermocycler will be loaded onto the thermocycler plate with a volume of 4ul. Sample duplicates are placed in neighboring rows (See diagram below)

![Screen Shot 2020-08-04 at 11](https://user-images.githubusercontent.com/43655550/89317215-b0c35b80-d642-11ea-859e-d1b6781276e6.png)
