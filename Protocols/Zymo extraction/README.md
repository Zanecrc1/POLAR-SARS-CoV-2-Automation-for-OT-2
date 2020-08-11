# Zymo Quick RNA/DNA Viral Magbead Extraction Automation
## Description
This protocol automates the Zymo quick RNA/DNA viral magbead extraction kit on the Opentrons OT-2 liquid handling platform. This protocol is a work in progress.
## Hardware
This protocol utilizes the following hardware:  
<br>
(1x) [Opentrons OT-2 liquid handling robot](https://shop.opentrons.com/products/ot-2)   
<br>
(1x) [Opentrons Gen2 temperature module](https://shop.opentrons.com/products/tempdeck)  
<br>
(1x) [Opentrons Gen2 magnetic module](https://shop.opentrons.com/products/magdeck)  
<br>
(1x) [Opentrons Gen2 P20 8-channel pipettor](https://shop.opentrons.com/collections/ot-2-robot/products/8-channel-electronic-pipette)  
<br>
(Variable) [Opentrons p200 filtered pipette tips](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-200ul-filter-tips) or [Biotix uTIP 200ul filtered tips](https://biotix.com/products/pipette-tips/utip-universal-pipette-tips/200-%ce%bcl-racked-sterilized/)
<br>
<br>
(1x per run) [Opentrons p10/p20 filtered pipette tips](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-10ul-tips) or [Biotix uTIP 10XL filtered tips](https://biotix.com/products/pipette-tips/utip-universal-pipette-tips/10-%ce%bcl-xl-racked-filtered-sterilized/)  
<br>
(1x per run) [Bio Rad Hard-Shell® 96-Well PCR Plates, low profile, thin wall, skirted, catalog #HSP9601](https://www.bio-rad.com/en-us/sku/hsp9601-hard-shell-96-well-pcr-plates-low-profile-thin-wall-skirted-white-clear?ID=hsp9601)  
<br>
## Reagents
* All reagents from the [Zymo quick RNA/DNA viral magbead extraction kit](https://www.zymoresearch.com/pages/quick-viral-covid-19), prepared according to the [kit manual](https://files.zymoresearch.com/protocols/_r2140_r2141_quick-dna-rna_viral_magbead.pdf):
  * 1X Shield
  * Viral magbeads
  * Magbead buffer
  * Wash Buffer 1
  * Wash Buffer 2
  * Nuclease free water
* 100% ethanol

## Setup 
Be sure to clean the OT-2 robot before setting up any run. See the Opentrons guide on how to do this [here](https://www.protocols.io/view/cleaning-an-ot-2-covid-19-diagnostic-station-beb5jaq6)
<br>
All labware should be calibrated **from the bottom of the wells.** You can learn about how to calibrate your robot [here](https://support.opentrons.com/en/articles/2687641-get-started-pipette-and-labware-calibration)
