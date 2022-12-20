// Context Menu에 Customize 추가 및 해당 페이지 새 탭에서 열기
chrome.runtime.onInstalled.addListener(function() {
  chrome.contextMenus.create({
    title: 'Customize',
    id: 'Customize',
    contexts: ['all']
  });
});
chrome.contextMenus.onClicked.addListener(function(info, tab) {
  chrome.tabs.create({  
      url: 'customize.html'
  });
})

// 유튜브 화면에 스크린샷 버튼 추가
chrome.webNavigation.onHistoryStateUpdated.addListener(function(data) {
	chrome.tabs.get(data.tabId, function(tab) {
		chrome.tabs.scripting.executeScirpt(data.tabId, {
      code: 'if (typeof AddScreenshotButton !== "undefined") { AddScreenshotButton(); }', runAt: 'document_start'});
	}); 
}, {url: [{hostSuffix: '.youtube.com'}]});

// 방법1
var dbraw = null;
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.from == 'content_scripts') {
    dbraw = request.data;
    console.log('content에서 data 받아서 dbraw에 저장 완료');
    chrome.tabs.create({  
      url: 'customize.html'
      })
  }
  if (request.from == 'customize') {
    sendResponse(dbraw);
  }
});



// // 방법2
// // 전역 변수
// var dbraw = null;
// chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
//   if (request.from == 'content_scripts') {
//     dbraw = request.data;
//     console.log('content에서 data 받아서 dbraw에 저장 완료');
//     chrome.tabs.create({  
//       url: 'customize.html'},
//       async function(tab) {
//         chrome.tabs.onUpdated.addListener(function abc(tid, tstat, tobj) {
//           if (tstat.status == 'complete') {
//             // tab update 되면 계속 받음 -> abc 함수 없앰
//             chrome.tabs.onUpdated.removeListener(abc);
//             // tobj.id 대신 tid도 가능
//             chrome.tabs.sendMessage(tobj.id, { from: 'background', message: 'This is detection result', data: dbraw });
//           }
//         })
//     });
//   }
// });
