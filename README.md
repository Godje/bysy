# Bysy
#### -read busy

Self-management Time logging tool written in Python. Writes to a JSON database, to be later used in self-analysis.

The way you can record and analyse the data is up to you. Although I provide a very simple and
effective example at the bottom.

Clearly inspired by **Log** by Josh Avanier

**Navigation**
- [Usage](https://github.com/Godje/bysy#usage)
- [Config](https://github.com/Godje/bysy#config)
- [Entry Structure](https://github.com/Godje/bysy#entry-structure-ideas)

## Usage

`*` means required input

- **start** 
	- args: `<sector*, project*, details*, comment>` 
	- starts a new Bysy entry with those parameters.
- **stop** or **pause**
	- stops the last entry
- **delete** 
	-	`<id*>` 
	- deletes an entry
- **list** or **ls** or **log**
	-	`<amount>`
	- lists the `amount` of last entries
- **time**
	- tells how much time have you been busy with the last entry
- **resume** 
	-	`<id>`
	-	resumes the task, or the entry at the `id` you type in. By resuming, means start it again.

**Example commands:**
```
$ bysy.py start "Dev" "Bysy" "Fixing bugs"
<output>
$ bysy.py stop

$ bysy.py start "Dev" "Bysy" "Fixing bugs" "finishing up on Issue #3"
<output>

$ bysy.py list
2 | Dev | Bysy | Fixing bugs | <start-time> |
1 | Dev | Bysy | Fixing bugs | <start-time> | <end-time>

$ bysy.py delete 1

$ bysy.py time #time since the Entry #2 started
0:04:00 
```

Analysing scripts and such will come later after a stable Core is done.

## Config

- **`listmax`** `<Number>`
	-	Limit the amount of items displayed in the list command. (Useful when you have more entries, than lines in your visible Terminal)

## Entry Structure ideas

**sector** - What task are you performing 

**project** - What project are you working on

**details** - Specific detail/section about your **current** task 

**comments** - some more specific details ignored in the analysis

6 related entry examples:
```
Code | TodoApp | UI | finishin up button animations
Code | TodoApp | UI | impletementing menu button
Code | Website | Environment | <blank>
Code | Website | Environment | Fixing npm config
Code | TodoApp | Backend | fixing api
Design | TodoApp | Backend | fixing api
```

Later can be parsed into such data:

**Sector focus:**
- **Code** 83.3% 
- **Design** 16.7%

**Project focus:**
- **Website** 33.3%
- **TodoApp** 66.6% 

Details can be used for further analysis specific to the project, or specific to the Sector/action
Comments are only used for later identification. Of course you are free to use the in the analysis
scripts if you want, but for me, it's just a simple little identification, of what the heck I was 
doing then
