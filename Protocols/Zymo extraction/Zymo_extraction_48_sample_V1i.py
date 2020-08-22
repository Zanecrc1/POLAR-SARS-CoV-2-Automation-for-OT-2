from opentrons import types, protocol_api
 
metadata = {
    'protocolName': 'POLAR Express NA Extraction',
    'author': 'Zane Colaric & Brian Glenn St Hilaire',
    'source': '',
    'apiLevel': '2.5'
    }

def run(polar_express_na_extraction):

	# Define tipracks and their locations 
	clean_tips_p300 = [polar_express_na_extraction.load_labware('biotix_utip_200_ul', s) for s in ['10','11','7', '8']]
	clean_tips_p20 = [polar_express_na_extraction.load_labware('biotix_utip_20_ul', s) for s in ['4',]]
	dirty_rack = polar_express_na_extraction.load_labware('opentrons_96_filtertiprack_200ul', '6')

  	# Pipettes
	p300 = polar_express_na_extraction.load_instrument('p300_multi_gen2', 'left', tip_racks=clean_tips_p300)
	p20 = polar_express_na_extraction.load_instrument('p20_multi_gen2', 'right', tip_racks=clean_tips_p20) 
  
  	# Modules
	magdeck = polar_express_na_extraction.load_module('magnetic module gen2', '9')
	tempdeck = polar_express_na_extraction.load_module('temperature module gen2', '1') 

 	# Plastics
	mag_plate = magdeck.load_labware('eppendorf_96_wellplate_500ul')
	elution_plate = tempdeck.load_labware('opentrons_96_aluminumblock_biorad_wellplate_200ul')
	reagent_wells = polar_express_na_extraction.load_labware('nest_12_reservoir_15ml', '3')
  
  	# Reagent setup. This is done in a 12 well reservoir plate
	protinase_k_nna_shield = reagent_wells['A1'] 
	nna_lysis_buffer_beads = reagent_wells['A2'] 
	magbead_nna_wash_1 = reagent_wells['A3'] 
	magbead_nna_wash_2 = reagent_wells['A4'] 
	ethanol_1 = reagent_wells['A5']
	ethanol_2 = reagent_wells['A6']
	nf_water = reagent_wells['A7']

 	# Number of sample colums to run. This can be 1-6
	number_of_sample_columns = 1

	# Set up and populate column lists based on number_of_sample_columns used 
	even_wells = []
	odd_wells = []
	all_wells = []
	for column in range(1, ((number_of_sample_columns*2)+1)):
	    if (column % 2) == 0:
	        even_wells.append(str("A") + str(column))
	        all_wells.append(str("A") + str(column))
	    else:
	        odd_wells.append(str("A") + str(column))
	        all_wells.append(str("A") + str(column))
	even_wells = tuple(even_wells)
	odd_wells = tuple(odd_wells)
	all_wells = tuple(all_wells)
	aspirate_depth = 0
	dispense_depth = 7.5
	zero = 0
	reagent_aspirate = 2 
	
	# Used to clean the tip of any residual liquids, and return the tip to a storage box between usage
	def blow_touch_store(instrument, sample_column, store_column):
		instrument.blow_out(mag_plate[sample_column].bottom(dispense_depth))
		instrument.touch_tip(mag_plate[store_column], radius = .7, v_offset= -10)
		instrument.move_to(mag_plate[store_column].top(-10))
		instrument.drop_tip(dirty_rack[store_column].top(-35)) 

	# Adds a reagent to sample columns. Includes a conditional for ethanol additions to add to the edges of a well to wash any residual salts from touch_tip away 
	def add(instrument, volume, reagent):
		magdeck.disengage()
		for sample_column, store_column in zip (even_wells, odd_wells):
			instrument.flow_rate.dispense = 50
			instrument.flow_rate.aspirate = 50
			instrument.pick_up_tip()
			instrument.aspirate(volume, reagent.bottom(reagent_aspirate))
			polar_express_na_extraction.max_speeds['Z'] = 50
			instrument.move_to(reagent.top())
			polar_express_na_extraction.max_speeds['Z'] = 300
			if reagent in (ethanol_1, ethanol_2):
				instrument.move_to(mag_plate[sample_column].top(-3))
				instrument.dispense(volume/4, mag_plate[sample_column].top().move(types.Point(x=-3.2, y=0, z=-3)))
				instrument.dispense(volume/4, mag_plate[sample_column].top().move(types.Point(x=+3.2, y=0, z=-3)))
				instrument.dispense(volume/4, mag_plate[sample_column].top().move(types.Point(x=0, y=+3.2, z=-3)))
				instrument.dispense(volume/4, mag_plate[sample_column].top().move(types.Point(x=0, y=-3.2, z=-3)))
				blow_touch_store(instrument, sample_column, store_column)
			else:
				instrument.dispense(volume, mag_plate[sample_column].bottom(dispense_depth))
				blow_touch_store(instrument, sample_column, store_column)

	# Mix reagents in sample columns for bead washes
	def mix_well(instrument, volume, reps):
		for sample_column, store_column in zip (even_wells, odd_wells):
			instrument.pick_up_tip(dirty_rack[store_column])
			instrument.flow_rate.dispense = 400
			instrument.flow_rate.aspirate = 300
			for i in range(reps):
				instrument.aspirate(volume*(3/10), mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=1, y=0, z=2)))
				instrument.aspirate(volume*(3/10), mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=0, y=0, z=1)))
				instrument.dispense(volume*(6/10), mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=-1.25, y=0, z=3)))
			instrument.flow_rate.dispense = 50
			instrument.flow_rate.aspirate = 50
			instrument.aspirate(volume*(8/10), mag_plate[sample_column].bottom(2))
			instrument.dispense(volume*(8/10), mag_plate[sample_column].bottom(dispense_depth))
			blow_touch_store(instrument, sample_column, store_column)

	# The initial mixing method to mix magbeads with sample. This mixes in a simplified way to reduce protocol time
	def mix_well_first(instrument, volume, reps):
		for sample_column, store_column in zip (even_wells, odd_wells):
			instrument.pick_up_tip(dirty_rack[store_column])
			instrument.flow_rate.dispense = 400
			instrument.flow_rate.aspirate = 300
			for i in range(reps):
				instrument.aspirate(volume*(7/10), mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=0, y=0, z=2)))
				instrument.dispense(volume*(7/10), mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=-0, y=0, z=3)))
			instrument.flow_rate.dispense = 50
			instrument.flow_rate.aspirate = 50
			instrument.aspirate(volume*(8/10), mag_plate[sample_column].bottom(2))
			instrument.dispense(volume*(8/10), mag_plate[sample_column].bottom(dispense_depth))
			blow_touch_store(instrument, sample_column, store_column)

	# The commands for engaging the magnetic module, and its accompanying incubation time
	def bind(height_in_mm, time_in_secs):
		magdeck.engage(height = height_in_mm)
		polar_express_na_extraction.delay(seconds = time_in_secs)

	# Removes reagents from column wells after binding the beads to a magnet
	def remove(instrument, volume):
		for sample_column, store_column in zip (even_wells, odd_wells):
			instrument.flow_rate.aspirate = 25
			instrument.pick_up_tip(dirty_rack[store_column])
			instrument.aspirate(volume, mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=1, y=0, z=0.6)))
			polar_express_na_extraction.delay(seconds = 3)
			instrument.flow_rate.aspirate = 25
			instrument.aspirate((200-volume), mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=1, y=0, z=0)))
			instrument.drop_tip()

	# A specialized mix function used to optimize the resuspension and elution step. 
	def elute(instrument=p20, volume=20, reps=10, reagent=nf_water):
		magdeck.disengage()
		for sample_column in even_wells:
			instrument.flow_rate.dispense = 50
			instrument.pick_up_tip()
			instrument.aspirate(volume, reagent.bottom(aspirate_depth))
			instrument.dispense(volume, mag_plate[sample_column].bottom(zero).move(types.Point(x=-2, y=0, z=3)))
			for i in range(reps):
				instrument.aspirate(volume, mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=0, y=0, z=0)))
				instrument.dispense(volume, mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=-2, y=0, z=1)))
			instrument.blow_out(mag_plate[sample_column].bottom(dispense_depth))
			instrument.touch_tip(mag_plate[sample_column], radius = .80, v_offset = -10)
			instrument.move_to(mag_plate[sample_column].top(-10))
			instrument.drop_tip()

	# Magbeads tend to settle quickly in the reagent well. This function is used to resuspend the beads prior to usage to ensure a more uniform distribution of beads
	def mix_stock(instrument=p300, reps=15, reagent=nna_lysis_buffer_beads):
		instrument.pick_up_tip()
		instrument.flow_rate.dispense = 300
		if number_of_sample_columns < 2:
			mix_stock_volume = 100
		else:
			mix_stock_volume = 200
		for i in range(reps):
			instrument.aspirate(mix_stock_volume, reagent.bottom(1))
			instrument.dispense(mix_stock_volume, reagent.bottom(6))
		instrument.flow_rate.aspirate = 50
		instrument.flow_rate.dispense = 50
		instrument.aspirate(mix_stock_volume, reagent.bottom(2))
		instrument.dispense(mix_stock_volume, reagent.bottom(2))
		instrument.blow_out(reagent.bottom(10))
		instrument.drop_tip() 
	# Transfers the final elution into the temperature module, placing copies of the sample next to each other
	def transfer_elute(instrument=p20, volume=4, seconds=30):
		magdeck.engage(height = 7.25)
		polar_express_na_extraction.delay(seconds)
		for sample_column, store_column in zip (even_wells, odd_wells):
			magdeck.engage(height = 7.25)
			instrument.flow_rate.aspirate = 2
			instrument.flow_rate.dispense = 2
			instrument.pick_up_tip()
			instrument.aspirate(volume, mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=1, y=0, z=0)))
			instrument.dispense(volume, elution_plate[store_column].bottom(zero))
			instrument.blow_out(elution_plate[store_column].bottom(dispense_depth))
			instrument.touch_tip(elution_plate[store_column], radius = .80, v_offset = -4)
			instrument.move_to(elution_plate[store_column].top(-4))
			instrument.aspirate(volume, mag_plate[sample_column].bottom(aspirate_depth).move(types.Point(x=1, y=0, z=0)))
			instrument.dispense(volume, elution_plate[sample_column].bottom(zero))
			instrument.blow_out(elution_plate[sample_column].bottom(dispense_depth))
			instrument.touch_tip(elution_plate[sample_column], radius = .80, v_offset = -4)
			instrument.move_to(elution_plate[sample_column].top(-4))
			instrument.drop_tip()
	# Adds proteinase K and mixes the sample and reagent
	def pro_k_treat(instrument=p300, volume=25, reps=5):
		for sample_column, store_column in zip (even_wells, odd_wells):
			instrument.flow_rate.dispense = 50
			instrument.flow_rate.aspirate = 100
			instrument.pick_up_tip()
			instrument.aspirate(volume, protinase_k_nna_shield.bottom(reagent_aspirate))
			polar_express_na_extraction.max_speeds['Z'] = 50
			instrument.move_to(protinase_k_nna_shield.bottom(30))
			polar_express_na_extraction.max_speeds['Z'] = 300
			instrument.dispense(volume, mag_plate[sample_column].bottom(zero))
			for i in range(reps):
				instrument.aspirate(volume, mag_plate[sample_column].bottom(zero))
				instrument.dispense(volume, mag_plate[sample_column].bottom(zero))
			instrument.flow_rate.dispense = 50
			instrument.flow_rate.aspirate = 50
			instrument.aspirate(50*(8/10), mag_plate[sample_column].bottom(zero))
			instrument.dispense(50*(8/10), mag_plate[sample_column].bottom(5))
			instrument.blow_out(mag_plate[store_column].bottom(dispense_depth))
			instrument.touch_tip(mag_plate[store_column], radius = .80, v_offset = -4)
			instrument.move_to(mag_plate[store_column].top(-4))
			instrument.drop_tip()

	# RNA will need to be kept cold to reduce degradation. The temperature module is preemtively set to 4C for this purpose
	tempdeck.set_temperature(4)
	polar_express_na_extraction.pause(msg = 'Begin Extraction')
	# Add proteinase K (1 tip used)
	pro_k_treat() # Tested: BGS 7Aug20
	polar_express_na_extraction.delay(minutes = 1)

	# Mix magbeads before adding
	mix_stock() # Tested: BGS 7Aug20

	# Add beads/buffer, mix, remove (1 tip used)
	polar_express_na_extraction.comment(msg = 'Perfoming magbead addition and mixing')
	add(p300, 100, nna_lysis_buffer_beads) # Tested: BGS 7Aug20
	mix_well_first(p300, 140, 30) # Tested: BGS 7Aug20
	bind(7.3, 45) # Tested: BGS 7Aug20
	remove(p300, 150) # Tested: BGS 7Aug20

	# Add wash 1, mix, remove (1 tip used)
	polar_express_na_extraction.comment(msg = 'Perfoming wash 1')
	add(p300, 150, magbead_nna_wash_1) # Tested: BGS 7Aug20
	mix_well(p300, 150, 15) # Tested: BGS 7Aug20
	bind(7.25, 45) # Tested: BGS 7Aug20
	remove(p300, 150) # Tested: BGS 7Aug20

	# Add wash 2, mix, remove (1 tip used)
	polar_express_na_extraction.comment(msg = 'Perfoming wash 2')
	add(p300, 150, magbead_nna_wash_2) # Tested: BGS 7Aug20
	mix_well(p300, 150, 15) # Tested: BGS 7Aug20
	bind(7.25, 45) # Tested: BGS 7Aug20
	remove(p300, 150) # Tested: BGS 7Aug20

	# Add 100% EtOH, mix, remove (1 of 2) (1 tip used)
	polar_express_na_extraction.comment(msg = 'Perfoming ethanol wash 1')	
	add(p300, 180, ethanol_1) # Tested: BGS 7Aug20
	mix_well(p300, 180, 15) # Tested: BGS 7Aug20
	bind(7.25, 45) # Tested: BGS 7Aug20
	remove(p300, 180) # Tested: BGS 7Aug20

	# Add 100% EtOH, mix, remove (2 of 2) (1 tip used)
	polar_express_na_extraction.comment(msg = 'Perfoming ethanol wash 2')	
	add(p300, 180, ethanol_2) # Tested: BGS 7Aug20
	mix_well(p300, 180, 15) # Tested: BGS 7Aug20
	bind(7.25, 45) # Tested: BGS 7Aug20
	remove(p300, 180) # Tested: BGS 7Aug20

	# Wait n minutes to allow excess ethanol to evaporate off.
	polar_express_na_extraction.comment(msg = 'Delaying 10 minutes to allow excess ethanol to evaporate off')	
	polar_express_na_extraction.delay(minutes = 10) # Tested: BGS 7Aug20

	# Elute and transfer to final plate
	polar_express_na_extraction.comment(msg = 'Perfoming final elution')	
	elute()
	transfer_elute()

	# Flash deck lights to visually signal end of protocol
	polar_express_na_extraction.comment(msg = 'Protocol completed')	
	for i in range(100):
		polar_express_na_extraction.set_rail_lights(False)
		polar_express_na_extraction.delay(seconds = 0.5)
		polar_express_na_extraction.set_rail_lights(True)
		polar_express_na_extraction.delay(seconds = 0.5)













