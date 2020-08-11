# POLAR-SARS-CoV-2 and viral RNA extraction automation

## Introduction
This repository contains all necessary documentation and files to run automated versions of the Zymo quick DNA/RNA viral magbead kit and the POLAR SARS-CoV-2 protocol. 

## Usage
These protocols run as a relay, with the Zymo extraction protocol output being the input for the POLAR protocol. Moving from one robot to the next only requires that the elution plate from the Zymo extraction protocol be manually moved from the temperature module of the extraction robot to the thermocycler of the POLAR robot. If you are not immediately running the samples post extraction, the extracted RNA will need to be **immediately frozen** to avoid RNA degradation. 

## Directory structure
* [`/Protocols`](https://github.com/Zanecrc1/POLAR-SARS-CoV-2-Automation-for-OT-2/tree/master/Protocols) Contains both the Zymo extraction protocol and the POLAR protocol .py files that can be uploaded to the OT-2 robot
* [`Protocols/Zymo extraction`](https://github.com/Zanecrc1/POLAR-SARS-CoV-2-Automation-for-OT-2/tree/master/Protocols/Zymo%20extraction) Contains the Zymo quick DNA/RNA viral magbead kit protocol and docs, designed to intake up to 6 columns of samples (48)
* [`Protocols/POLAR`](https://github.com/Zanecrc1/POLAR-SARS-CoV-2-Automation-for-OT-2/tree/master/Protocols/POLAR) Contains the POLAR Express protocol and docs, designed to intake up to 6 columns of samples (48)
* [`/custom_labware`](https://github.com/Zanecrc1/POLAR-SARS-CoV-2-Automation-for-OT-2/tree/master/custom_labware) Contains the .json files for all necessary custom labware items used in the protocols
* [`/metadata`](https://github.com/Zanecrc1/POLAR-SARS-CoV-2-Automation-for-OT-2/tree/master/metadata) Contains technical drawings for custom labware, and any other bits that may proves useful to someone out there 
