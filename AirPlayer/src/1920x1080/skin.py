#!/usr/bin/python
# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Pixmap import Pixmap
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

#<skin>
#<output id="0">
#	<resolution xres="1280" yres="720" bpp="32" />
#</output>

"""<screen name="AirPlayerMoviePlayer" position="240,600" size="880,80" title="InfoBar" flags="wfNoBorder">
	<ePixmap position="0,0" zPosition="-1" size="880,80" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/infobarmovie.png" />
	<eLabel text="AirPlayer" position="90, 5" size="260,35" font="Regular;26" valign="top" noWrap="1" foregroundColor="#00ffffff" backgroundColor="#00000000" transparent="1" />
	<ePixmap zPosition="-1" position="90,40" size="600,8" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/progress_lightgrey.png" />
	<widget source="session.CurrentService" render="Progress" position="90,40" size="600,8" zPosition="2" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/progress.png" transparent="1">
		<convert type="ServicePosition">Position</convert>
	</widget>
	<widget source="session.CurrentService" render="PositionGauge" position="90,40" size="500,10" zPosition="2" transparent="1">
		<convert type="ServicePosition">Gauge</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="90,48" size="120,28" font="Regular;24" halign="left" foregroundColor="#00ffffff" backgroundColor="#00000000" transparent="1">
		<convert type="ServicePosition">Position</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="321,48" size="120,28" font="Regular;24" halign="center" foregroundColor="#00ffffff" backgroundColor="#00000000" transparent="1">
		<convert type="ServicePosition">Remaining</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="550,48" size="140,24" font="Regular;22" halign="right" foregroundColor="#00ffffff" backgroundColor="#00000000" transparent="1">
		<convert type="ServicePosition">Length</convert>
	</widget>
	
	<widget name="bufferslider" position="90,40" size="600,8" zPosition="1" transparent="1" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/progress_grey.png" />
	<widget source="label_cache" transparent="1" render="Label" zPosition="2" position="440,4" size="250,18" font="Regular;17" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="right" />
	<widget source="label_speed" transparent="1" render="Label" zPosition="2" position="440,22" size="250,18" font="Regular;17" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="right" />
	<widget source="label_update"  transparent="1" render="Label" zPosition="4" position="225,5"  size="250,28" font="Regular;24" backgroundColor="#00000000" foregroundColor="#00ff0000" halign="right"/>
	
	<eLabel text="Premium" position="715,5" size="80,20" font="Regular;17" backgroundColor="#00000000" foregroundColor="#00ffffff" transparent="1" />
	<ePixmap zPosition="1" position="800,5" size="57,20" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/premium_off.png" />
	<widget source="premiumUser" render="Pixmap" position="800,5" size="57,20" zPosition="2" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/premium_on.png">
      <convert type="ConditionalShowHide" />
    </widget>
    
    <eLabel text="Proxy" position="715,30" size="80,20" font="Regular;17" backgroundColor="#00000000" foregroundColor="#00ffffff" transparent="1" />
	<ePixmap zPosition="1" position="800,30" size="57,20" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/proxy_off.png" />
	<widget source="useProxy" render="Pixmap" position="800,30" size="57,20" zPosition="2" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/proxy_on.png">
      <convert type="ConditionalShowHide" />
    </widget>
</screen>"""

"""<screen name="AirPlayMusicPlayer" position="340,120" size="600,452" title="AirPlayMusicPlayer" flags="wfNoBorder" >
    <widget source="label_update"  transparent="2" render="Label" zPosition="4" position="0,0"  size="600,28" font="Regular;24" backgroundColor="#00000000" foregroundColor="#00ff0000" />
    <widget name="label_message"  transparent="2" zPosition="4" position="0,30"  size="600,60" font="Regular;24" backgroundColor="#00000000" foregroundColor="#00ff0000" />
    <widget name="cover" position="0,90" size="300,300" zPosition="1" alphatest="on" />
    <widget name="label_title"  transparent="2" zPosition="4" position="305,100"  size="290,50" font="Regular;22" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="center"/>
    <widget name="label_album"  transparent="2" zPosition="4" position="305,150"  size="290,50" font="Regular;22" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="center"/>
    <widget name="label_interpret"  transparent="2" zPosition="4" position="305,200"  size="290,50" font="Regular;22" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="center"/>
    <ePixmap zPosition="-1" position="320,300" size="260,8" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/progress_grey_small.png" />
    <widget name="progress" position="320,300" size="260,8" zPosition="1" transparent="1" pixmap="%s/Extensions/AirPlayer/Skins/Classic/1280x720/progress_small.png" />
</screen>"""

#</skin>
