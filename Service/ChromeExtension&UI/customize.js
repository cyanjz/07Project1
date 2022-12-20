// 방법1
chrome.runtime.sendMessage({ from: 'customize', message: 'Send detection result' }, function(response) {
    console.log('customize에서 background로 detection 결과 달라고 요청');
    dbraw = response;
    dbraw = dbraw.result[0].items
    dbrawManage(dbraw);
    makeProdList(products);
    initScreen(); 
});

// // 방법2
// chrome.runtime.sendMessage({ from: 'customize', message: 'Send detection result' }, function(bm) {
//     console.log('customize에서 background로 detection 결과 달라고 요청');	
// });
// chrome.runtime.onMessage.addListener(async function(request, sender, sendResponse) {
//     dbraw = request.data
//     dbrawManage(dbraw);
// });


// 가구목록

var dbraw = null
var customizeResult = {}
var color = null
var material = null

var rawColorList = new Array;
var totalColorList = new Array;

var rawMaterialList = new Array;
var totalMaterialList = new Array;

var products = []

// 스크린샷 전송 후 서버에서 받은 db 데이터 처리
function dbrawManage(dbraw) {

    if (dbraw.length > 0) {
        furniture = Number(dbraw[0].가구);
        customizeResult.대분류 = furniture;
    }
    
    for (let i=0; i<dbraw.length; i++) {
        brandName = dbraw[i].브랜드;
        imgUrl = dbraw[i].imgurl;
        prodName = dbraw[i].name;
        price = dbraw[i].price;
        prodUrl = dbraw[i].url;
        size = dbraw[i].사이즈;

        products.push({'brandName': brandName, 'imgUrl': imgUrl, 'prodName': prodName, 'price': price, 'prodUrl': prodUrl, 'size': size })

        rawColorList.push(dbraw[i].색상태그.split('/'));
        for (let j=0; j<rawColorList.length; j++) {
            totalColorList = totalColorList.concat(rawColorList[j])
        }
        totalColorList = [...new Set(totalColorList)];
        color = totalColorList;
        customizeResult.색상태그 = color


        rawMaterialList.push(dbraw[i].주요재질.split('/'));
        for (let k=0; k<rawMaterialList.length; k++) {
            totalMaterialList = totalMaterialList.concat(rawMaterialList[k]);
        }
        totalMaterialList = [...new Set(totalMaterialList)];
        material = totalMaterialList;
        customizeResult.주요재질 = material
    }


    switch(furniture) {
        case 0:
            customizeResult.모션 = dbraw[0].모션;
            customizeResult.저상 = dbraw[0].저상;
            customizeResult.수납 =  dbraw[0].수납;
            customizeResult.헤드 = dbraw[0].헤드;

            BedorChairButton[0].checked = true;

            if (dbraw[0].모션 == 1) {
                document.querySelectorAll('input[name=BedClasstag]')[0].checked = true;
            } else {
                document.querySelectorAll('input[name=BedClasstag]')[0].checked = false;
            }
            if (dbraw[0].저상 == 1) {
                document.querySelectorAll('input[name=BedClasstag]')[1].checked = true;
            } else {
                document.querySelectorAll('input[name=BedClasstag]')[1].checked = false;
            }
            if (dbraw[0].수납 == 1) {
                document.querySelectorAll('input[name=BedClasstag]')[2].checked = true;
            } else {
                document.querySelectorAll('input[name=BedClasstag]')[2].checked = false;
            }
            if (dbraw[0].헤드 == 1) {
                document.querySelectorAll('input[name=BedClasstag]')[3].checked = true;
            } else {
                document.querySelectorAll('input[name=BedClasstag]')[3].checked = false;
            }

            BedColorTag.forEach(el => {for (let i=0; i<color.length; i++) {
                if (color.includes(el.getAttribute('value')) == true) {
                    el.checked = true;
                    el.classList.add('active');
                    el.style.outline = '3px solid white';
                } else {
                    el.checked = false;
                    el.classList.remove('active');
                    el.style.outline = 'none';
                }
            }
            })

            BedMaterialTag.forEach(el => {for (let i=0; i<material.length; i++) {
                if (material.includes(el.getAttribute('value')) == true) {
                    el.checked = true;
                    el.classList.add('active');
                } else {
                    el.checked = false;
                    el.classList.remove('active');
                }
            }
            })

            break;
            
        case 1:
            customizeResult.팔걸이 = dbraw[0].팔걸이;
            customizeResult.등받이 = dbraw[0].등받이;
            customizeResult.다리형태 = dbraw[0].다리형태;

            BedorChairButton[1].checked = true;

            if (dbraw[0].팔걸이 == 1) {
                document.querySelectorAll('input[name=ChairClasstag]')[0].checked = true;
            } else {
                document.querySelectorAll('input[name=ChairClasstag]')[0].checked = false;
            }
            if (dbraw[0].등받이 == 1) {
                document.querySelectorAll('input[name=ChairClasstag]')[1].checked = true;
            } else {
                document.querySelectorAll('input[name=ChairClasstag]')[1].checked = false;
            }

            
            ChairColorTag.forEach(el => {for (let i=0; i<color.length; i++) {
                if (color.includes(el.getAttribute('value')) == true) {
                    el.checked = true;
                    el.classList.add('active');
                    el.style.outline = '3px solid white'
                } else {
                    el.checked = false;
                    el.classList.remove('active');
                    el.style.outline = 'none'
                }
            }
            })

            ChairMaterialTag.forEach(el => {for (let i=0; i<material.length; i++) {
                if (material.includes(el.getAttribute('value')) == true) {
                    el.checked = true;
                    el.classList.add('active');
                } else {
                    el.checked = false;
                    el.classList.remove('active');
                }
            }
            })

            break;
    }

    CommonMaterialTag.forEach(el => {for (let i=0; i<material.length; i++) {
        if (material.includes(el.getAttribute('value')) == true) {
            el.checked = true;
            el.classList.add('active');
        } else {
            el.checked = false;
            el.classList.remove('active');
        }
    }
    }) 
}

function makeProdList(products) {
    const template = document.getElementById("product_list");
    const elements = new Set();

    for (let i=0; i<products.length; i++) {
        const element = template.content.firstElementChild.cloneNode(true);
        element.querySelector(".img_area > a").href = products[i].prodUrl;
        element.querySelector(".img_area > a > img").src = products[i].imgUrl;
        element.querySelector(".brand_name").textContent = products[i].brandName;
        element.querySelector(".info_area > .prod_name > a").textContent = products[i].prodName;
        element.querySelector(".info_area > .prod_name > a").href = products[i].prodUrl;
        // element.querySelector(".prod_box > button").addEventListener('click', function() {
        //     window.open(new URL(products[i].prodUrl),"_blank");
        // })
        element.querySelector(".price").textContent = products[i].price+'원';
        element.querySelector(".prod_size").textContent = products[i].size;  
        elements.add(element);
    }
    document.querySelector("ul").append(...elements);
}


// 정렬
const BtnContainer = document.querySelector(".shop__buttonContainer");
const BasicBtn = document.querySelector(".shop__basicBtn");
const LowPriceBtn = document.querySelector(".shop__lowPriceBtn");
const HighPriceBtn = document.querySelector(".shop__highPriceBtn");
const ABCBtn = document.querySelector(".shop__AbcBtn");

// 오름차순 -> 낮은 가격순
function ProductSortUp() {
    for (let i=0; i<products.length;i++) {
        document.querySelector('ul').removeChild(document.querySelector('li'))
    }
    
    const NewProducts = [...products];
    NewProducts.sort(function (a, b) {
        return Number(a.price.split(',').join("")) - (b.price.split(',').join(""));
    });
    makeProdList(NewProducts)
}
  
// 내림차순 -> 높은 가격순
function ProductSortDown() {
    for (let i=0; i<products.length;i++) {
        document.querySelector('ul').removeChild(document.querySelector('li'))
    }

    const NewProducts = [...products];
    NewProducts.sort(function (a, b) {
        return Number(b.price.split(',').join("")) - (a.price.split(',').join(""));
    });
    makeProdList(NewProducts)
}

// 브랜드순
function BrandABC() {
    for (let i=0; i<products.length;i++) {
        document.querySelector('ul').removeChild(document.querySelector('li'))
    }

    const NewProducts = [...products];
    NewProducts.sort(function (a, b) {
        if (a.brandName < b.brandName) return -1;
        else if (a.brandName == b.brandName) return 0;
        else return 1;
    });
    makeProdList(NewProducts)
}

// 기본순
function ProductBasic() {
    for (let i=0; i<products.length;i++) {
        document.querySelector('ul').removeChild(document.querySelector('li'))
    }
    makeProdList(products)
}

// 정렬 버튼 동작
BtnContainer.addEventListener("click", (e) => {
    if (e.target == LowPriceBtn) {
        ProductSortUp();
    } else if (e.target == HighPriceBtn) {
        ProductSortDown();
    } else if (e.target == ABCBtn) {
        BrandABC();
    } else if (e.target == BasicBtn) {
        ProductBasic();
    } else {
        return;
    }
});
  


// dom 내 변수
var BedorChairButton=document.getElementsByName('BedChairButtonsCheck');
var BedButton = document.getElementById('BedclassButtonsCheck');
var ChairButton = document.getElementById('ChairclassButtonsCheck');

var onlyBedMaterial = document.getElementsByClassName('bedmaterial')[0];
var onlyChairMateiral = document.getElementsByClassName('chairmaterial')[0];

var BedColorPalette = document.getElementsByClassName('BedColors')[0];
var ChairColorPalette = document.getElementsByClassName('ChairColors')[0];

var BedColorTag = document.getElementsByName('Bedcolor');
var ChairColorTag = document.getElementsByName('Chaircolor');

var CommonMaterialTag = document.getElementsByName('commonM');
var BedMaterialTag = document.getElementsByName('bedM');
var ChairMaterialTag = document.getElementsByName('chairM');

var regexp = /background-color: (#.+);/;



// 화면 구성
function initScreen() {
    // 가구 대분류
    if (BedorChairButton[0].checked == true) {

        BedButton.style.display = "block";
        ChairButton.style.display = "none";

        BedColorPalette.style.display='flex'
        ChairColorPalette.style.display='none'

        onlyBedMaterial.style.display='block'
        onlyChairMateiral.style.display='none'

        BedClass()

    } else if (BedorChairButton[1].checked == true) {

        BedButton.style.display = "none";
        ChairButton.style.display = "block";

        BedColorPalette.style.display ='none'
        ChairColorPalette.style.display ='flex'

        onlyBedMaterial.style.display ='none'
        onlyChairMateiral.style.display ='block'

        ChairClass()

    } else {
        BedButton.style.display = "none";
        ChairButton.style.display = "none";
        customizeResult.대분류 = "";
    }
}


// 침대 관련 dict 삭제
function BedDelete() {
    delete customizeResult.모션;
    delete customizeResult.저상;
    delete customizeResult.수납;
    delete customizeResult.헤드;
    document.getElementsByName('BedClasstag').forEach(function(input) {
        input.checked = false;
    })      
    BedColorTag.forEach(function(el) {
        el.classList.remove('active');
        el.style.outline = 'none';
    })
    BedMaterialTag.forEach(el => {for (let i=0; i<material.length; i++) {
        el.checked = false;
        el.classList.remove('active');
    }
    })
}

// 의자 관련 dict 삭제
function ChairDelete() {
    delete customizeResult.팔걸이;
    delete customizeResult.등받이;
    delete customizeResult.다리형태;
    document.getElementsByName('ChairClasstag').forEach(function(input) {
         input.checked = false
    })  
    document.getElementsByName('ChairLegClasstag').forEach(function(input) {
        input.checked = false;
    })
    ChairColorTag.forEach(function(el) {
        el.classList.remove('active');
        el.style.outline = 'none';
    })
    ChairMaterialTag.forEach(el => {for (let i=0; i<material.length; i++) {
        el.checked = false;
        el.classList.remove('active');
    }
    })
}



// 침대 class
function BedClass() {
    ChairDelete();

    customizeResult.대분류 = 0;

    document.getElementsByName('BedClasstag').forEach(function(input) {
        if (input.checked == true) {
            customizeResult[input.value] = 1;
        } else {
            customizeResult[input.value] = 0;
        }
    })                

    if (customizeResult.색상태그) {
        ChairColorTag.forEach(el => {for (let i=0; i<customizeResult.색상태그.length; i++) {
            if (customizeResult.색상태그[i] == el.getAttribute('value')) {
                customizeResult.색상태그.splice(i,1);
                i--;
            }
        }
        })
    }

    if (customizeResult.주요재질) {
        ChairMaterialTag.forEach(el => {for (let i=0; i<customizeResult.주요재질.length; i++) {
            if (customizeResult.주요재질[i] == el.getAttribute('value')) {
                customizeResult.주요재질.splice(i,1);
                i--;
            }
        }
        })
    }    
}

// 의자 class
function ChairClass() {
    BedDelete()

    customizeResult.대분류 = 1;

    document.getElementsByName('ChairClasstag').forEach(function(input) {
        if (input.checked == true) {
            customizeResult[input.value] = 1;
        } else {
            customizeResult[input.value] = 0;
        }
    })
    
    const regexp1 = /ChairLeg(\d)/;
    document.getElementsByName('ChairLegClasstag').forEach(function(input) {
        if (input.checked == true) {
            customizeResult.다리형태 = Number(input.value.match(regexp1)[1]);
        }
    })

    switch(customizeResult.다리형태) {
        case 0:
            document.querySelectorAll('input[name=ChairLegClasstag]')[0].checked = true;
            break;
        case 1:
            document.querySelectorAll('input[name=ChairLegClasstag]')[1].checked = true;
            break;
        case 2:
            document.querySelectorAll('input[name=ChairLegClasstag]')[2].checked = true;
            break;
        case 3:
            document.querySelectorAll('input[name=ChairLegClasstag]')[3].checked = true;
            break;
        case 4:
            document.querySelectorAll('input[name=ChairLegClasstag]')[4].checked = true;
            break;
    }


    if (customizeResult.색상태그) {
        BedColorTag.forEach(el => {for (let i=0; i<customizeResult.색상태그.length; i++) {
            if (customizeResult.색상태그[i] == el.getAttribute('value')) {
                customizeResult.색상태그.splice(i,1);
                i--;
            }
        }
        })
    }
 
    if (customizeResult.주요재질) {
        BedMaterialTag.forEach(el => {for (let i=0; i<customizeResult.주요재질.length; i++) {
            if (customizeResult.주요재질[i] == el.getAttribute('value')) {
                customizeResult.주요재질.splice(i,1);
                i--;
            }
        }
        })
    }
}



 // 침대 색상
document.querySelectorAll('div[name=Bedcolor]').forEach(function(div) {
    div.addEventListener('click', function() {
        if (div.classList.contains('active')) {
            div.classList.remove('active')
            div.style.outline = 'none';
        } else {
            div.classList.add('active');
            div.style.outline = '3px solid white';
        } let p = new Set;
        document.querySelectorAll('div.active').forEach(function(div) {p.add(div.attributes[3].value);
        });
        customizeResult.색상태그 = [...p];
        if (customizeResult.색상태그) {
            ChairColorTag.forEach(el => {for (let i=0; i<customizeResult.색상태그.length; i++) {
                if (customizeResult.색상태그[i] == el.getAttribute('value')) {
                    customizeResult.색상태그.splice(i,1);
                    i--;
                }
            }
            })
        }
    })
});

// 의자 색상
document.querySelectorAll('div[name=Chaircolor]').forEach(function(div) {
    div.addEventListener('click', function() {
        if (div.classList.contains('active')) {
            div.classList.remove('active')
            div.style.outline = 'none';
        } else {
            div.classList.add('active');
            div.style.outline = '3px solid white';
        } let p = new Set;
        document.querySelectorAll('div.active').forEach(function(div) {p.add(div.attributes[3].value);
        });
        customizeResult.색상태그 = [...p];

        if (customizeResult.색상태그) {
            BedColorTag.forEach(el => {for (let i=0; i<customizeResult.색상태그.length; i++) {
                if (customizeResult.색상태그[i] == el.getAttribute('value')) {
                    customizeResult.색상태그.splice(i,1);
                    i--;
                }
            }
            })
        }        
    })
});


// 침대 재질
document.querySelectorAll('input[name=bedM]').forEach(function(input) {
    input.addEventListener('click', function() {
        if (input.classList.contains('active')) {
            input.classList.remove('active')
        } else {
            input.classList.add('active');
        } let p = new Set;
        document.querySelectorAll('input.active').forEach(function(input) {p.add(input.value);
        });
        customizeResult.주요재질 = [...p];

        if (customizeResult.주요재질) {
            ChairMaterialTag.forEach(el => {for (let i=0; i<customizeResult.주요재질.length; i++) {
                if (customizeResult.주요재질[i] == el.getAttribute('value')) {
                    customizeResult.주요재질.splice(i,1);
                    i--;
                }
            }
            })
        }  
    })
});

// 의자 재질
document.querySelectorAll('input[name=chairM]').forEach(function(input) {
    input.addEventListener('click', function() {
        if (input.classList.contains('active')) {
            input.classList.remove('active')
        } else {
            input.classList.add('active');
        } let p = new Set;
        document.querySelectorAll('input.active').forEach(function(input) {p.add(input.value);
        });
        customizeResult.주요재질 = [...p];

        if (customizeResult.주요재질) {
            BedMaterialTag.forEach(el => {for (let i=0; i<customizeResult.주요재질.length; i++) {
                if (customizeResult.주요재질[i] == el.getAttribute('value')) {
                    customizeResult.주요재질.splice(i,1);
                    i--;
                }
            }
            })
        }  
    })
});

// 공통 재질
document.querySelectorAll('input[name=commonM]').forEach(function(input) {
    input.addEventListener('click', function() {
        if (input.classList.contains('active')) {
            input.classList.remove('active')
        } else {
            input.classList.add('active');
        } let p = new Set;
        document.querySelectorAll('input.active').forEach(function(input) {p.add(input.value);
        });
        customizeResult.주요재질 = [...p];
    })
});






//customize 후 서버로 데이터 전달
async function custom2server(customizeResult) {
    // let serverUrl = 'http:\/\/localhost:50000\/uploadfile\/';
    // let serverUrl = 'http://54.180.26.244:8000/items/';
    // let serverUrl = 'https://three.sunde41.net/items';
    let serverUrl = 'https://three.sunde41.net/edittags';

    // let serverUrl = 'https://inisw72555.duckdns.org/items/';


    await fetch(serverUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(customizeResult)
    })
        .then(resp => {
            return resp.json();
        })
        .then(data => {
            dbraw = data.result[0].items;   

            if (document.querySelector('li')) {
                for (let i=0; i<products.length;i++) {
                    document.querySelector('ul').removeChild(document.querySelector('li'))
                }
            }

            products = []; 

            if (dbraw.length > 0) {
                dbrawManage1(dbraw);
            }
           
        })
        // .catch(error => {
        //     alert('죄송합니다\n해당 조건을 만족하는 가구가 없습니다\n');
        // });
}


// // 검색 버튼
// document.querySelector('button[name=search]').addEventListener('click', function() {
//     custom2server(customizeResult)
// });


function reset() {    

    // if (products.length > 0) {
    //     for (let i=0; i<products.length;i++) {
    //         document.querySelector('ul').removeChild(document.querySelector('li'))
    //     }
    // }

    if (document.querySelector('li')) {
        for (let i=0; i<products.length;i++) {
            document.querySelector('ul').removeChild(document.querySelector('li'))
        }
    }

    customizeResult.색상태그 = [];
    customizeResult.주요재질 = [];
    
    if(BedorChairButton[0].checked == true) {
        ChairDelete();
        customizeResult.모션 = 0;
        customizeResult.저상 = 0;
        customizeResult.수납 = 0;
        customizeResult.헤드 = 0;
    } else {
        BedDelete();
        customizeResult.팔걸이 = 0;
        customizeResult.등받이 = 0;
        customizeResult.다리형태 = null;
    }

    document.querySelectorAll('input[type=checkbox]').forEach(function(el) {
        el.checked = false;
    })

    document.querySelectorAll('input[name=ChairLegClasstag]').forEach(function(el) {
        el.checked = false;
    })

    BedColorTag.forEach(function(el) {
        el.classList.remove('active');
        el.style.outline = 'none';
    })

    ChairColorTag.forEach(function(el) {
        el.classList.remove('active');
        el.style.outline = 'none';
    })

    CommonMaterialTag.forEach(el => {for (let i=0; i<material.length; i++) {
        el.checked = false;
        el.classList.remove('active');
    }
    })

    BedMaterialTag.forEach(el => {for (let i=0; i<material.length; i++) {
        el.checked = false;
        el.classList.remove('active');
    }
    })

    ChairMaterialTag.forEach(el => {for (let i=0; i<material.length; i++) {
        el.checked = false;
        el.classList.remove('active');
    }
    })
}

// 초기화 버튼
document.querySelector('button[name=reset]').addEventListener('click', function() {
    reset();
});

document.querySelectorAll('input[name=BedChairButtonsCheck]').forEach(function(input) {
    input.addEventListener('change', function() {
        reset();
        initScreen();
    })
})


function dbrawManage1(dbraw) {

    if (dbraw[0].가구) {
        furniture = Number(dbraw[0].가구);
        customizeResult.대분류 = furniture;
    }
    
    for (let i=0; i<dbraw.length; i++) {
        brandName = dbraw[i].브랜드;
        imgUrl = dbraw[i].imgurl;
        prodName = dbraw[i].name;
        price = dbraw[i].price;
        prodUrl = dbraw[i].url;
        size = dbraw[i].사이즈;

        products.push({'brandName': brandName, 'imgUrl': imgUrl, 'prodName': prodName, 'price': price, 'prodUrl': prodUrl, 'size': size })
    }

    makeProdList(products);
    initScreen();  
}



document.querySelectorAll('input[name=ChairLegClasstag]').forEach(function(input) {
    input.addEventListener('change', function() {
        initScreen();
        custom2server(customizeResult);
    })
})
document.querySelectorAll('input[type=checkbox]').forEach(function(input) {
    input.addEventListener('change', function() {
        initScreen();
        custom2server(customizeResult);
    })
})
document.querySelectorAll('div[name=Bedcolor]').forEach(function(div) {
    div.addEventListener('click', function() {
    custom2server(customizeResult);
    })
})
document.querySelectorAll('div[name=Chaircolor]').forEach(function(div) {
    div.addEventListener('click', function() {
    custom2server(customizeResult);
    })
})


