# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.2] - 2025-07-11

### Fixed
- Transparent PNGs and BMPs were previously converted without alpha, resulting in solid backgrounds. This is now resolved.

## [1.3.1] - 2025-07-10
### Fixed
- Improved error logging when attempting to write files in protected or read-only folders.


## [1.2.1] - 2025-07-06

### Added
- Display file size next to each image during conversion, e.g. `image.png (1.2 MB)...`
- Progress bar now shows live conversion progress for multiple files
- Real-time updates to output log as each file is processed
- Output area includes a close (❌) button to clear and hide log

### Changed
- Drag-and-drop area resizes better with window and uses larger font
- Improved initial window width and layout proportions
- Disabled drag area while processing to prevent overlap/conflicts

### Fixed
- App no longer freezes during large batch conversions (now runs in a background thread)
- Only shows “Finished!” once at the end instead of multiple messages
- Properly clears and resets progress bar after each conversion batch

## [1.2.0] - 2025-07-06

### Changed
- Rezised window
- Output is now scrollable window with option to close it
- Drag area will not be resized as small. 
- Window is resizable

## [1.0.2] - 2025-07-06

### Changed 
- Updating github build.yml
- Updated README.md
- Updated LICENSE

## [1.0.1] - 2025-07-06

### Changed 
- Updating github build.yml

## [1.0.0] - 2025-07-06

### Added
- Initial push. 