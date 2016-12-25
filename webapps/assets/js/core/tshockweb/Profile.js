(function (namespace, $) {
	"use strict";

    var Profile = function () {
		// Create reference to this instance
		var o = this;
		// Initialize app when document is ready
		$(document).ready(function () {
			o.initialize();
		});

	};

    console.log("Starting collecting data for dashboard");
    var tshock = JSON.parse(Cookies.get('tshockweb'));
    var base_url = window.location.protocol + "//" + window.location.host + "/";
    toastr.warning('This name is already added', '');
	namespace.Profile = new Profile;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
