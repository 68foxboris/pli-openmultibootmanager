#############################################################################
#
# Copyright (C) 2014 Impex-Sat Gmbh & Co.KG
# Written by Sandro Cavazzoni <sandro@skanetwork.com>
# All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#############################################################################

from Screens.Screen import Screen
from Screens.MessageBox import MessageBox

from Components.ActionMap import ActionMap
from Components.Label import Label

from OMBManagerCommon import OMB_DATA_DIR, OMB_UPLOAD_DIR, OMB_TMP_DIR, OMB_MANAGER_VERION
from OMBManagerInstall import BOX_NAME
from OMBManagerLocale import _
from enigma import getDesktop
try:
	screenWidth = getDesktop(0).size().width()
except:
	screenWidth = 720

class OMBManagerAbout(Screen):
	if screenWidth >= 1920:
		skin = """
			<screen position="center,center" size="1000,400">
				<widget name="about" position="20,20" size="940,340" font="Regular;33" zPosition="1" foregroundColor="yellow" />
			</screen>"""
	else:
		skin = """
			<screen position="center,center" size="560,300">
				<widget name="about" position="10,10" size="540,240" font="Regular;22" zPosition="1" foregroundColor="yellow" />
			</screen>"""

	def __init__(self, session):
		Screen.__init__(self, session)
		
		self.setTitle(_('openMultiboot About'))

		about = "openMultiboot Manager " + OMB_MANAGER_VERION + "\n"
		about += BOX_NAME + "\n"
		about += "(c) 2014 Impex-Sat Gmbh & Co.KG\n\n"
		about += "Written by Sandro Cavazzoni <sandro@skanetwork.com>"
		about += "\n"
		about += "Modded by Meo"
		about += "\n"
		about += "\nPatch for openPli Dimitrij <dima-73@inbox.lv>"
		self['about'] = Label(about)
		self["actions"] = ActionMap(["SetupActions"],
		{
			"cancel": self.keyCancel
		})

	def keyCancel(self):
		self.close()
