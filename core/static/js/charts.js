/* Arquivo definido para armazenar as configs destinadas 
   ao plot dos gráficos da plataforma. */

   $("#HumidadeSolo").ready( function() {
	var ctx = document.getElementById("HumidadeSolo").getContext('2d');
	var datasets = [];
	var labels = [];

	console.log(dataHumSolo);

	for(var i = 0; i < dataHumSolo.length; i++) {
		var dataToPlot = []; labelsToPlot = [];
		for (var j=0; j < dataHumSolo[i].length; j++){
			dataToPlot.push(dataHumSolo[i][j].split('#')[1]);
			labelsToPlot.push(dataHumSolo[i][j].split('#')[0]);
		}
		datasets.push({
			label: idSensores[i],
			steppedLine: false,
			data: dataToPlot,
			//borderColor: 'rgba(75, 192, 192, 1)',
			fill: false,
		});
		if (i==0)
			labels = labelsToPlot;
    }

	var myChart = new Chart(ctx, {
        type: 'line',
        data: {
			labels: labels,
			datasets: datasets
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

$("#HumidadeAr").ready( function() {
	var ctx = document.getElementById("HumidadeAr").getContext('2d');
	var datasets = [];
	var labels = [];


	for(var i = 0; i < dataHumAr.length; i++) {
		var dataToPlot = []; labelsToPlot = [];
		for (var j=0; j < dataHumAr[i].length; j++){
			dataToPlot.push(dataHumAr[i][j].split('#')[1]);
			labelsToPlot.push(dataHumAr[i][j].split('#')[0]);
		}
		datasets.push({
			label: idSensores[i],
			steppedLine: false,
			data: dataToPlot,
			//borderColor: 'rgba(75, 192, 192, 1)',
			fill: false,
		});
		if (i==0)
			labels = labelsToPlot;
    }

	var myChart = new Chart(ctx, {
        type: 'line',
        data: {
			labels: labels,
			datasets: datasets
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

$("#Temperatura").ready( function() {
	var ctx = document.getElementById("Temperatura").getContext('2d');
	var datasets = [];
	var labels = [];

	for(var i = 0; i < dataTemp.length; i++) {
		var dataToPlot = []; labelsToPlot = [];
		for (var j=0; j < dataTemp[i].length; j++){
			dataToPlot.push(dataTemp[i][j].split('#')[1]);
			labelsToPlot.push(dataTemp[i][j].split('#')[0]);
		}
		datasets.push({
			label: idSensores[i],
			steppedLine: false,
			data: dataToPlot,
			//borderColor: 'rgba(75, 192, 192, 1)',
			fill: false,
		});
		if (i==0)
			labels = labelsToPlot;
    }

	var myChart = new Chart(ctx, {
        type: 'line',
        data: {
			labels: labels,
			datasets: datasets
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