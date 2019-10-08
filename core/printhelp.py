class txtmodif:
	NORMAL = '\033[0m'
	BOLD = '\033[1m'
	WARNING = '\033[91m'

## Print help function
def printhelp(args):
	help_string = """{0}\

Available methods:{1}

	{0}start{1}\t\t\t- (Sector, Project, Description) starts a new Log
	{0}stop|pause{1}\t\t- stops the last log
	{0}list|ls|log{1}\t\t- lists logs
	{0}time{1}\t\t\t- tells how much time has passed since the last log
	{0}delete{1}\t\t\t- delets a selected log
	{0}resume{1}\t\t\t- resumes a the last task. Or the task at <id> you specify
	{0}help{1}\t\t\t- displays this help message
		"""
	print help_string.format(txtmodif.BOLD, txtmodif.NORMAL)
