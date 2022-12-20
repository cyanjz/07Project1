'use strict';

chrome.storage.sync.get(['screenshotKey', 'screenshotFunctionality', 'screenshotFileFormat'], function(result) {
	ScreenshotKeyCheck.checked = result.screenshotKey;
	ScreenshotFileFormat.value = result.screenshotFileFormat;
});

ScreenshotKeyCheck.oninput = function() {
	chrome.storage.sync.set({'screenshotKey': this.checked});
};

ScreenshotFileFormat.onchange = function() {
	chrome.storage.sync.set({'screenshotFileFormat': this.value});
}