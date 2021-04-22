var request = require("request");

function login(name, iggID) {
	var options = {
		method: "POST",
		url: "https://lordsmobile.igg.com/project/seiya/ajax.php?lang=en",
		headers: {
			"sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			"Accept": "application/json, text/plain, */*",
			"X-Requested-With": "XMLHttpRequest",
			"sec-ch-ua-mobile": "?0",
			"User-Agent":
				"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
			"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryh5UFqJ1QDxZpJGtD",
			"Cookie": "lang=en; seiya_iggid=512937877"
		},
		formData: {
			ac: "run_login",
			char_name: name,
			iggid: iggID
		}
	};
	request(options, function (error, response) {
		if (error) throw new Error(error);
		getGift(iggID);
		console.log(response.body);
	});
}

function getGift(iggID) {
	var options = {
		method: "POST",
		url: "https://lordsmobile.igg.com/project/seiya/ajax.php?lang=en",
		headers: {
			"sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			"Accept": "application/json, text/plain, */*",
			"X-Requested-With": "XMLHttpRequest",
			"sec-ch-ua-mobile": "?0",
			"User-Agent":
				"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
			"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryH8MoqjkfxQy3hcFk",
			"Cookie": "lang=en; seiya_iggid=" + iggID
		},
		formData: {
			ac: "run_receive"
		}
	};
	request(options, function (error, response) {
		if (error) throw new Error(error);
		console.log(response.body);
	});
}

login("ShiftySavior", "512937876");
