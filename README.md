# Bysy
#### -read busy

A Python Time logger. Writes to JSON database, to be later used in self-analysis.

The way you can record and analyse the data is up to you. Although I provide a very simple and
effective example at the bottom.

Clearly inspired by **Log** by Josh Avanier

### Usage

`*` means required input

- **start** | `<sector*, project*, details*, comment>` 
	- starts a new Bysy entry with those parameters.
- **stop** 
	- stops the last entry
- **delete** | `<id*>` 
	- deletes an entry
- **list** | `<amount>`
	- lists the `amount` of last entries
- **time**
	- tells how much time have you been busy with the last entry

### Entry Structure ideas

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
