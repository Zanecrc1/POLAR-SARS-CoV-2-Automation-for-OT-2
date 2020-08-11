from opentrons import types, protocol_api

#POLAR EXPRESS
#Aiden
#Zane Colaric Brian St. Hilaire 
#APIv2

#-------------------------------------------------------------------------------------------------
#Notes: 
#-------------------------------------------------------------------------------------------------

metadata={"apiLevel": "2.5"}

def run(protocol_context):


	# Labware Setup
	rt_reagents = protocol_context.load_labware(
		'nest_12_reservoir_15mL', '2')


	# Tiprack set up, split for manual tracking
	p20rack1 = protocol_context.load_labware('opentrons_96_filtertiprack_20ul', '3')
	p20rack2 = protocol_context.load_labware('opentrons_96_filtertiprack_20ul', '5')
	p20rack3 = protocol_context.load_labware('opentrons_96_filtertiprack_20ul', '6')
	p20rack4 = protocol_context.load_labware('opentrons_96_filtertiprack_20ul', '8')
	p20rack5 = protocol_context.load_labware('opentrons_96_filtertiprack_20ul', '9')
	p20rack6 = protocol_context.load_labware('opentrons_96_filtertiprack_20ul', '11')

	# Pipette Setup
	p20 = protocol_context.load_instrument('p20_multi_gen2', 'left')
	#p300 = protocol_context.load_instrument('p300_multi', 'right')

	# Module Setup
	magdeck = protocol_context.load_module('magnetic module gen2', '4')
	mag_plate = magdeck.load_labware('biorad_96_wellplate_200ul_pcr')

	tempdeck = protocol_context.load_module('temperature module gen2', '1')
	cold_reagents = tempdeck.load_labware(
	    'opentrons_96_aluminumblock_biorad_wellplate_200ul')

	thermocycler = protocol_context.load_module('thermocycler')
	reaction_plate = thermocycler.load_labware(
	    'biorad_96_wellplate_200ul_pcr')

	#Cold reagents, located in slot 1, temperature module. Well columns 1-6 are reagents, and columns 7-12 are indexes 
	RT_PCR_MM_pool_1 = cold_reagents['A1']
	RT_PCR_MM_pool_2 = cold_reagents['A1'] #FOR TESTING
	hackflex_mm = cold_reagents['A3']
	PCR_mm = cold_reagents['A4']


	# Room temperature reagents, in 12 well reservoir
	mineral_oil = rt_reagents['A1']
	twb = rt_reagents['A2']
	tag_stop =rt_reagents['A3']
	spri = rt_reagents['A4']
	ethanol = rt_reagents['A5']
	tris = rt_reagents['A6']

	#PCR cycle designations
	pcr_cycles_1 = 40 # TEST 
	pcr_cycles_2 = 4


	#Reagent volumes
	sample_vol = 4
	RT_PCR_MM_vol = 6
	hackflex_vol = 10
	tag_stop_vol = 10
	#eth_vol = 10 #ul
	#tris_vol = 10 #ul
	#spri_ratio = 0.8 #x

	total_vol = 20 #RT_PCR_MM_vol + hackflex_vol + tag_stop_vol + sample_vol


	#Slow down head movement
	protocol_context.max_speeds['X'] = 300
	protocol_context.max_speeds['Y'] = 300
	#protocol_context.max_speeds['Z'] = 50

	p20.flow_rate.dispense = 3.5
	p20.flow_rate.aspirate = 3.5


	#Comment out or add in the well names that the samples will be located in.
	#ex: 'A1', 'B1', 'C1', 'D6', 'A4'
	#If using multichannel, only use A1, A2, A3 etc, this will use all wells within that column. ex: 'A1' will use wells A1, B1, C1, D1, E1, F1, G1, H1. 
	#Order of wells is important- first well listed will be the first used and last well listed will be the last used
	
	all_samples = 'A2', 'A4','A6', 'A8', # 'A9', 'A10', 'A11', 'A12'
				  #'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12'
				  #'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12'
				  #'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12'
				  #'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12'
				  #'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'
				  #'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12'
				  #'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12'

	side_A = 	  'A1', 'A2', 'A3', 'A4', 'A5', 'A6' 
				  #'B1', 'B2', 'B3', 'B4', 'B5', 'B6' 
				  #'C1', 'C2', 'C3', 'C4', 'C5', 'C6' 
				  #'D1', 'D2', 'D3', 'D4', 'D5', 'D6' 
				  #'E1', 'E2', 'E3', 'E4', 'E5', 'E6' 
				  #'F1', 'F2', 'F3', 'F4', 'F5', 'F6' 
				  #'G1', 'G2', 'G3', 'G4', 'G5', 'G6' 
				  #'H1', 'H2', 'H3', 'H4', 'H5', 'H6' 

	side_B =	  'A7', 'A8', 'A9', 'A10', 'A11', 'A12'
				  #'B7', 'B8', 'B9', 'B10', 'B11', 'B12'
				  #'C7', 'C8', 'C9', 'C10', 'C11', 'C12'
				  #'D7', 'D8', 'D9', 'D10', 'D11', 'D12'
				  #'E7', 'E8', 'E9', 'E10', 'E11', 'E12'
				  #'F7', 'F8', 'F9', 'F10', 'F11', 'F12'
				  #'G7', 'G8', 'G9', 'G10', 'G11', 'G12'
				  #'H7', 'H8', 'H9', 'H10', 'H11', 'H12'

	sample_set_A = 'A2', 'A6',

	sample_set_B = 'A4', 'A8',

	pooling_wells = 'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12' 

	index_rows = side_B


	# A function used for more efficient mixing
	def well_mix(instrument, reps, vol, location):
		for i in range(reps):
			instrument.aspirate(vol/2, location.move(types.Point(x=-1.5, y=0, z=2)))
			instrument.aspirate(vol/2, location.move(types.Point(x=0, y=0, z=1)))
			instrument.dispense(vol, location.move(types.Point(x=+1.5, y=0, z=3)))

	#START PROTOCOL, IT WILL PAUSE ONCE SETUP TEMP IS REACHED. PRESS RESUME WHEN REAGENTS AND SAMPLES ARE LOADED
 
	#Preset temperatures for the temperature module and the thermocycler to ensure 
	#reagents are kept at proper temperature
	tempdeck.set_temperature(10)
	thermocycler.open_lid()
	thermocycler.set_block_temperature(10)
	thermocycler.set_lid_temperature(25)
	magdeck.disengage()

	protocol_context.pause(msg = 'PRESS RESUME WHEN REAGENTS AND SAMPLES ARE LOADED')

	# Add RT PCR master mix to pool 1 (sample set 1)
	for i, j in zip(side_A, sample_set_A):
		p20.pick_up_tip(p20rack1[i])
		p20.aspirate(RT_PCR_MM_vol, RT_PCR_MM_pool_1.bottom(0.2))
		p20.dispense(RT_PCR_MM_vol + 5, reaction_plate[j].bottom(5))
		#p20.mix(3, 7, reaction_plate[j].bottom(0))
		protocol_context.delay(seconds = 1)
		protocol_context.max_speeds['Z'] = 10
		p20.move_to(reaction_plate[j].top(-5))
		p20.blow_out(reaction_plate[j].top(-5))
		p20.touch_tip(reaction_plate[j], radius = .80, v_offset = -4)
		p20.aspirate(10, reaction_plate[j].top(-4))
		p20.move_to(reaction_plate[j].top(-4))
		protocol_context.max_speeds['Z'] = 50
		p20.return_tip()

	for i, j in zip(side_B, sample_set_B):
		p20.pick_up_tip(p20rack1[i])
		p20.aspirate(RT_PCR_MM_vol, RT_PCR_MM_pool_2.bottom(0.2))
		p20.dispense(RT_PCR_MM_vol + 5, reaction_plate[j].bottom(5))
		#p20.mix(3, 7, reaction_plate[j].bottom(0))
		protocol_context.delay(seconds = 1)
		protocol_context.max_speeds['Z'] = 10
		p20.move_to(reaction_plate[j].top(-5))
		p20.blow_out(reaction_plate[j].top(-5))
		p20.touch_tip(reaction_plate[j], radius = .80, v_offset = -4)
		p20.aspirate(10, reaction_plate[j].top(-4))
		p20.move_to(reaction_plate[j].top(-4))
		protocol_context.max_speeds['Z'] = 50
		p20.return_tip()

	#Add mineral oil (The RT-PCR step is very long and even with increased thermocyler seal thickness, over 50% loss was observed)
	for i in all_samples:
		p20.pick_up_tip(p20rack2[i])
		p20.move_to(mineral_oil.bottom(15))
		protocol_context.max_speeds['Z'] = 10
		p20.aspirate(10, mineral_oil.bottom(1))
		p20.move_to(mineral_oil.bottom(15))
		protocol_context.max_speeds['Z'] = 50
		p20.flow_rate.dispense = 2
		p20.move_to(reaction_plate[i].top(-6))
		p20.dispense(7, reaction_plate[i].top(-6).move(types.Point(x=-1.3, y=0, z=0)))
		protocol_context.delay(seconds = 2)
		p20.touch_tip(reaction_plate[i], radius = .80, v_offset = -4)
		p20.move_to(reaction_plate[i].top(-4))
		p20.aspirate(5, reaction_plate[i].top(-4))
		p20.flow_rate.dispense = 3.5
		p20.drop_tip()

	#Qiagen RT-PCR One-Step Ahead program  
	#PCR setup, temp and cycle designation 
	thermocycler.close_lid()
	thermocycler.set_block_temperature(50)
	protocol_context.delay(minutes = 15) #real time _10__ (+5 min for mixing)
	thermocycler.set_block_temperature(95)
	protocol_context.delay(minutes = 5) #real time __1_

	#Qiagen RT-PCR One-Step Ahead PCR Program 
	COVER_TEMP = 25
	PLATE_TEMP_PRE = 25
	PLATE_TEMP_HOLD_1 = (95, 15)
	PLATE_TEMP_HOLD_2 = (65, 30)
	PLATE_TEMP_HOLD_3 = (72, 30)
	PLATE_TEMP_POST = 25

	CYCLED_STEPS = [{'temperature': PLATE_TEMP_HOLD_1[0], 'hold_time_seconds': PLATE_TEMP_HOLD_1[1]},
                    {'temperature': PLATE_TEMP_HOLD_2[0], 'hold_time_seconds': PLATE_TEMP_HOLD_2[1]},
                    {'temperature': PLATE_TEMP_HOLD_3[0], 'hold_time_seconds': PLATE_TEMP_HOLD_3[1]}]

	# Work starts here
	# Qiagen RT-PCR One-Step Ahead program              
	# Set PRE temp
	thermocycler.set_block_temperature(PLATE_TEMP_PRE)
	# Set LID temp
	thermocycler.set_lid_temperature(COVER_TEMP)

	thermocycler.set_block_temperature(PLATE_TEMP_HOLD_2[0], hold_time_seconds=PLATE_TEMP_HOLD_2[1])

	thermocycler.execute_profile(steps=CYCLED_STEPS, repetitions=pcr_cycles_1)

	thermocycler.set_block_temperature(PLATE_TEMP_POST)
	protocol_context.delay(minutes = 1)

	thermocycler.open_lid()

	protocol_context.pause()


	# #Qiagen RT-PCR One-Step Ahead program  
	# #PCR setup, temp and cycle designation 
	# thermocycler.close_lid()
	# thermocycler.set_block_temperature(55)
	# protocol_context.delay(minutes = 15) #real time _10__ (+5 min for mixing)
	# thermocycler.set_block_temperature(95)
	# protocol_context.delay(minutes = 1) #real time __1_

	# #Qiagen RT-PCR One-Step Ahead PCR Program 
	# COVER_TEMP = 105
	# PLATE_TEMP_PRE = 25
	# PLATE_TEMP_HOLD_1 = (95, 15)
	# PLATE_TEMP_HOLD_2 = (63, 180)
	# PLATE_TEMP_POST = 25

	# CYCLED_STEPS = [{'temperature': PLATE_TEMP_HOLD_1[0], 'hold_time_seconds': PLATE_TEMP_HOLD_1[1]},
 #                    {'temperature': PLATE_TEMP_HOLD_2[0], 'hold_time_seconds': PLATE_TEMP_HOLD_2[1]}]

	# # Work starts here
	# # Qiagen RT-PCR One-Step Ahead program              
	# # Set PRE temp
	# thermocycler.set_block_temperature(PLATE_TEMP_PRE)
	# # Set LID temp
	# thermocycler.set_lid_temperature(COVER_TEMP)

	# thermocycler.set_block_temperature(PLATE_TEMP_HOLD_2[0], hold_time_seconds=PLATE_TEMP_HOLD_2[1])

	# thermocycler.execute_profile(steps=CYCLED_STEPS, repetitions=pcr_cycles_1)

	# thermocycler.set_block_temperature(PLATE_TEMP_POST)
	# protocol_context.delay(minutes = 1)

	# thermocycler.open_lid()

	# protocol_context.pause()

	#Add X ul of HackFlex master mix to set A and B 
	p20.pick_up_tip(p20rack3['A1'])
	p20.mix(5, 10, hackflex_mm.bottom(1))
	p20.blow_out(hackflex_mm.top().move(types.Point(x=-1.2, y=0, z=0)))
	p20.touch_tip(hackflex_mm, radius = 0.8, v_offset = -4)
	p20.move_to(hackflex_mm.top(-4))
	p20.return_tip()

	for i, j in zip(side_A, sample_set_A):
		p20.pick_up_tip(p20rack3[i])
		p20.aspirate(hackflex_vol, hackflex_mm.bottom(0.8))
		p20.move_to(reaction_plate[j].top(-4))
		protocol_context.max_speeds['Z'] = 10
		p20.move_to(reaction_plate[j].bottom())
		protocol_context.delay(seconds = 2)
		p20.dispense(hackflex_vol, reaction_plate[j].bottom(1))
		protocol_context.max_speeds['Z'] = 50
		p20.flow_rate.dispense = 3.5
		p20.flow_rate.aspirate = 3.5
		p20.blow_out(reaction_plate[j].top(-7))
		p20.aspirate(hackflex_vol, reaction_plate[j].top(-4))
		p20.touch_tip(reaction_plate[j], radius = .80, v_offset = -4)
		p20.move_to(reaction_plate[j].top(-4))
		p20.return_tip()

	for i, j in zip(side_B, sample_set_B):
		p20.pick_up_tip(p20rack3[i])
		p20.aspirate(hackflex_vol, hackflex_mm.bottom(0.8))
		p20.move_to(reaction_plate[j].top(-4))
		protocol_context.max_speeds['Z'] = 10
		p20.move_to(reaction_plate[j].bottom())
		protocol_context.delay(seconds = 2)
		p20.dispense(hackflex_vol, reaction_plate[j].bottom(1))
		protocol_context.max_speeds['Z'] = 50
		p20.blow_out(reaction_plate[j].top(-7))
		p20.aspirate(hackflex_vol, reaction_plate[j].top(-4))
		p20.touch_tip(reaction_plate[j], radius = .80, v_offset = -4)
		p20.move_to(reaction_plate[j].top(-4))
		p20.return_tip()

	#Run tagmentation reaction 
	#thermocycler.close_lid()
	thermocycler.set_block_temperature(55)
	protocol_context.delay(minutes = 10) #real time __10m_ (+5 min added for mixing with heat)
	thermocycler.set_block_temperature(25)
	protocol_context.delay(minutes = 1) #real time _1m__
	#thermocycler.open_lid() 

	#Add X ul tagmentation stop buffer
	for i, j in zip(side_A, sample_set_A):
		p20.pick_up_tip(p20rack4[i])
		p20.aspirate(tag_stop_vol, tag_stop.bottom(0.5))
		p20.move_to(reaction_plate[j].top(-4))
		protocol_context.max_speeds['Z'] = 10
		p20.move_to(reaction_plate[j].bottom())
		protocol_context.delay(seconds = 2)
		p20.flow_rate.dispense = 2
		p20.flow_rate.aspirate = 2
		p20.dispense(tag_stop_vol, reaction_plate[j].bottom(1))
		protocol_context.max_speeds['Z'] = 50
		p20.mix(3, 10, reaction_plate[j].bottom(1))
		p20.flow_rate.dispense = 3.5
		p20.flow_rate.aspirate = 3.5
		p20.blow_out(reaction_plate[j].top(-4))
		p20.aspirate(10, reaction_plate[j].top(-4))
		p20.touch_tip(reaction_plate[j], radius = .80, v_offset = -4)
		p20.move_to(reaction_plate[j].top(-4))
		p20.return_tip()

	for i, j in zip(side_B, sample_set_B):
		p20.pick_up_tip(p20rack4[i])
		p20.aspirate(tag_stop_vol, tag_stop.bottom(0.5))
		p20.move_to(reaction_plate[j].top(-4))
		protocol_context.max_speeds['Z'] = 10
		p20.flow_rate.dispense = 2
		p20.flow_rate.aspirate = 2
		p20.dispense(tag_stop_vol, reaction_plate[j].bottom(1))
		protocol_context.max_speeds['Z'] = 50
		p20.mix(3, 10, reaction_plate[j].bottom(1)) #Need to mix?
		p20.flow_rate.dispense = 3.5
		p20.flow_rate.aspirate = 3.5
		p20.blow_out(reaction_plate[j].top(-4))
		p20.aspirate(10, reaction_plate[j].top(-4))
		p20.touch_tip(reaction_plate[j], radius = .80, v_offset = -4)
		p20.move_to(reaction_plate[j].top(-4))
		p20.return_tip()

	#thermocycler.close_lid()

	#Run PTC program for tagmentation stop buffer
	thermocycler.set_block_temperature(25)
	protocol_context.delay(minutes = 5) #___10m___
	thermocycler.set_block_temperature(10)
	protocol_context.delay(minutes = 2) ##___5m___
	#thermocycler.open_lid()

	#Combine pools, and transfer to magnetic module. Samples will end up in ODD numbered rows to reduce chances of contamination 
	for i, j, k in zip(side_A, sample_set_A, sample_set_B,):
		p20.flow_rate.dispense = 3.5
		p20.flow_rate.aspirate = 3.5
		p20.pick_up_tip(p20rack1[i])
		p20.move_to(reaction_plate[j].top())
		protocol_context.max_speeds['Z'] = 10
		p20.aspirate(total_vol, reaction_plate[j].bottom(-0.5))
		p20.move_to(reaction_plate[j].top())
		protocol_context.max_speeds['Z'] = 50
		p20.dispense(total_vol, mag_plate[j].bottom(2).move(types.Point(x=-1, y=0, z=0)))
		p20.touch_tip(mag_plate[j], radius = .80, v_offset = -4)
		p20.move_to(mag_plate[j].top(-4))

		p20.move_to(reaction_plate[k].top())
		protocol_context.max_speeds['Z'] = 10
		p20.aspirate(total_vol, reaction_plate[k].bottom(-0.5))
		p20.move_to(reaction_plate[k].top())
		protocol_context.max_speeds['Z'] = 50
		p20.dispense(total_vol, mag_plate[j].bottom(2).move(types.Point(x=-1, y=0, z=0)))
		protocol_context.delay(seconds = 1)
		p20.blow_out(mag_plate[j].bottom(5))
		p20.aspirate(10, mag_plate[j].top(-3))
		p20.touch_tip(mag_plate[j], radius = .80, v_offset = -4)
		p20.move_to(mag_plate[j].top(-4))

		#waste consolidation from even wells into odd wells
		p20.dispense(10, reaction_plate[k].bottom(5))
		p20.aspirate(15, reaction_plate[k].bottom())
		p20.aspirate(5, reaction_plate[k].bottom())
		p20.dispense(20, reaction_plate[j].bottom(2).move(types.Point(x=-1, y=0, z=0)))
		p20.aspirate(20, reaction_plate[k].bottom(-0.1))
		p20.touch_tip(reaction_plate[j], radius = .80, v_offset = -4)
		p20.move_to(reaction_plate[j].top(-4))


		p20.return_tip()

	magdeck.engage(height = 6.5)
	protocol_context.delay(minutes = 2)

	#After binding the beads to the magnet, dispose of the supernatant

	for i, j, k in zip(side_A, side_B, sample_set_A):
		p20.pick_up_tip(p20rack1[i])
		p20.flow_rate.aspirate = 2.5
		p20.aspirate(20, mag_plate[k].bottom().move(types.Point(x=-1.2, y=0, z=0)))
		p20.touch_tip(mag_plate[k], radius = .80, v_offset = -5)
		p20.dispense(20, reaction_plate[k].top(-5))
		p20.touch_tip(reaction_plate[k], radius = .80, v_offset = -5)
		p20.aspirate(20, mag_plate[k].bottom().move(types.Point(x=-1.2, y=0, z=0)))
		p20.touch_tip(mag_plate[k], radius = .80, v_offset = -5)
		p20.dispense(20, reaction_plate[k].top(-5))
		p20.touch_tip(reaction_plate[k], radius = .80, v_offset = -5)
		p20.drop_tip()
		p20.pick_up_tip(p20rack1[j])
		p20.aspirate(20, mag_plate[k].bottom().move(types.Point(x=-0.5, y=0, z=0)))
		p20.flow_rate.aspirate = 3.5
		p20.drop_tip()

	#Add the TWB and mix to wash the beads
	for i, j in zip(side_A, sample_set_A):
		p20.flow_rate.dispense = 3.5
		p20.pick_up_tip(p20rack5[i])
		p20.aspirate(17, twb.bottom(1))
		p20.dispense(17, mag_plate[j].bottom(2).move(types.Point(x=+1.2, y=0, z=3)))
		protocol_context.delay(seconds = 2)
		p20.aspirate(20, mag_plate[j].top(-4))
		p20.touch_tip(radius = .80, v_offset = -4)
		p20.move_to(mag_plate[j].top(-4))
		p20.return_tip()

	protocol_context.delay(minutes = 2) #reat time 5 mins
	#Remove TWB
	for i, j in zip(side_A, sample_set_A):
		p20.flow_rate.aspirate = 2
		p20.pick_up_tip(p20rack5[i])
		p20.aspirate(20, mag_plate[j].bottom(-0.1).move(types.Point(x=-1.5, y=0, z=0)))
		p20.drop_tip()

	protocol_context.pause()

	#Add PCR master mix to index, and use to resuspend beads, then transfer to PCR plate
	magdeck.disengage()

	for i, j, k in zip (index_rows, sample_set_A, sample_set_B):
		p20.pick_up_tip(p20rack5[i])
		p20.aspirate(10, PCR_mm.bottom(0.5))
		p20.dispense(10, cold_reagents[i].bottom(1))
		p20.mix(3, 15, cold_reagents[i].bottom(1))
		p20.aspirate(20, cold_reagents[i].bottom())
		p20.dispense(20, mag_plate[j].bottom(3))
		p20.flow_rate.dispense = 50
		p20.flow_rate.aspirate = 30
		well_mix(p20, 5, 17, mag_plate[j].bottom())
		p20.mix(5, 17, mag_plate[j].bottom(1).move(types.Point(x=+1.5, y=0, z=1)))
		p20.flow_rate.dispense = 3.5
		p20.flow_rate.aspirate = 3.5
		p20.aspirate(15, mag_plate[j].bottom(-0.1))
		protocol_context.delay(seconds = 2)
		p20.aspirate(5, mag_plate[j].bottom(-0.1))
		p20.move_to(mag_plate[j].bottom(0.1))
		p20.dispense(20, reaction_plate[k].bottom(1))
		protocol_context.delay(seconds = 2)
		p20.blow_out(reaction_plate[k].bottom(6))
		p20.touch_tip(reaction_plate[k], radius = .80, v_offset = -4)
		p20.move_to(reaction_plate[k].top(-4))
		p20.aspirate(15, mag_plate[j].bottom(-0.1))
		protocol_context.delay(seconds = 2)
		p20.aspirate(5, mag_plate[j].bottom(-0.1))
		p20.move_to(mag_plate[j].bottom(0.1))
		p20.dispense(20, reaction_plate[k].bottom(1))
		protocol_context.delay(seconds = 2)
		p20.blow_out(reaction_plate[k].bottom(6))
		p20.touch_tip(reaction_plate[k], radius = .80, v_offset = -4)
		p20.move_to(reaction_plate[k].top(-4))

		p20.return_tip()

	# #Temperature module is no longer in use after this step, so it is deactivated 
	tempdeck.deactivate()

	thermocycler.close_lid()

	#PCR setup, temp and cycle designation for final PCR reaction
	COVER_TEMP = 105
	PLATE_TEMP_PRE = 25
	PLATE_TEMP_HOLD_1 = (98, 30)  # 30)
	PLATE_TEMP_HOLD_2 = (98, 15)  # 10)
	PLATE_TEMP_HOLD_3 = (62, 15)   # 30)
	PLATE_TEMP_HOLD_4 = (65, 15)  # 30)
	PLATE_TEMP_POST = 25
	CYCLED_STEPS = [{'temperature': PLATE_TEMP_HOLD_2[0], 'hold_time_seconds': PLATE_TEMP_HOLD_2[1]},
	                {'temperature': PLATE_TEMP_HOLD_3[0], 'hold_time_seconds': PLATE_TEMP_HOLD_3[1]},
	                {'temperature': PLATE_TEMP_HOLD_4[0], 'hold_time_seconds': PLATE_TEMP_HOLD_4[1]}]

	# Set PRE temp
	thermocycler.set_block_temperature(PLATE_TEMP_PRE)
	# Set LID temp
	thermocycler.set_lid_temperature(COVER_TEMP)

	thermocycler.set_block_temperature(PLATE_TEMP_HOLD_1[0], hold_time_seconds=PLATE_TEMP_HOLD_1[1])

	thermocycler.execute_profile(steps=CYCLED_STEPS, repetitions=pcr_cycles_2)

	thermocycler.set_block_temperature(PLATE_TEMP_POST)
	protocol_context.delay(minutes = 0.5)

	thermocycler.deactivate()


	#POOLING --------------UNTESTED, NEED TO WATCH FOR IMPACTS------------

	# thermocycler.open_lid()

	#p20.pick_up_tip(p20rack4['H1']) #This needs to be a bottom most located pipette tip (H row), the multichannel acts as if the back most head is the only thing it has. Hence calling A1 
	#results in an action on all wells below the A row. picking up in the H row will ensure that only one tip is added to the head. 

	# for i, well in zip(set_A, pooling_wells):
	# 	p20.aspirate(5, reaction_plate[i].bottom())
	# 	p20.dispense(5, mag_plate[well].bottom(2))

	#Flash the lights to signal end of protocol
	for i in range(500):
		protocol_context.set_rail_lights(False)
		protocol_context.delay(seconds = 0.5)
		protocol_context.set_rail_lights(True)
		protocol_context.delay(seconds = 0.5)
