(function (namespace, $) {
	"use strict";

    var Web = function () {
		// Create reference to this instance
		var o = this;
		// Initialize app when document is ready
		$(document).ready(function () {
			o.initialize();
		});

	};

    $('#tshockweb_login').on('click', function (e) {
        var username = $("#username").val();
        var password = $("#password").val();
        var url = window.location.protocol + "//" + window.location.host + "/" + "api/login";

        $.ajax({
            type: 'POST',
            url: url,
            data: JSON.stringify({ username: username, password: password }),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                alert("Data: " + JSON.stringify(data));
            }
        });
    });

	namespace.Web = new Web;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
