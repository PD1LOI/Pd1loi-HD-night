#
#  CamdInfo - Converter
#
#  Coded by weazle (c) 2010
#  Support: www.dreambox-tools.info
#
#  This plugin is licensed under the Creative Commons 
#  Attribution-NonCommercial-ShareAlike 3.0 Unported 
# <widget source="session.CurrentService" render="Label" position="189,397" zPosition="4" size="350,20" noWrap="1" valign="center" halign="center" font="Regular;14" foregroundColor="clText" transparent="1"  backgroundColor="#20002450">
#	<convert type="pliCamd">Camd</convert>
# </widget>			

from enigma import iServiceInformation
from Components.Converter.Converter import Converter
from Components.Element import cached
from Tools.Directories import fileExists
import os


class pliCamd(Converter, object):
	def __init__(self, type):
		Converter.__init__(self, type)

	@cached
	def getText(self):
		service = self.source.service
		info = service and service.info()
		camd = ""
		camdlist = None
		serlist = None
		if not info:
			return ""
		
		#Pli
		elif fileExists("/etc/init.d/softcam") or fileExists("/etc/init.d/cardserver"):
			try:
				camdlist = os.popen("/etc/init.d/softcam info")
			except:
				pass
			try:
				serlist = os.popen("/etc/init.d/cardserver info")
			except:
				pass
			
		# Unknown emu
		else:
			return None
			
		if serlist is not None:
			try:
				cardserver = ""
				for current in serlist.readlines():
					cardserver = current
				serlist.close()
			except:
				pass
		else:
			cardserver = "NA"

		if camdlist is not None:
			try:
				emu = ""
				for current in camdlist.readlines():
					emu = current
				camdlist.close()
			except:
				pass
		else:
			emu = "NA"
			
		return "%s %s" % (cardserver.split('\n')[0], emu.split('\n')[0])
		
	text = property(getText)

	def changed(self, what):
		Converter.changed(self, what)
