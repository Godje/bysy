class txtmodif:
	NORMAL = '\033[0m'
	BOLD = '\033[1m'
	WARNING = '\033[91m'

## Print help function
def printhelp():
	help_string = """{0}\

Available methods:{1}

	{0}start{1}   - (Sector, Project, Description) starts a new Log
	{0}stop{1}		- stops the last log
	{0}list{1}		- lists logs
	{0}time{1}		- tells how much time has passed since the last log
	{0}delete{1}  - delets a selected log
	{0}help{1}		- displays this help message
		"""
	print help_string.format(txtmodif.BOLD, txtmodif.NORMAL)
