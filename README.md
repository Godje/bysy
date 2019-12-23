# Welcome to bysy 👋
![Version](https://img.shields.io/badge/version-1.1-blue.svg?cacheSeconds=2592000)
[![Documentation](https://img.shields.io/badge/documentation-yes-brightgreen.svg)](https://github.com/Godje/bysy/wiki)
[![License: MPL--2.0](https://img.shields.io/badge/License-MPL--2.0-yellow.svg)](https://github.com/Godje/bysy/blob/master/LICENSE)
[![Twitter: danielmayovsky](https://img.shields.io/twitter/follow/danielmayovsky.svg?style=social)](https://twitter.com/danielmayovsky)

> Self-management time logging tool

This is a manual tool for recording the activities you are busy with, to later analyze the data and see your habits, or anything you would like to do with the data. When you have the data on your time spending, the sky is the limit of what you see from it. This tool is just an opinionated helper on recording that data.

You mark the start and the end of a particular activity, and the `alias` or other commands are only there to make the marking of start of the activity easier.

The data entry has a following structure and recorded in JSON:

```
entry:
	s (sector): String, manual, required
	p (project): String, manual, required
	d (details): String, manual, required
	c (comments): String, manual, not required 
	s (start_date): Date, auto
	e (end_date): Date, auto
	i (id): Integer, auto
```

The commands are later explained in concise detail in the `help` command

## Install

```sh
pip install bysy
```
or [install from source](https://github.com/Godje/bysy/wiki/Install-from-source)

## Usage

```sh
bysy help
```

### Wiki

https://github.com/Godje/bysy/wiki

## Author

👤 **Daniel Mayovskiy**

* Website: https://danielmayovskiy.com
* Twitter: [@danielmayovskiy](https://twitter.com/DanielMayovsky)
* Github: [@godje](https://github.com/godje)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](https://github.com/Godje/bysy/issues).

## Show your support

Give a ⭐️ if this project helped you!


## 📝 License

Copyright © 2019 [Daniel Mayovskiy](https://github.com/godje).

This project is [MPL--2.0](https://github.com/Godje/bysy/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
