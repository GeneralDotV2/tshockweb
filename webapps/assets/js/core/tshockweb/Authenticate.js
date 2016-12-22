(function (namespace, $) {
	"use strict";

    var Authenticate = function () {
		// Create reference to this instance
		var o = this;
		// Initialize app when document is ready
		$(document).ready(function () {
			o.initialize();
		});

	};

    // authenticate if token is present and is valid
    if (Cookies.get('tshockweb') != undefined) {
        var tshock = JSON.parse(Cookies.get('tshockweb'));
        $.ajax({
            type: 'POST',
            url: window.location.protocol + "//" + window.location.host + "/" + "api/validation",
            data: JSON.stringify({token: tshock.token}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status != 200) {
                    // redirect to login
                    console.log("Existing token is invalid, redirecting to login!");
                    Cookies.remove('tshockweb');
                    window.location.replace(window.location.protocol + "//" + window.location.host + "/" + "webapps/html/pages/login.html");
                } else {
                    console.log("Token in cookie is valid, continue my lord and savior");
                }
            }
        });
    } else {
        console.log("No cookie available, redirecting to login!");
        window.location.replace(window.location.protocol + "//" + window.location.host + "/" + "webapps/html/pages/login.html");
    }

    // triggers logout
    $('#tshockweb_logout').on('click', function (e) {
        var tshock = JSON.parse(Cookies.get('tshockweb'));
        $.ajax({
            type: 'POST',
            url: window.location.protocol + "//" + window.location.host + "/" + "api/logout",
            data: JSON.stringify({ token: tshock.token}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    console.log("Success: " + data.result);
                    Cookies.remove('tshockweb');
                    window.location.replace(window.location.protocol + "//" + window.location.host + "/" + "webapps/html/pages/login.html");
                } else {
                    alert("Logout failed: " + data.result);
                }
            }
        });
    });

	namespace.Authenticate = new Authenticate;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
