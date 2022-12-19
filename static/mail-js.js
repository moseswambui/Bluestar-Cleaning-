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
			//pay: {
				//required: true,
			//},
			//payp: {
				//required: '#customRadio2[value="Paypal"]:checked',
			//},
			//qrcode: {
				//required: '#customRadio3[value="Google-Pay"]:checked',
			//},
			//tnc: {
			//	required: true,
			//},
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
			//"dp": {
			//	required: "Select dates."
			//},
			//"pay": {
			//	required: "Select atleast one mode of payment."
			//},
			//"payp": {
			//	required: "Paypal address is required.",
			//	email: "Please enter a valid email ID."
			//},
			//"qrcode": {
				//required: "Send us your transaction ID."
			//},
			// "tnc": {
			// 	required: "Accept terms and conditions."
			// },
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
			//var field1 = $('#fname').val();		//taking values from firstname input
			//var field2 = $('#lname').val();
			//var field3 = $('#pnumber').val();
			//var field4 = $('#email').val();
			//var field5 = $('#category').val();
			//var field6 = $('#service').val();
			//var field7 = $('#consultant').val();
			//var field8 = $('#dp').val();
			//var field9 = $('#message1').val();
			//var field10 = $('input[name="pay"]:checked').val();
			//var field11 = $('#payp').val();
			//var field12 = $('#qrcode').val();
			const firstName = document.getElementById('fname')
			const lastName = document.getElementById('lname')
			const emailAddress = document.getElementById('email')
			const phoneNumber = document.getElementById('pnumber')
			const type = document.getElementById('category')
			const category = document.getElementById('service')
			const consultant = document.getElementById('consultant')
			const serviceDate = document.getElementById('dp')
			const pay = document.getElementById('customRadio1')
			
			const csrf = document.getElementsByName('csrfmiddlewaretoken')
			console.log('csrf', csrf[0].value)
			$.ajax({
				url: '',	//linking mail file
				data: {
					"csrfmiddlewaretoken":csrf[0].value,
					"fname": firstName.value,	//pass firstname to mail
					"lname": lastName.value,
					"pnumber": phoneNumber.value,
					"email": emailAddress.value,
					"type": type.value,
					"category": category.value,
					"consultant": consultant.value,
					'dp':serviceDate.value,
					'pay':pay.value,
					//"dp": field8,
					//"message1": field9,
					//"pay": field10,
					//"payp": field11,
					//"qrcode": field12
				},
				type: "POST",
				//dataType: "xml",
				success: function (data) {
					console.log(data)
				},
				error: function(error){
					console.log(error)
				}

			});
			
			//On submit
			alert("Form Submitted!");
			$('#example-form')[0].reset();
			$("#wizard").steps('reset');
			
		}

	});
	$("#category").change(function() {
		var url = $("#example-form").attr("data-categories-url");
		var typeId = $(this).val();
		console.log(typeId)
	
		$.ajax({
		  url: url,
		  data: {
			'type':typeId
		  },
		  success: function(data){
			$("#service").html(data);
		  }
		});
	  });

	  $("#service").change(function() {
		var url = $("#example-form").attr("data-extra-info-url");
		var serviceId = $(this).val();
	
		$.ajax({
		  url: url,
		  data: {
			'service':serviceId
		  },
		  success: function(data){
			$("#title").html(data);
		  }
		});
	  });
	  $("#service").change(function() {
		var url = $("#example-form").attr("data-pricing-url");
		var serviceId = $(this).val();
	
		$.ajax({
		  url: url,
		  data: {
			'service':serviceId
		  },
		  success: function(data){
			$("#pricing").html(data);
		  }
		});
	  });
	  $("#category").change(function() {
		var url = $("#example-form").attr("data-consultants-url");
		var typeId = $(this).val();
	
		$.ajax({
		  url: url,
		  data: {
			'type':typeId
		  },
		  success: function(data){
			$("#consultant").html(data);
		  }
		});
	  });

	  $("#service").change(function() {
		var url = $("#example-form").attr("src","category-image-url");
		var serviceId = $(this).val();
	
		$.ajax({
		  url: url,
		  data: {
			'service':serviceId
		  },
		  success: function(data){
			$("#category-image").html(data);
		  }
		});
	  });




})