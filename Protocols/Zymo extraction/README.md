# Zymo Quick RNA/DNA Viral Magbead Extraction Automation
## Description
This protocol automates the Zymo quick RNA/DNA viral magbead extraction kit on the Opentrons OT-2 liquid handling platform. This protocol is a work in progress.
## Hardware
This protocol utilizes the following hardware:  
* (1x) [Opentrons OT-2 liquid handling robot](https://shop.opentrons.com/products/ot-2)   
* (1x) [Opentrons Gen2 temperature module](https://shop.opentrons.com/products/tempdeck)  
* (1x) [Opentrons Gen2 magnetic module](https://shop.opentrons.com/products/magdeck)  
* (1x) [Opentrons Gen2 P20 8-channel pipettor](https://shop.opentrons.com/collections/ot-2-robot/products/8-channel-electronic-pipette)  
* (Variable) [Opentrons p200 filtered pipette tips](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-200ul-filter-tips) or [Biotix uTIP 200ul filtered tips](https://biotix.com/products/pipette-tips/utip-universal-pipette-tips/200-%ce%bcl-racked-sterilized/)
* (1x per run) [Opentrons p10/p20 filtered pipette tips](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-10ul-tips) or [Biotix uTIP 10XL filtered tips](https://biotix.com/products/pipette-tips/utip-universal-pipette-tips/10-%ce%bcl-xl-racked-filtered-sterilized/)  
* (1x per run) [Bio Rad Hard-Shell® 96-Well PCR Plates, low profile, thin wall, skirted, catalog #HSP9601](https://www.bio-rad.com/en-us/sku/hsp9601-hard-shell-96-well-pcr-plates-low-profile-thin-wall-skirted-white-clear?ID=hsp9601)  
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
* Be sure to clean the OT-2 robot before setting up any run. See the Opentrons guide on how to do this [here](https://www.protocols.io/view/cleaning-an-ot-2-covid-19-diagnostic-station-beb5jaq6)
* All labware should be calibrated **from the bottom of the wells.** You can learn about how to calibrate your robot [here](https://support.opentrons.com/en/articles/2687641-get-started-pipette-and-labware-calibration)
* Ensure that the pipette tip box on **slot 6** is **EMPTY.** This box needs to be an [Opentrons p200 box](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-200ul-filter-tips). The robot will placing used tips in this box to store them before re-use. Because of this the box needs to have slotted bottoms that protect each tip from contaminating eachother. This is true of the Opentrons tip boxes. All other tips can either be Biotix uTIPs or Opentrons tips as well. 
