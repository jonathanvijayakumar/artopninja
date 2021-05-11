# ChangeLog
All notable changes to this project will be documented in this file.

## [0.1.0]() - 2021-01-05
First release of the AutosarModeller. Please refer README for more information.

## [0.1.1]() - 2021-01-11
Provision to get the objects which refer a particular object.

## [0.2.0]() - 2021-01-16
### Added
New UI to visualize the Autosar model.
### Changed
- New API `get_children()` to get child elements of a particular autosar element
- New API `get_property_values()` to get values of all attributes of anautosar element.

## [0.2.1]() - 2021-01-24
Support for processing the integer attributes configured as hex, binary or octal values in arxml file.

## [0.2.2]() - 2021-01-28
- Small UI improvement - posibility to select search type
- Implemented multiple type searches (by short name, by Autosar type and by regular expression on name)
- Added menu bar - implemented theme selection at runtime

## [0.2.3]() - 2021-02-04
- Small UI improvement - possibility to copy `name` and `path` of a node from the autosar explorer to clipboard.
