var login = document.querySelectorAll('.login_module');
login[0].addEventListener('click', function () {
    location.assign('login/user/');
});
login[1].addEventListener('click', function () {
    location.assign('login/admin/');
});
login[2].addEventListener('click', function () {
    location.assign('login/register/');
});