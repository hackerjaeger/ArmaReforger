This following search strings can be for search for the related information in Reforger server log files (.log). This can be done with the log-files-search.py tool or simple Windows-based "CTRL+F" searching when the log file is open.

Server Activity:

	Server FPS Low: "serveradmintools_server_fps_low"

	All Server FPS Entries: "FPS" 

		(lines will also provide # of players, AI, Vehicles at the moment)

Reforger Game Session:

	Game started: "serveradmintools_game_started"

	Game ended: "serveradmintools_game_ended"

ARES/GM Activity:

	All ARES/GM actions: "serveradmintools_admin_action"

Player Activity:

	Logins:  "serveradmintools_player_joined" 

		(provides time, player name & playerID)
			 
	All Activity for Specific Player: search using player ID (long alphanumeric string)

		(note, player IDs can be found as "ID", "identity" "IdentityId" - all poor search terms; the term PlayerID is NOT a unique ID)

	Connectivity Loss:  [placeholder]

	Blue-on-Blue/Fratricide: [placeholder]

Medical:

	All medical events: "NoInstantDeath"

	Hit Resulting in Immediate Knock-Out: "lethal hit intercepted"

	Unconsciousness: "unconscious"

	Bleed-out Status: "bleed-out"

	Death from Bleed-out: "bleed-out expired"

	Revivals: "revived"

	Player killed:  "serveradmintools_player_killed"

