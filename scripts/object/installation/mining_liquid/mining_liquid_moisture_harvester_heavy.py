import sys

def setup(core, object):
	object.setAttachment('radial_filename', 'structure/harvester')
	object.setHarvester_type(4)
	object.setPowerCost(75); 
	object.setMaintenanceCost(90);
	return