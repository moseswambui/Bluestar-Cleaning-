// JavaScript Document

$(document).ready(function () {
	"use strict"

	//varibale for disabling sundays
	var disabledDays = [0];

	//DATE PICKER
	$('#dp').datepicker({
		
		//options for date picker
		language: 'en',
		multipleDates: 3,
		multipleDatesSeparator: '  ,  ',
		timepicker: true,
		dateTimeSeparator: '-',
		clearButton: true,
		
		//set min and max time for booking 9=9:00AM, 17=5:59PM
		minHours: 9,
		maxHours: 17,

		// Now can select only dates, which goes after today
		minDate: new Date(),

		// Make Sunday disabled
		onRenderCell: function (date, cellType) {
			if (cellType == 'day') {
				var day = date.getDay(),
					isDisabled = disabledDays.indexOf(day) != -1;

				return {
					disabled: isDisabled
				}
			}
		},
	});


	//SELECT2
	$('#category, #service, #consultant').select2();


	//RADIO BUTTON DIV SELECT
	$('input[type="radio"]').click(function () {
		var inputValue = $(this).attr("value");
		var targetBox = $("." + inputValue);
		$(".box").not(targetBox).hide();
		$(targetBox).show();
	});


	//FETCH DATA ON REVIEW SECTION - STEP-4
	$('#fname').change(function () {
		$('#summaryfname').text($(this).val());
	});

	$('#lname').change(function () {
		$('#summarylname').text($(this).val());
	});

	$('#pnumber').change(function () {
		$('#summarypnumber').text($(this).val());
	});

	$('#email').change(function () {
		$('#summaryemail').text($(this).val());
	});

	$('#category').change(function () {
		$('#summarycategory').text($(this).val());
	});

	$('#service').change(function () {
		$('#summaryservice').text($(this).val());
	});

	$('#consultant').change(function () {
		$('#summaryconsultant, #xyz').text($(this).val());
	});

	$('#message1').change(function () {
		$('#summarymessage').text($(this).val());
	});

	$('input[name="pay"]').change(function () {
		$('#summarypayment').text($(this).val());
	});


//////CASCASING SELECT START//////

	//ko binding handler
	ko.bindingHandlers.select2 = {
		init: function (element, valueAccessor) {

			var options = ko.toJS(valueAccessor()) || {};
			setTimeout(function () {
				$(element).select2(options);
			}, 0);

			ko.utils.domNodeDisposal.addDisposeCallback(element, function () {
				$(element).select2('destroy');
			});
		},
		update: function (element) {
			$(element).trigger('change');
		}
	};

	//Define our options model
	var cascadingOption = function (data) {
		var self = this;
		self.data = self;
		self.text = data.text;
		self.childOptions = data.childOptions;
		console.log(self);
	}

	//fill our models with example data
	function buildData() {
		var uomBachelor = new cascadingOption({
			text: 'Sofa Cleaning',
			childOptions: [
				new cascadingOption({
					text: 'Joseph Rio (220$)'
				}),
				new cascadingOption({
					text: 'John Mill (220$)'
				})
			]
		});

		var uomMaster = new cascadingOption({
			text: 'Carpet Cleaning',
			childOptions: [
				new cascadingOption({
					text: 'Sandy Andrea (220$)'
				}),
				new cascadingOption({
					text: 'Meghan Kate (220$)'
				})
			]
		});

		var uom = new cascadingOption({
			text: 'Upholstery Cleaning ',
			childOptions: [uomBachelor, uomMaster]
		});

		var mdx = new cascadingOption({
			text: 'Office Cleaning',
			childOptions: [
				new cascadingOption({
					text: 'Occupied Office',
					childOptions: [{
							text: 'Oli Ye (150$)'
						},
						{
							text: 'Peg Legge (150$)'
						},
					]
				}),
				new cascadingOption({
					text: 'After Renovation',
					childOptions: [{
							text: 'Dr. Cierra Vega (220$)'
						},
						{
							text: 'Dr. Kierra Gentry (220$)'
						}
					]
				}),
				new cascadingOption({
					text: 'New Office',
					childOptions: [{
							text: 'Thomas Crane (220$)'
						},
						{
							text: 'Miranda Shaffer (220$)'
						},
						{
							text: 'Alvaro Mcgee (220$)'
						}
					]
				})
			]
		});


		// Add this part if you need to add more options ---- START
		
		
		var h2 = new cascadingOption({
			text: 'House Cleaning',
			childOptions: [
				new cascadingOption({
					text: 'Post Construction',
					childOptions: [{
							text: 'Aida Bugg (150$)'
						},
						{
							text: 'Peg Legge (150$)'
						},
					]
				}),
				new cascadingOption({
					text: 'After Renovation',
					childOptions: [{
							text: 'Miranda Shaffer (220$)'
						},
						{
							text: 'Allie Grater (220$)'
						},
						{
							text: 'Olive Yew (220$)'
						},
					]
				})
			]
		});


		// END

		//return values
		return [uom, mdx, h2];

	}

	var viewModel = {
		togaMakers: buildData(),
		selectedCategory: ko.observable(),
		selectedService: ko.observable(),
		selectedConsultant: ko.observable()
	};

	viewModel.togaServices = ko.computed(function () {
		if (viewModel.selectedCategory()) {
			var make = ko.utils.arrayFirst(viewModel.togaMakers, function (item) {
				return item.text === viewModel.selectedCategory();
			});
			return make.childOptions;
		}
	});

	viewModel.togaConsultants = ko.computed(function () {
		if (viewModel.selectedService()) {
			var type = ko.utils.arrayFirst(viewModel.togaServices(), function (item) {
				return item.text === viewModel.selectedService();
				console.log("Answer:" + item);
			});
			return type.childOptions;
		}
	});

	ko.applyBindings(viewModel);

//////CASCASING SELECT END//////

});	//DOCUMENT END//