/* Arquivo definido para armazenar as configs destinadas 
   ao plot dos gráficos da plataforma. */

$("#consumoTotalMes").ready( function() {
	var ctx = document.getElementById("consumoTotalMes").getContext('2d');

	var dataToPlot = []; labelsToPlot = [];

	for(var i = 0; i < newDataMes.length; i++) {
		dataToPlot.push(newDataMes[i].split(' ')[1]);
		labelsToPlot.push("Dia " + newDataMes[i].split(' ')[0]);
    }

	var myChart = new Chart(ctx, {
        type: 'line',
        data: {
			labels: labelsToPlot,
			datasets: [{
				label: 'Consumo dos últimos 30 dias',
				steppedLine: false,
				data: dataToPlot,
				borderColor: 'rgba(75, 192, 192, 1)',
				fill: false,
			}]
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
		    scales: {
		        yAxes: [{
		            ticks: {
		                beginAtZero:true
		            }
		        }]
		    }
		}
	});
});

$("#consumoTotalSemana").ready( function() {
	var ctx = document.getElementById("consumoTotalSemana").getContext('2d');

	var dataToPlot = []; labelsToPlot = [];

	for(var i = 0; i < newDataSemana.length; i++) {
		dataToPlot.push(newDataSemana[i].split(' ')[1]);
		labelsToPlot.push(newDataSemana[i].split(' ')[0]);
    }

	var myChart = new Chart(ctx, {
        type: 'line',
        data: {
			labels: labelsToPlot,
			datasets: [{
				label: 'Consumo dos últimos 7 dias',
				steppedLine: false,
				data: dataToPlot,
				borderColor: 'rgba(75, 192, 192, 1)',
				fill: false,
			}]
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
		    scales: {
		        yAxes: [{
		            ticks: {
		                beginAtZero:true
		            }
		        }]
		    }
		}
	});
});

$("#consumoTotalDia").ready( function() {
	var ctx = document.getElementById("consumoTotalDia").getContext('2d');

	var dataToPlot = []; labelsToPlot = [];

	for(var i = 0; i < newDataDia.length; i++) {
		dataToPlot.push(newDataDia[i].split(' ')[1]);
		labelsToPlot.push(newDataDia[i].split(' ')[0]);
    }

	var myChart = new Chart(ctx, {
        type: 'line',
        data: {
			labels: labelsToPlot,
			datasets: [{
				label: 'Consumo do último dia',
				steppedLine: false,
				data: dataToPlot,
				borderColor: 'rgba(75, 192, 192, 1)',
				fill: false,
			}]
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
		    scales: {
		        yAxes: [{
		            ticks: {
		                beginAtZero:true
		            }
		        }]
		    }
		}
	});
});

//consumo local
//mes
$("#consumoLocalmes").ready( function() {
	var ctx = document.getElementById("consumoLocalmes").getContext('2d');

	var dataToPlot = []; labelsToPlot = [];

	for(var i = 0; i < newData.length; i++) {
		dataToPlot.push(newData[i].split(' ')[1]);
		labelsToPlot.push("Dia " + newData[i].split(' ')[0]);
    }

	var myChart = new Chart(ctx, {
        type: 'line',
        data: {
			labels: labelsToPlot,
			datasets: [{
				label: 'Consumo dos últimos 30 dias',
				steppedLine: false,
				data: dataToPlot,
				borderColor: 'rgba(75, 192, 192, 1)',
				fill: false,
			}]
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
		    scales: {
		        yAxes: [{
		            ticks: {
		                beginAtZero:true
		            }
		        }]
		    }
		}
	});
});
//semana
$("#consumoLocalSemana").ready( function() {
	var ctx = document.getElementById("consumoLocalSemana").getContext('2d');

	var dataToPlot = []; labelsToPlot = [];

	for(var i = 0; i < newData.length; i++) {
		dataToPlot.push(newData[i].split(' ')[1]);
		labelsToPlot.push("Dia " + newData[i].split(' ')[0]);
    }

	var myChart = new Chart(ctx, {
        type: 'line',
        data: {
			labels: labelsToPlot,
			datasets: [{
				label: 'Consumo dos últimos 7 dias',
				steppedLine: false,
				data: dataToPlot,
				borderColor: 'rgba(75, 192, 192, 1)',
				fill: false,
			}]
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
		    scales: {
		        yAxes: [{
		            ticks: {
		                beginAtZero:true
		            }
		        }]
		    }
		}
	});
});