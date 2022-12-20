var screenshotKey = false;
var screenshotFormat = "png";
var extension = 'png';

function CaptureScreenshot() {

	var appendixTitle = "screenshot." + extension;
	var title;
	var headerEls = document.querySelectorAll("h1.title.ytd-video-primary-info-renderer");

	function SetTitle() {
		if (headerEls.length > 0) {
			title = headerEls[0].innerText.trim();
			return true;
		} else {
			return false;
		}
	}
	
	if (SetTitle() == false) {
		headerEls = document.querySelectorAll("h1.watch-title-container");
		if (SetTitle() == false)
			title = '';
	}

	var player = document.getElementsByClassName("video-stream")[0];

	var time = player.currentTime;

	title += " ";

	let minutes = Math.floor(time / 60)
	time = Math.floor(time - (minutes * 60));
	if (minutes > 60) {
		let hours = Math.floor(minutes / 60)
		minutes -= hours * 60;
		title += hours + "-";
	}

	title += minutes + "-" + time;
	title += " " + appendixTitle;

	var canvas = document.createElement("canvas");
	canvas.width = player.videoWidth;
	canvas.height = player.videoHeight;
	canvas.getContext('2d').drawImage(player, 0, 0, canvas.width, canvas.height);

	var downloadLink = document.createElement("a");
	downloadLink.download = title;

	function DownloadBlob(blob) {
		downloadLink.href = URL.createObjectURL(blob);
	}

	async function ClipboardBlob(blob) {
		// ClipboardItem() : MIME 형식을 키로, Blob을 값으로 사용하여 새 ClipboardItem object 만듦
		const clipboardItemInput = new ClipboardItem({ "image/png": blob });
		await navigator.clipboard.write([clipboardItemInput]);
	}
	canvas.toBlob(async function (blob) {
		await ClipboardBlob(blob);
		screenshotupload(blob);
	}, 'image/png');

	// jsonp, CORS 에러 서버 쪽에서 crossdomain 정책 허용
 
	async function screenshotupload(blob){
		let formData = new FormData();           
    	formData.append("file", blob);
    	
		// let serverUrl = 'http:\/\/localhost:5000\/uploadfile\/';
		// let serverUrl = 'http://54.180.26.244:8000/chair/';
		let serverUrl = 'https://three.sunde41.net/inference';
		// let serverUrl = 'https://inisw72555.duc/kdns.org/bed/';

		var dbraw = null

		await fetch(serverUrl, {
     		method: "POST",
      		body: formData
    	})
			.then(resp => {
				return resp.json();
			})
			.then(data => {
				dbraw = data;
				chrome.runtime.sendMessage({ from: 'content_scripts', message: 'Open customize page', data: dbraw}, function(bm) {
					console.log('content에서 background로 customize page 열어달라고 요청');	
				});
			})
			.catch(error => {
				alert('Detection 실패\n침대 혹은 의자가 있는 화면에서 클릭해주세요',error);
			});
			
		// document.getElementsByClassName('ytp-play-button ytp-button')[0].click()

	}
}


function AddScreenshotButton() {
	var ytpRightControls = document.getElementsByClassName("ytp-right-controls")[0];
	if (ytpRightControls) {
		ytpRightControls.prepend(screenshotButton);
	}
}

var screenshotButton = document.createElement("button");
screenshotButton.className = "screenshotButton ytp-button";
screenshotButton.style.width = "auto";
// screenshotButton.innerHTML = "가구찾기";
screenshotButton.innerHTML = '<img src="https://cdn-icons-png.flaticon.com/128/2590/2590525.png" width="33px" height="33px">';
screenshotButton.style.cssFloat = "left";
screenshotButton.addEventListener('click', CaptureScreenshot);


chrome.storage.sync.get(['screenshotKey', 'screenshotFileFormat'], function(result) {
	screenshotKey = result.screenshotKey;
	if (result.screenshotFileFormat === undefined) {
		screenshotFormat = 'png'
	} else {
		screenshotFormat = result.screenshotFileFormat
	}

	if (screenshotFormat === 'jpeg') {
		extension = 'jpg';
	} else {
		extension = screenshotFormat;
	}
});

document.addEventListener('keydown', function(e) {
	if (document.activeElement.contentEditable === 'true' || document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA' || document.activeElement.contentEditable === 'plaintext')
		return true;

	if (screenshotKey && e.key === 'p') {
		CaptureScreenshot();
		e.preventDefault();
		return false;
	}
});

AddScreenshotButton();

