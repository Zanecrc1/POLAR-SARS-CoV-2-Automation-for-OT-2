# POLAR-SARS-CoV-2-Automation-for-OT-2
## Description
This protocol automates the Pathogen-Oriented Low-Cost Assembly &amp; Re-Sequencing (POLAR) diagnostic SARS-CoV-2 test on the Opentrons OT-2 liquid handling platform. This protocol is a work in progress. 
<br>
## Hardware
This protocol utilizes the following hardware:  
* (1x) [Opentrons OT-2 liquid handling robot](https://shop.opentrons.com/products/ot-2)   
* (1x) [Opentrons Gen2 temperature module](https://shop.opentrons.com/products/tempdeck)  
* (1x) [Opentrons Gen2 magnetic module](https://shop.opentrons.com/products/magdeck)  
* (1x) [Opentrons Gen2 P20 8-channel pipettor](https://shop.opentrons.com/collections/ot-2-robot/products/8-channel-electronic-pipette)  
* (1x) [Gen 1 Opentrons thermocycler module](https://shop.opentrons.com/products/thermocycler-module)  
* (1x) [Opentrons p200 filtered pipette tips](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-200ul-filter-tips) or [Biotix uTIP 200ul filtered tips](https://biotix.com/products/pipette-tips/utip-universal-pipette-tips/200-%ce%bcl-racked-sterilized/)
* (5x per run) [Opentrons p10/p20 filtered pipette tips](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-10ul-tips) or [Biotix uTIP 10XL filtered tips](https://biotix.com/products/pipette-tips/utip-universal-pipette-tips/10-%ce%bcl-xl-racked-filtered-sterilized/)  
* (1x per run) [Opentrons thermocycler rubber seals](https://shop.opentrons.com/products/thermocycler-seals)   
* (3x per run) [Bio Rad Hard-Shell® 96-Well PCR Plates, low profile, thin wall, skirted, catalog #HSP9601](https://www.bio-rad.com/en-us/sku/hsp9601-hard-shell-96-well-pcr-plates-low-profile-thin-wall-skirted-white-clear?ID=hsp9601)
## Reagents 
* [Luna Universal Probe One-Step RT-qPCR Kit] (https://www.neb.com/products/e3006-luna-universal-probe-one-step-rt-qpcr-kit#Product%20Information)
* [Nextera DNA Flex Library Prep] (https://www.illumina.com/products/by-type/sequencing-kits/library-prep-kits/nextera-dna-flex.html)
* [Random Hexamer Primer] (https://www.thermofisher.com/order/catalog/product/SO142#/SO142)
* [Luna® Universal Probe One-Step RT-qPCR Kit] (https://www.neb.com/products/e3006-luna-universal-probe-one-step-rt-qpcr-kit#Product%20Information)
* [IDT for Illumina Nextera DNA Unique Dual Indexes Set] (https://www.illumina.com/products/by-type/sequencing-kits/library-prep-kits/nextera-dna-flex.html)
* [NEBNext® Q5U®  Master Mix] (https://www.neb.com/protocols/2019/04/09/reaction-setup-nebnext-q5u-master-mix-m0597)
* [Magnesium Chloride Solution (1M)] (https://www.sigmaaldrich.com/catalog/product/sigma/m1028?lang=en&region=US&gclid=EAIaIQobChMIiJ7z3sK86QIVhsDACh066wtlEAAYASAAEgICa_D_BwE)
* [N,N-Dimethylformamide (100%)] (https://www.sigmaaldrich.com/catalog/product/sial/227056?lang=en&region=US)
* [Sodium Dodecyl Sulfate, 10%] (https://www.thermofisher.com/order/catalog/product/AM9822#/AM9822)

## Setup
Be sure to clean the OT-2 robot before setting up any run. See the Opentrons guide on how to do this [here](https://www.protocols.io/view/cleaning-an-ot-2-covid-19-diagnostic-station-beb5jaq6)
<br>

For this protocol, the thermocycler unit will need to be modified to fit into only slots 7 & 10. A small black panel on the bottom of the thermocycler module needs to be unscrewed in order to allow the thermocycler to shift to the left and free up slots 8 & 11 for additional tips. Note that doing this inhibits the right pipettor from accessing well column 'A1' on the thermocycler module. The right pipettor will not be used to access this column in this protocol. Follow the steps [here](https://github.com/Zanecrc1/POLAR-SARS-CoV-2-Automation-for-OT-2/blob/master/metadata/remove_TC_plate.md) to do this.
<br>

The protocol has a build in pre-cooling/heating step where all modules will cool or heat to their initial working temperatures. Start the protocol and allow the modules to cool to their respective temperatures before adding temperature sensitive enzymes. Once these temperatures are reached the protocol will pause itself, and will ask you to press the RESUME button to begin the protocol.
<br>


All labware should be calibrated **from the bottom of the wells.** You can learn about how to calibrate your robot [here](https://support.opentrons.com/en/articles/2687641-get-started-pipette-and-labware-calibration)
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
### 12 Well Reservoir Reagents
Well 1: Sterile mineral oil (2mL)
<br>
Well 2: Tris-tween wash buffer
<br>
Well 3: Tagmentation stop buffer

### Thermocycler pre-run configuration
All samples will be loaded onto the thermocycler plate with a volume of 4ul. Sample duplicates are placed in neighboring rows (See diagram below)

![Screen Shot 2020-08-04 at 11](https://user-images.githubusercontent.com/43655550/89317215-b0c35b80-d642-11ea-859e-d1b6781276e6.png)
