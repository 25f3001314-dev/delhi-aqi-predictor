let aqiChart;

async function fetchCurrentAQI() {
    try {
        // Try real-time API first
        const response = await fetch('/api/real-time');
        const data = await response.json();
        
        if (data.aqi) {
            document.getElementById('aqiNumber').textContent = data.aqi;
            
            // Determine category
            let category, color;
            if (data.aqi <= 50) {
                category = 'Good';
                color = '#00e400';
            } else if (data.aqi <= 100) {
                category = 'Moderate';
                color = '#ffff00';
            } else if (data.aqi <= 150) {
                category = 'Unhealthy for Sensitive Groups';
                color = '#ff7e00';
            } else if (data.aqi <= 200) {
                category = 'Unhealthy';
                color = '#ff0000';
            } else if (data.aqi <= 300) {
                category = 'Very Unhealthy';
                color = '#8f3f97';
            } else {
                category = 'Hazardous';
                color = '#7e0023';
            }
            
            document.getElementById('categoryValue').textContent = category;
            document.getElementById('pm25Value').textContent = data.pm25 || '--';
            document.getElementById('pm10Value').textContent = data.pm10 || '--';
            document.getElementById('temperature').textContent = data.temp || '--';
            document.getElementById('humidity').textContent = (data.humidity || '--') + ' %';
            document.getElementById('windSpeed').textContent = '--' + ' km/h';
            document.getElementById('lastUpdated').textContent = new Date().toLocaleString();
            
            // Update colors based on AQI
            document.getElementById('aqiNumber').style.color = color;
            document.getElementById('categoryValue').style.color = color;
        }
        
    } catch (error) {
        console.error('Error fetching current AQI:', error);
        // Fallback to default values
        document.getElementById('aqiNumber').textContent = '180';
        document.getElementById('categoryValue').textContent = 'Unhealthy';
    }
}

async function fetchHistoricalData() {
    try {
        const response = await fetch('/api/historical');
        const data = await response.json();
        
        // Find min and max
        const values = data.map(d => d.aqi);
        const minAqi = Math.min(...values);
        const maxAqi = Math.max(...values);
        const minIndex = values.indexOf(minAqi);
        const maxIndex = values.indexOf(maxAqi);
        
        document.getElementById('minAqi').textContent = minAqi;
        document.getElementById('maxAqi').textContent = maxAqi;
        document.getElementById('minTime').textContent = data[minIndex].timestamp;
        document.getElementById('maxTime').textContent = data[maxIndex].timestamp;
        
        renderChart(data);
    } catch (error) {
        console.error('Error fetching historical data:', error);
    }
}

function renderChart(data) {
    const ctx = document.getElementById('aqiChart').getContext('2d');
    
    if (aqiChart) {
        aqiChart.destroy();
    }
    
    const labels = data.map(d => d.timestamp);
    const aqiValues = data.map(d => d.aqi);
    
    // Color bars based on AQI value
    const barColors = aqiValues.map(aqi => {
        if (aqi <= 50) return '#00e400';
        if (aqi <= 100) return '#ffff00';
        if (aqi <= 150) return '#ff7e00';
        if (aqi <= 200) return '#ff0000';
        if (aqi <= 300) return '#8f3f97';
        return '#7e0023';
    });
    
    aqiChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'New Delhi',
                data: aqiValues,
                backgroundColor: barColors,
                borderWidth: 0,
                barThickness: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return 'AQI: ' + context.parsed.y;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 400,
                    title: {
                        display: true,
                        text: 'AQI (US)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Time'
                    },
                    ticks: {
                        maxTicksLimit: 12
                    }
                }
            }
        }
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    fetchCurrentAQI();
    fetchHistoricalData();
    
    // Refresh every 5 minutes
    setInterval(fetchCurrentAQI, 300000);
    setInterval(fetchHistoricalData, 300000);
    
    // Manual refresh button
    document.querySelector('.refresh-btn').addEventListener('click', () => {
        fetchCurrentAQI();
        fetchHistoricalData();
    });
});
