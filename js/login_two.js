var maxbigbox = document.getElementsByClassName('maxbox')
var num = 1
var backgroundbox = document.getElementsByClassName('background')
var background_cord = document.getElementsByClassName('cord')
backgroundbox[0].addEventListener('mousedown', fn_one)
function fn_one() {
    background_cord[0].style.top = '-7px'
    backgroundbox[0].style.top = '150px'
    backgroundbox[0].addEventListener('mouseup', fn)
    if (background_cord[0].style.top === '-7px' && backgroundbox[0].style.top === '150px') {
        maxbigbox[0].addEventListener('mouseup', fn1)
    }
}
function fn1() {
    background_cord[0].style.top = '-37px'
    backgroundbox[0].style.top = '120px'
    if (num === 0) {
        console.log('点击了');
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscape.jpg)';
        num += 1;
    } else if (num === 1) {
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscapetwo.jpg)';
        num += 1
    } else if (num === 2) {
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscapethree.jpg)';
        num += 1
    } else {
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscapefour.jpg)';
        num = 0
    }
    maxbigbox[0].removeEventListener('mouseup', fn1)

}


function fn() {
    background_cord[0].style.top = '-37px'
    backgroundbox[0].style.top = '120px'
    if (num === 0) {
        console.log('点击了');
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscape.jpg)';
        num += 1;
    } else if (num === 1) {
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscapetwo.jpg)';
        num += 1
    } else if (num === 2) {
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscapethree.jpg)';
        num += 1
    } else {
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscapefour.jpg)';
        num = 0
    }
    maxbigbox[0].removeEventListener('mouseup', fn1)

}

background_cord[0].addEventListener('mousedown', function () {
    background_cord[0].style.top = '-7px'
    backgroundbox[0].style.top = '150px'
})
background_cord[0].addEventListener('mouseup', function () {
    background_cord[0].style.top = '-37px'
    backgroundbox[0].style.top = '120px'
    if (num === 0) {
        console.log('点击了');
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscape.jpg)';
        num += 1;
    } else if (num === 1) {
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscapetwo.jpg)';
        num += 1
    } else if (num === 2) {
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscapethree.jpg)';
        num += 1
    } else {
        maxbigbox[0].style.backgroundImage = 'url(images/login_images/landscapefour.jpg)';
        num = 0
    }
});

var login1 = document.querySelector('.box .form .inputBx input[type="submit"]');
login1.addEventListener('click', function () {
    console.log('点击成功');
    // location.assign('index.html');
});