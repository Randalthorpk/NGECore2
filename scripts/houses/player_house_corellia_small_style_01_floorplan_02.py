import sys
from services.housing import HouseTemplate
from engine.resources.scene import Point3D

def setup(core):
	houseTemplate = HouseTemplate("object/tangible/deed/player_house_deed/shared_corellia_house_small_floor_02_deed.iff", "object/building/player/shared_player_house_corellia_small_style_01_floorplan_02.iff", 2)
	
	houseTemplate.addBuildingSign("object/tangible/sign/player/shared_house_address.iff", Point3D(float(-7.39), float(2.36), float(2)))
	houseTemplate.addPlaceablePlanet("corellia")
	houseTemplate.addPlaceablePlanet("talus")
	houseTemplate.setDefaultItemLimit(200)
	
	core.housingService.addHousingTemplate(houseTemplate)
	return