import React from 'react';
import './App.css';
import BasicLineChart from "./BasicLineChat";
import {GetReportsResponse} from "./GetReportsResponse";
import ReportCard from "./ReportCard";
import PlantStatus from "./PlantStatus";

function App() {
  const [chartData, setChartData] = React.useState<number[]>([]);
  const [xAxisData, setXAxisData] = React.useState<number[]>([]);

  React.useEffect(() => {
    fetch('http://127.0.0.1:8000/c303282d-f2e6-46ca-a04a-35d3d873712d/reports')
      .then(response => response.json())
      .then((data: GetReportsResponse) => {

        const timestamps = data.reports.map(report => report.timestamp);
        const humidityValues = data.reports.map(report => report.humidity);

        setXAxisData(timestamps);
        setChartData(humidityValues);
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh',
      width: '100vw',
      flexDirection: 'column',
      boxSizing: 'border-box'
    }}>
      <h1>My plant!</h1>
      <PlantStatus isConnected={xAxisData.length > 0}></PlantStatus>
      <ReportCard numberOfReports={xAxisData.length}/>
      <BasicLineChart xAxisData={xAxisData} chartData={chartData}/>
    </div>
  );
}


export default App;
