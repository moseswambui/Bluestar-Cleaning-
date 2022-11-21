// JavaScript Document
//Wizard Init
//FOR WIZARD AND VALIDATIONS
$(document).ready(function () {
	'use strict';
	//defining form
	var form = $("#example-form").show();

	form.validate({
		ignore: ".ignore",
		focusInvalid: true,

		errorPlacement: function errorPlacement(error, element) {
			return false
		},

		//error message block
		showErrors: function (errorMap, errorList) {
			$("#wizard").find("input").each(function () {
				$(this).removeClass("error");
			});
			$(".errorblock").html("");
			if (errorList.length) {
				$(".errorblock").html(errorList[0]['message']);
				$(errorList[0]['element']).addClass("error");
			}
		},

		//rules for validation
		rules: {
			confirm: {
				equalTo: "#password"
			},
			pay: {
				required: true,
			},
			payp: {
				required: '#customRadio2[value="Paypal"]:checked',
			},
			qrcode: {
				required: '#customRadio3[value="Google-Pay"]:checked',
			},
			tnc: {
				required: true,
			},
		},

		//message for validation
		messages: {
			"fname": {
				required: "Firstname required."
			},
			"lname": {
				required: "Lastname required."
			},
			"pnumber": {
				required: "Phone No. required.",
			},
			"email": {
				required: "Email is required.",
				email: "Invalid email."
			},
			"category": {
				required: "Select category.",
			},
			"service": {
				required: "Select service.",
			},
			"consultant": {
				required: "Select consultant."
			},
			"dp": {
				required: "Select dates."
			},
			"pay": {
				required: "Select atleast one mode of payment."
			},
			"payp": {
				required: "Paypal address is required.",
				email: "Please enter a valid email ID."
			},
			"qrcode": {
				required: "Send us your transaction ID."
			},
			"tnc": {
				required: "Accept terms and conditions."
			},
		},


	});

	//wizard steps
	form.children("div").steps({
		headerTag: "h3",
		bodyTag: "section",
		transitionEffect: "none",
		titleTemplate: '#title#',
		
		//labels
		labels: {
			finish: "Submit",
			next: "Next",
			previous: "Back",
		},
		
		//while changing step
		onStepChanging: function (event, currentIndex, newIndex) {

			// Allways allow previous action even if the current form is not valid!
			if (currentIndex > newIndex) {
				return true;
			}

			form.validate().settings.ignore = ":disabled,:hidden";
			return form.valid();
		},
		
		//while finishing
		onFinishing: function (event, currentIndex) {
			return form.valid();
		},
		
		//when finished
		onFinished: function (event, currentIndex) {
			
			$("#example-form").on("submit", function (e) {
				//send data through ajax
				e.preventDefault();
				return false;
			});

			//Ajax Example
			var field1 = $('#fname').val();		//taking values from firstname input
			var field2 = $('#lname').val();
			var field3 = $('#pnumber').val();
			var field4 = $('#email').val();
			var field5 = $('#category').val();
			var field6 = $('#service').val();
			var field7 = $('#consultant').val();
			var field8 = $('#dp').val();
			var field9 = $('#message1').val();
			var field10 = $('input[name="pay"]:checked').val();
			var field11 = $('#payp').val();
			var field12 = $('#qrcode').val();

			$.ajax({
				url: '{% url index %}',	//linking mail file
				data: {
					"fname": field1,	//pass firstname to mail
					"lname": field2,
					"pnumber": field3,
					"email": field4,
					"category": field5,
					"service": field6,
					"consultant": field7,
					"dp": field8,
					"message1": field9,
					"pay": field10,
					"payp": field11,
					"qrcode": field12
				},
				type: "POST",
				dataType: "xml",
				success: function (data) {},

			});
			
			//On submit
			alert("Form Submitted!");
			$('#example-form')[0].reset();
			$("#wizard").steps('reset');
			
		}

	});


})