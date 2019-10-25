# Bysy
read busy

Self-management Time logging tool written in Python.
The way you can record and analyse the data is up to you. I provide a very simple and
effective example at the bottom, but you are free to experiment.

Clearly inspired by **Log** by Josh Avanier

**Navigation**
- [Installation](https://github.com/Godje/bysy#installation)
- [Usage](https://github.com/Godje/bysy#usage)
- [Config](https://github.com/Godje/bysy#config)
- [Alias](https://github.com/Godje/bysy#alias)
- [Entry Structure](https://github.com/Godje/bysy#entry-structure-ideas)

## Installation

```
# clone and install
git clone https://github.com/Godje/bysy
cd bysy
pip install .

# init
bysy init
```

## Usage

`*` means required input

- **`start`** 
	- args: `<sector*, project*, details*, comment>` 
	- starts a new Bysy entry with those parameters.
- **`stop`** or **`pause`**
	- stops the last entry
- **`delete`** 
	-	`<id*>` 
	- deletes an entry
- **`list`** or **`ls`** or **`log`**
	-	`<amount>`
	- lists the `amount` of last entries
- **`time`**
	- tells how much time have you been busy with the last entry
- **`resume`** 
	-	`<id>`
	-	resumes the task, or the entry at the `id` you type in. By resuming, means start it again.
- **`config`**
	-	commands: `get`, `list`, `set`, `help`
	- further commands to change config values
- **`alias`**
	-	commands: `get`, `list`, `set`, `help`
	- further commands to change alias values


## Config

- **`get`**
	- args: `key`
	-	Internal command that returns the value for the config.
- **`list`**
	-	Lists all the configured values.
- **`set`**
	- args: `<key>`, `<value>`
	-	Set the new config value

### Config values

- **`listmax`** `<Number>`
	-	Limit the amount of items displayed in the list command. (Useful when you have more entries, than lines in your visible Terminal)

## Alias

- **`get`**
	- args: `key`
	-	Internal command that returns the value for the alias.
- **`list`**
	-	Lists all the configured aliases.
- **`set|create`**
	- args: `<key>`, `<value>`
	-	Set the new config value

#### Example commands

```
$ bysy start "Dev" "Bysy" "Fixing bugs"
<output>
$ bysy stop

$ bysy start "Dev" "Bysy" "Fixing bugs" "finishing up on Issue #3"
<output>

$ bysy list
2 | Dev | Bysy | Fixing bugs | <start-time> |
1 | Dev | Bysy | Fixing bugs | <start-time> | <end-time>

$ bysy delete 1

$ bysy time #time since the Entry #2 started
0:04:00 
```

Analysing scripts and such will come later after a stable Core is done.

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
