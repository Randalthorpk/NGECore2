import sys
from resources.datatables import Options

def setup(core, object):
	object.setAttachment('radial_filename', 'object/conversation')
	object.setAttachment('conversationFile', 'respec')
	return