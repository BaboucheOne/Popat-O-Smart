import * as React from 'react';
import { LineChart } from '@mui/x-charts/LineChart';

export default function BasicLineChart({ xAxisData, chartData }: { xAxisData: number[], chartData: number[] }) {
  return (
    <LineChart
      xAxis={[{ data: xAxisData, scaleType: 'time', tickInterval: xAxisData, label: 'time (s)' }]}
      series={[
        {
          data: chartData,
          label: 'Humidity (%)',
        },
      ]}
      width={window.innerWidth}
      height={window.innerHeight}
    />
  );
}
