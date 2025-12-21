# Changelog

All notable changes to the CBSE-09 Science Platform will be documented in this file.

## [Unreleased] - 2025-12-21

### Added
- **Smart Navigation Persistence**: Implemented a system to remember the user's last visited chapter across all platform tools.
- **Context-Aware Navbar**: The navigation bar now dynamically updates links to preserve chapter context using URL parameters and `localStorage`.
- **Horizontal Scrolling Navigation**: Added a mobile-optimized, single-row scrolling menu to the header.

### Changed
- **Mobile UI Refinement**: Redesigned the navigation bar for better usability on small screens, including larger touch targets and a compact layout.
- **Improved State Management**: Updated `exam.js` and `download.html` to prioritize the last visited chapter when context is not explicitly provided in the URL.
- **Code Refactoring**: Replaced margin-based spacing with CSS `gap` in the navigation bar for better consistency and cleaner code.

### Fixed
- **Navigation Reset Bug**: Fixed an issue where navigating from the "Track Progress" page would reset the user's chapter context to Chapter 1.
- **Download Page Links**: Corrected redundant and broken navigation logic in `download.html` to align with the centralized menu system.
