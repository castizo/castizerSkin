#!/usr/bin/python
import xbmc
import xbmcgui
import string
import os.path
import sys
 
PATHTOPLAYLISTS = xbmc.getInfoLabel( '$INFO[Skin.String(Setting.CastizerPlaylist)]' )
FILENAME = xbmc.translatePath("special://skin/config/castizersettings.txt")

#DIR_USERDATA = os.path.join( "special://home/", "hola.txt")
#print DIR_USERDATA

COMMAND_NEXT = '{"jsonrpc": "2.0", "method": "Player.GoTo", "params": { "playerid": 0, "to": "next" }, "id": 1}'
COMMAND_PLAY_PAUSE = '{"jsonrpc": "2.0", "method": "Player.PlayPause", "params": { "playerid": 0 }, "id": 1}'

count = len(sys.argv) - 1
 
if count == 0:
	#xbmcgui.Dialog().ok("Castizer script","no arguments specified")
	xbmc.executeJSONRPC(COMMAND_NEXT)
	sys.exit
	
#xbmcgui.Dialog().ok("Status",sys.argv[0] +" called with " + str(count)+" args",
#		"["+", ".join(sys.argv[1:])+"]")

par = sys.argv[1]
print par


print("CASTIZER BEGIN !")

#xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Player.PlayPause", "params": { "playerid": 0 }, "id": 1}')

#xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Player.Open", "params": { "item": { "file" : "/Users/pgarcia/workspace/castizer_data/test.m3u" } } }')

# If the file does not exist, create it with 0
if not os.path.isfile(FILENAME):
	print("Populating new file...")
	FILE = open(FILENAME, 'w')
	FILE.write('0 0' + '\n')
	FILE.close()

log = open(FILENAME, 'r')
for line in log:
	a, b = [int(i) for i in line.split()]
	print 'a = %d, b = %d\n' %(a, b)
number = int(a)
log.close()

number += 1
if number > 3:
	number = 1
#print("Current list: " + str(number))

playlist = PATHTOPLAYLISTS + str(number) + "/"
print playlist

#Save new list number
FILE = open(FILENAME, 'w')
FILE.write(str(number) + ' 69' + '\n')
FILE.close()

#xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Player.Open", "params": { "item": { "file" :  } } }')
xbmc.executebuiltin("PlayMedia(" + playlist + ")")

#print xbmc.executebuiltin('$INFO[Skin.String(Setting.CastizerImageFolder)]') 

#if number == 0:
#	print('OK')    
#else:
#	print('error')


  
print("CASTIZER END !")
